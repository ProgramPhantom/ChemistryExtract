import os
import json
import difflib
import typing
from pydantic import BaseModel
from chemstractor.lib.processor import PDFProcessor
from chemstractor.lib.validate import validate_flory_entry, validate_mark_houwink_entry

def load_cache(cache_path: str) -> dict:
    """Loads the chemical cache from a JSON file."""
    if not cache_path or not os.path.exists(cache_path):
        return {}
    try:
        with open(cache_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
    except Exception:
        pass
    return {}


def save_cache(cache_path: str, cache: dict) -> None:
    """Saves the chemical cache to a JSON file."""
    if not cache_path:
        return
    try:
        # Ensure parent directory exists
        parent = os.path.dirname(cache_path)
        if parent and not os.path.exists(parent):
            os.makedirs(parent, exist_ok=True)
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(cache, f, indent=2, ensure_ascii=False)
    except Exception:
        pass


def find_fuzzy_match(dirty_name: str, cache: dict, threshold: float = 0.9) -> str | None:
    """
    Checks if a dirty name matches a key in the cache exactly (case-insensitive)
    or is already a clean name (value in the cache), or fuzzy matches a key in the cache.
    """
    dirty_name_clean = dirty_name.strip()
    if not dirty_name_clean:
        return None

    # 1. Exact match in keys (case-sensitive)
    if dirty_name_clean in cache:
        return cache[dirty_name_clean]

    # 2. Case-insensitive match in keys
    dirty_lower = dirty_name_clean.lower()
    for key, val in cache.items():
        if key.lower().strip() == dirty_lower:
            return val

    # 3. Direct match with existing clean values
    clean_names = set(cache.values())
    if dirty_name_clean in clean_names:
        return dirty_name_clean
    for val in clean_names:
        if val.lower().strip() == dirty_lower:
            return val

    # 4. Fuzzy match against keys
    keys = list(cache.keys())
    matches = difflib.get_close_matches(dirty_name_clean, keys, n=1, cutoff=threshold)
    if matches:
        return cache[matches[0]]

    return None

def select_from_existing_names(dirty_name: str, clean_names: list[str], ai_instance) -> str:
    """Uses the AI to match the dirty name against existing clean names using a dynamic Literal schema."""
    if not clean_names:
        return "not found"

    # Append "not found" to the options
    options = list(clean_names) + ["not found"]
    options_tuple = tuple(options)
    LiteralType = typing.Literal[options_tuple]

    class ChemicalMatch(BaseModel):
        match: LiteralType

    prompt = (
        f"You are a chemistry data specialist. We have a dirty or variant chemical name extracted from a paper.\n"
        f"Your task is to identify if it matches or refers to one of the clean, canonical chemical names listed below.\n\n"
        f"Dirty Chemical Name: '{dirty_name}'\n\n"
        f"Canonical Options:\n" + "\n".join(f"- {name}" for name in clean_names) + "\n\n"
        f"If the dirty name refers to one of the canonical options, select that option exactly.\n"
        f"If it does not match any of the canonical options, select 'not found'."
    )

    system_instruction = (
        "You must select exactly one of the provided canonical chemical name options, or 'not found' if there is no match. "
        "Do not make up new names in this step."
    )

    res = ai_instance.prompt(
        prompt=prompt,
        schema=ChemicalMatch,
        system_instruction=system_instruction,
        temperature=0.0
    )

    if res.success and res.data:
        return res.data.match
    else:
        return "not found"


CHEMICAL_ERROR_TYPES = ["Not found", "Invalid chemical"]
DATA_ERROR_TYPES = ["Not found", "Derivation too complex", "Out of range"]
ALL_ERROR_TYPES = ["Not found", "Invalid chemical", "Derivation too complex", "Out of range"]


ERROR_TARGET_MAP = {
    "not found": "Not found",
    "not_found": "Not found",
    "n/a": "Not found",
    "none": "Not found",
    "null": "Not found",
    "missing": "Not found",
    "invalid chemical": "Invalid chemical",
    "invalid_chemical": "Invalid chemical",
    "invalid": "Invalid chemical",
    "invalid chemical name": "Invalid chemical",
    "derivation too complex": "Derivation too complex",
    "derivation_too_complex": "Derivation too complex",
    "too complex": "Derivation too complex",
    "complex derivation": "Derivation too complex",
    "out of range": "Out of range",
    "out_of_range": "Out of range",
    "outside range": "Out of range"
}


def check_prepopulated_error(val: typing.Any, valid_errors: list[str] = ALL_ERROR_TYPES) -> str | None:
    """
    Checks if a field value is a pre-populated error message from an earlier stage using fuzzy matching.
    Returns the canonical error string if matched, or None.
    """
    if val is None:
        return None

    val_str = str(val).strip()
    if not val_str:
        return "Not found" if "Not found" in valid_errors else valid_errors[0]

    # Normalize punctuation, underscores, and hyphens
    normalized_val = val_str.lower().replace("_", " ").replace("-", " ").strip()

    # 1. Direct match against normalized alias map
    if normalized_val in ERROR_TARGET_MAP:
        err = ERROR_TARGET_MAP[normalized_val]
        if err in valid_errors:
            return err

    # 2. Direct match against canonical valid errors
    for err in valid_errors:
        if normalized_val == err.lower():
            return err

    # 3. Fuzzy similarity match against all alias targets for valid errors
    relevant_targets = [t for t, err in ERROR_TARGET_MAP.items() if err in valid_errors]
    matches = difflib.get_close_matches(normalized_val, relevant_targets, n=1, cutoff=0.7)
    if matches:
        return ERROR_TARGET_MAP[matches[0]]

    # 4. Fallback fuzzy match against canonical valid_errors strings directly
    canonical_matches = difflib.get_close_matches(val_str, valid_errors, n=1, cutoff=0.7)
    if canonical_matches:
        return canonical_matches[0]

    return None


def generate_new_clean_chemical_name(dirty_name: str, ai_instance) -> str:
    """Uses the AI to generate a new canonical name for a chemical string, or 'Invalid chemical' if it is not a valid chemical."""
    class ChemicalGeneration(BaseModel):
        clean_name: str

    prompt = (
        f"You are an expert chemist. You will be given a raw, dirty, or abbreviated chemical name extracted from scientific literature.\n"
        f"Your task is to convert it into a standard, clean, and canonical polymer or solvent chemical name. E.g., expand acronyms where clear (like 'PMMA' to 'poly(methyl methacrylate)'), "
        f"or correct typos/formatting issues (like 'T0luene' to 'toluene' or 'THF-d8' to 'THF-d8' or 'CDCl3' to 'chloroform-d').\n\n"
        f"Raw chemical name: '{dirty_name}'\n\n"
        f"Rules:\n"
        f"1. Create a clean, nicely formatted chemical name using standard nomenclature.\n"
        f"2. If the input is not a specific polymer or solvent chemical compound—for instance, if it refers to general material or biological categories (e.g., 'globular proteins', 'finite rods', 'polyelectrolytes'), non-chemical text (e.g. noise, page numbers, citations), or ambiguous non-specific classes—you MUST respond exactly with 'Invalid chemical'.\n"
        f"3. Do not include extra text, explanations, or quotes."
    )

    system_instruction = (
        "Generate a clean, standard chemical name. Respond with 'Invalid chemical' if the text does not represent a specific polymer or solvent chemical compound."
    )

    res = ai_instance.prompt(
        prompt=prompt,
        schema=ChemicalGeneration,
        system_instruction=system_instruction,
        temperature=0.0
    )

    if res.success and res.data:
        return res.data.clean_name.strip()
    else:
        return "Invalid chemical"


def homogenise_chemical(raw_name: str, cache: dict, ai_instance, stats: dict) -> tuple[str, str, str]:
    """
    Homogenises a raw name and updates stats.
    Returns:
    (clean_name, source, fail_reason)
    source is one of "cache", "ai_match", "ai_generate", or "fail".
    """
    try:
        if not raw_name or not str(raw_name).strip():
            stats["total_processed"] += 1
            stats["failed"] += 1
            return "N/A", "fail", "Not found"

        raw_name_clean = str(raw_name).strip()

        # Check if raw_name is a pre-populated error message
        pre_err = check_prepopulated_error(raw_name_clean, CHEMICAL_ERROR_TYPES + ["Derivation too complex", "Out of range"])
        if pre_err:
            stats["total_processed"] += 1
            stats["failed"] += 1
            err_reason = pre_err if pre_err in CHEMICAL_ERROR_TYPES else "Not found"
            return raw_name_clean, "fail", err_reason

        stats["total_processed"] += 1

        # 1. Check cache (including fuzzy matches)
        cached_val = find_fuzzy_match(raw_name_clean, cache)
        if cached_val:
            stats["cache_hits"] += 1
            return cached_val, "cache", ""

        # 2. Select from existing clean names in the cache
        clean_names = sorted(list(set(cache.values())))
        clean_names = [n for n in clean_names if n and n.upper() not in ("N/A", "INVALID CHEMICAL")]

        match_val = "not found"
        if clean_names:
            match_val = select_from_existing_names(raw_name_clean, clean_names, ai_instance)

        if match_val != "not found" and match_val in clean_names:
            cache[raw_name_clean] = match_val
            stats["ai_match_hits"] += 1
            return match_val, "ai_match", ""

        # 3. Generate new clean name
        generated_val = generate_new_clean_chemical_name(raw_name_clean, ai_instance)
        if not generated_val or generated_val.lower() in ("invalid chemical", "n/a", "not found"):
            stats["failed"] += 1
            err_reason = "Invalid chemical" if (generated_val and generated_val.lower() in ("invalid chemical", "n/a")) else "Not found"
            return raw_name_clean, "fail", err_reason

        # Save the generated name to the cache
        cache[raw_name_clean] = generated_val
        stats["ai_generated"] += 1
        return generated_val, "ai_generate", ""
    except BaseException as e:
        if isinstance(e, (KeyboardInterrupt, SystemExit)):
            raise e
        stats["failed"] += 1
        return raw_name, "fail", f"Unexpected error during name homogenisation: {str(e)}"


def check_entry_data_errors(entry: dict, data_fields: list[str], paper_name: str, table_name: str, failures: list) -> list[str]:
    """
    Checks numerical data point fields in an entry for pre-populated error messages (e.g. 'Not found', 'Derivation too complex', 'Out of range').
    Appends failure objects to failures list and returns a list of failed field names.
    """
    failed_data_fields = []
    checked_base_fields = set()

    for field in data_fields:
        val = entry.get(field)
        if val is None:
            continue

        base_field = field.replace("raw_", "")
        err = check_prepopulated_error(val, DATA_ERROR_TYPES)
        if err:
            if base_field not in checked_base_fields:
                checked_base_fields.add(base_field)
                failed_data_fields.append(base_field)
                failures.append({
                    "source_paper": paper_name,
                    "table": table_name,
                    "field": base_field,
                    "value": str(val),
                    "reason": err
                })
    return failed_data_fields


def process_mark_houwink_entries(
    proc: PDFProcessor,
    paper_name: str,
    cache: dict,
    ai_instance,
    stats: dict,
    mh_results: list,
    failures: list
) -> int:
    """Processes Mark-Houwink interpretation data for a single paper, homogenising chemical names."""
    paper_mh_count = 0
    for i, mh_data in enumerate(proc.interpretation_mh_data_list):
        if not mh_data:
            continue
        table_name = f"table{i + 1}"
        mh_entries = mh_data.get("mh_entries", [])
        for entry in mh_entries:
            polymer_raw = entry.get("polymer_name", "")
            solvent_raw = entry.get("solvent", "")

            poly_clean, poly_source, poly_fail_reason = homogenise_chemical(
                polymer_raw, cache, ai_instance, stats
            )
            failed_fields = []
            if poly_fail_reason:
                failed_fields.append("polymer_name")
                failures.append({
                    "source_paper": paper_name,
                    "table": table_name,
                    "field": "polymer_name",
                    "value": polymer_raw,
                    "reason": poly_fail_reason
                })

            solv_clean, solv_source, solv_fail_reason = homogenise_chemical(
                solvent_raw, cache, ai_instance, stats
            )
            if solv_fail_reason:
                failed_fields.append("solvent")
                failures.append({
                    "source_paper": paper_name,
                    "table": table_name,
                    "field": "solvent",
                    "value": solvent_raw,
                    "reason": solv_fail_reason
                })

            # Check numerical data point fields for errors
            data_failed = check_entry_data_errors(
                entry,
                ["K_value", "raw_K_value", "a_value", "raw_a_value", "temperature_k"],
                paper_name,
                table_name,
                failures
            )
            failed_fields.extend(data_failed)

            # Numerical bounds outlier checking for Mark-Houwink coefficients
            bounds_failed = validate_mark_houwink_entry(entry, paper_name, table_name, failures)
            for f in bounds_failed:
                if f not in failed_fields:
                    failed_fields.append(f)

            # Create clean entry
            clean_entry = entry.copy()
            clean_entry["polymer_name_original"] = polymer_raw
            clean_entry["polymer_name"] = poly_clean
            clean_entry["solvent_original"] = solvent_raw
            clean_entry["solvent"] = solv_clean
            clean_entry["source_paper"] = paper_name
            clean_entry["table_name"] = table_name
            clean_entry["failed_fields"] = ", ".join(failed_fields) if failed_fields else "None"

            mh_results.append(clean_entry)
            paper_mh_count += 1

    return paper_mh_count


def process_flory_entries(
    proc: PDFProcessor,
    paper_name: str,
    cache: dict,
    ai_instance,
    stats: dict,
    flory_results: list,
    failures: list
) -> int:
    """Processes Flory interpretation data for a single paper, homogenising chemical names."""
    paper_flory_count = 0

    for i, flory_data in enumerate(proc.interpretation_flory_data_list):
        if not flory_data:
            continue
        table_name = f"table{i + 1}"
        flory_entries = flory_data.get("flory_entries", [])

        for entry in flory_entries:
            polymer_raw = entry.get("polymer_name", "")
            solvent_raw = entry.get("solvent", "")

            poly_clean, poly_source, poly_fail_reason = homogenise_chemical(
                polymer_raw, cache, ai_instance, stats
            )

            failed_fields = []
            if poly_fail_reason:
                failed_fields.append("polymer_name")
                failures.append({
                    "source_paper": paper_name,
                    "table": table_name,
                    "field": "polymer_name",
                    "value": polymer_raw,
                    "reason": poly_fail_reason
                })

            solv_clean, solv_source, solv_fail_reason = homogenise_chemical(
                solvent_raw, cache, ai_instance, stats
            )
            if solv_fail_reason:
                failed_fields.append("solvent")
                failures.append({
                    "source_paper": paper_name,
                    "table": table_name,
                    "field": "solvent",
                    "value": solvent_raw,
                    "reason": solv_fail_reason
                })

            # Check numerical data point fields for errors
            data_failed = check_entry_data_errors(
                entry,
                ["v_value", "raw_v_value", "c_value", "raw_c_value", "temperature_k"],
                paper_name,
                table_name,
                failures
            )
            failed_fields.extend(data_failed)

            # Numerical bounds outlier checking for Flory coefficients
            bounds_failed = validate_flory_entry(entry, paper_name, table_name, failures)
            for f in bounds_failed:
                if f not in failed_fields:
                    failed_fields.append(f)

            # Create clean entry
            clean_entry = entry.copy()
            clean_entry["polymer_name_original"] = polymer_raw
            clean_entry["polymer_name"] = poly_clean
            clean_entry["solvent_original"] = solvent_raw
            clean_entry["solvent"] = solv_clean
            clean_entry["source_paper"] = paper_name
            clean_entry["table_name"] = table_name
            clean_entry["failed_fields"] = ", ".join(failed_fields) if failed_fields else "None"

            flory_results.append(clean_entry)
            paper_flory_count += 1

    return paper_flory_count


def gather_and_homogenise(processors: list[PDFProcessor], cache_path: str, ai_instance):
    """
    Processes all loaded PDFProcessor instances, extracts polymer and solvent names from their interpretation
    data, homogenises them using the 4-stage pipeline, updates the cache, and aggregates the results.
    Yields progress dictionary events during execution.
    """
    cache = load_cache(cache_path)

    mh_results = []
    flory_results = []
    failures = []

    stats = {
        "total_processed": 0,
        "cache_hits": 0,
        "ai_match_hits": 0,
        "ai_generated": 0,
        "failed": 0
    }

    total_papers = len(processors)

    papers_summary = []

    for idx, proc in enumerate(processors):
        paper_name = proc.base_no_ext
        yield {
            "status": "paper_start",
            "paper_idx": idx,
            "paper_name": paper_name,
            "total_papers": total_papers
        }

        # Check if interpretation results are present
        if not proc.interpretation_flory_data_list and not proc.interpretation_mh_data_list:
            title = "N/A"
            if getattr(proc, 'metadata_res', None) and proc.metadata_res.success and proc.metadata_res.data:
                title = proc.metadata_res.data.get("title") or "N/A"
            elif proc.command_outputs and proc.command_outputs.get("metadata"):
                meta_dict = proc.command_outputs["metadata"]
                if isinstance(meta_dict, dict):
                    title = meta_dict.get("title") or "N/A"

            papers_summary.append({
                "source_paper": paper_name,
                "title": title,
                "total_tables": proc.num_tables or len(proc.cat_data_list),
                "selected_tables": 0,
                "flory_count": 0,
                "mh_count": 0,
                "failed_count": 0
            })

            yield {
                "status": "paper_complete",
                "paper_idx": idx,
                "paper_name": paper_name,
                "total_papers": total_papers,
                "mh_count": 0,
                "flory_count": 0
            }
            continue

        paper_mh_count = 0
        paper_flory_count = 0

        try:
            paper_mh_count = process_mark_houwink_entries(
                proc, paper_name, cache, ai_instance, stats, mh_results, failures
            )
        except BaseException as e:
            if isinstance(e, (KeyboardInterrupt, SystemExit)):
                raise e
            failures.append({
                "source_paper": paper_name,
                "table": "N/A",
                "field": "Mark-Houwink processing",
                "value": "N/A",
                "reason": f"Unexpected error during Mark-Houwink homogenisation: {str(e)}"
            })

        try:
            paper_flory_count = process_flory_entries(
                proc, paper_name, cache, ai_instance, stats, flory_results, failures
            )
        except BaseException as e:
            if isinstance(e, (KeyboardInterrupt, SystemExit)):
                raise e
            failures.append({
                "source_paper": paper_name,
                "table": "N/A",
                "field": "Flory processing",
                "value": "N/A",
                "reason": f"Unexpected error during Flory homogenisation: {str(e)}"
            })

        title = "N/A"
        if getattr(proc, 'metadata_res', None) and proc.metadata_res.success and proc.metadata_res.data:
            title = proc.metadata_res.data.get("title") or "N/A"
        elif proc.command_outputs and proc.command_outputs.get("metadata"):
            meta_dict = proc.command_outputs["metadata"]
            if isinstance(meta_dict, dict):
                title = meta_dict.get("title") or "N/A"

        total_tables = proc.num_tables or len(proc.cat_data_list)
        selected_tables = sum(
            1 for c in proc.cat_data_list if c and (c.get("contains_mark_houwink_parameters") or c.get("contains_flory_parameters"))
        )
        if selected_tables == 0:
            selected_tables = max(len(proc.interpretation_flory_data_list), len(proc.interpretation_mh_data_list))

        paper_failed_count = sum(1 for f in failures if f.get("source_paper") == paper_name)

        papers_summary.append({
            "source_paper": paper_name,
            "title": title,
            "total_tables": total_tables,
            "selected_tables": selected_tables,
            "flory_count": paper_flory_count,
            "mh_count": paper_mh_count,
            "failed_count": paper_failed_count
        })

        yield {
            "status": "paper_complete",
            "paper_idx": idx,
            "paper_name": paper_name,
            "total_papers": total_papers,
            "mh_count": paper_mh_count,
            "flory_count": paper_flory_count
        }

    save_cache(cache_path, cache)

    results = {
        "mark_houwink_entries": mh_results,
        "flory_entries": flory_results,
        "failures": failures,
        "stats": stats,
        "papers_summary": papers_summary
    }
    yield {
        "status": "complete",
        "results": results
    }
