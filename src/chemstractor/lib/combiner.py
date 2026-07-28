import os
import json
import difflib
import typing
from pydantic import BaseModel
from chemstractor.lib.processor import PDFProcessor
from chemstractor.lib.validate import validate_flory_entry, validate_mark_houwink_entry


INTERPRETATION_SUCCESS_THRESHOLD = 0.70

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
    except Exception as e:
        print(f"Warning: Failed to save chemical cache to '{cache_path}': {e}")


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
    clean_names = set(v for v in cache.values() if v and v.upper() not in ("N/A", "INVALID CHEMICAL"))
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

    dirty_name_str = str(dirty_name).strip() if dirty_name else ""
    if not dirty_name_str:
        return "Invalid chemical"

    prompt = (
        f"You are an expert chemist. You will be given a raw, dirty, or abbreviated chemical name extracted from scientific literature.\n"
        f"CRITICAL WARNING: The input text may contain hallucinations, corrupt OCR fragments, noise, or nonsense text fragments (e.g., 'uma') resulting from previous extraction steps.\n\n"
        f"Raw chemical name: '{dirty_name_str}'\n\n"
        f"Rules:\n"
        f"1. Create a clean, nicely formatted chemical name using standard nomenclature ONLY IF the input string clearly and unambiguously represents a specific polymer or solvent compound (or standard acronym/variant, e.g., 'PMMA' to 'poly(methyl methacrylate)', 'T0luene' to 'toluene', 'CDCl3' to 'chloroform-d').\n"
        f"2. DO NOT GUESS OR HALLUCINATE: You MUST NOT invent, hallucinate, or extrapolate a chemical name from a corrupt string, nonsense fragment, or unrecognized word. For example, if given a hallucinated fragment like 'uma', DO NOT guess '1,2,4-trichlorobenzene' or any other solvent/polymer. You MUST respond exactly with 'Invalid chemical'.\n"
        f"3. If the input is not a specific polymer or solvent chemical compound—for instance, if it refers to general material or biological categories (e.g., 'globular proteins', 'finite rods', 'polyelectrolytes'), non-chemical text (e.g. noise, page numbers, citations), corrupt text fragments (e.g. 'uma'), or ambiguous non-specific classes—you MUST respond exactly with 'Invalid chemical'.\n"
        f"4. Do not include extra text, explanations, or quotes."
    )

    system_instruction = (
        "Generate a clean, standard chemical name if the input is a valid chemical or standard acronym. "
        "Strictly respond with 'Invalid chemical' if the text is a hallucinated fragment (e.g. 'uma'), corrupt/nonsense string, or non-specific category. "
        "NEVER invent or guess a chemical compound for ambiguous or corrupt text."
    )

    res = ai_instance.prompt(
        prompt=prompt,
        schema=ChemicalGeneration,
        system_instruction=system_instruction,
        temperature=0.0
    )

    if res.success and res.data:
        clean_val = res.data.clean_name.strip()
        if clean_val.lower() in ("invalid chemical", "n/a", "none", "null", "not found", ""):
            return "Invalid chemical"
        return clean_val
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
            if cached_val.lower() in ("invalid chemical", "n/a", "not found"):
                stats["cache_hits"] += 1
                stats["failed"] += 1
                return raw_name_clean, "fail", "Invalid chemical"
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
            cache[raw_name_clean] = "Invalid chemical"
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


def check_entry_data_errors(entry: dict, data_fields: list[str], paper_name: str, table_name: str, failures: list) -> dict[str, str]:
    """
    Checks numerical data point fields in an entry for pre-populated error messages (e.g. 'Not found', 'Derivation too complex', 'Out of range').
    Appends failure objects to failures list and returns a dict mapping base field name -> error reason.
    """
    failed_data_dict = {}
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
                failed_data_dict[base_field] = err
                failures.append({
                    "source_paper": paper_name,
                    "table": table_name,
                    "field": base_field,
                    "value": str(val),
                    "reason": err
                })
    return failed_data_dict
def try_parse_float(val: typing.Any) -> float | None:
    """Attempts to parse a value into a float, returning None if not possible."""
    if val is None:
        return None
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        val_str = val.strip()
        if not val_str:
            return None
        try:
            return float(val_str)
        except ValueError:
            return None
    return None


def process_mark_houwink_entries(
    processor: PDFProcessor,
    paper_name: str,
    cache: dict,
    ai_instance,
    stats: dict,
    mh_results: list
) -> int:
    """Processes Mark-Houwink interpretation data for a single paper, homogenising chemical names."""
    paper_mh_count = 0

    for i, mh_data in enumerate(processor.interpretation_mh_data_list):
        if not mh_data:
            continue
        table_name = f"table{i + 1}"
        mh_entries = mh_data.get("mark_houwink_entries", [])

        for entry in mh_entries:
            polymer_raw = entry.get("polymer_name", "")
            solvent_raw = entry.get("solvent", "")

            poly_clean, poly_source, poly_fail_reason = homogenise_chemical(
                polymer_raw, cache, ai_instance, stats
            )

            solv_clean, solv_source, solv_fail_reason = homogenise_chemical(
                solvent_raw, cache, ai_instance, stats
            )

            temp_raw = entry.get("temperature_k")
            temp_parsed = try_parse_float(temp_raw)
            temp_missing = (
                temp_parsed is None or
                check_prepopulated_error(temp_raw, DATA_ERROR_TYPES) is not None
            )

            k_raw = entry.get("K_value")
            k_parsed = try_parse_float(k_raw)

            a_raw = entry.get("a_value")
            a_parsed = try_parse_float(a_raw)

            entry_for_validation = entry.copy()
            if k_parsed is not None:
                entry_for_validation["K_value"] = k_parsed
            if a_parsed is not None:
                entry_for_validation["a_value"] = a_parsed

            bounds_failed = validate_mark_houwink_entry(entry_for_validation)

            k_invalid = (
                k_parsed is None or
                check_prepopulated_error(k_raw, DATA_ERROR_TYPES) is not None or
                bounds_failed.get("K_value_out_of_range", False)
            )

            a_invalid = (
                a_parsed is None or
                check_prepopulated_error(a_raw, DATA_ERROR_TYPES) is not None or
                bounds_failed.get("a_value_out_of_range", False)
            )

            failed_fields = {
                "solvent_name": bool(solv_fail_reason or solv_clean in (None, "N/A", "Invalid chemical")),
                "polymer_name": bool(poly_fail_reason or poly_clean in (None, "N/A", "Invalid chemical")),
                "temperature_missing": temp_missing,
                "K_value_out_of_range": k_invalid,
                "a_value_out_of_range": a_invalid,
                "eta_out_of_range": bounds_failed.get("eta_out_of_range", False)
            }

            clean_entry = entry.copy()
            clean_entry["polymer_name_original"] = polymer_raw
            clean_entry["polymer_name"] = poly_clean
            clean_entry["solvent_original"] = solvent_raw
            clean_entry["solvent"] = solv_clean
            clean_entry["source_paper"] = paper_name
            clean_entry["table_name"] = table_name
            if k_parsed is not None:
                clean_entry["K_value"] = k_parsed
            if a_parsed is not None:
                clean_entry["a_value"] = a_parsed
            if temp_parsed is not None:
                clean_entry["temperature_k"] = temp_parsed
            clean_entry["failed_fields"] = failed_fields

            mh_results.append(clean_entry)
            paper_mh_count += 1

    return paper_mh_count


def process_flory_entries(
    processor: PDFProcessor,
    paper_name: str,
    cache: dict,
    ai_instance,
    stats: dict,
    flory_results: list
) -> int:
    """Processes Flory interpretation data for a single paper, homogenising chemical names."""
    paper_flory_count = 0

    for i, flory_data in enumerate(processor.interpretation_flory_data_list):
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

            solv_clean, solv_source, solv_fail_reason = homogenise_chemical(
                solvent_raw, cache, ai_instance, stats
            )

            temp_raw = entry.get("temperature_k")
            temp_parsed = try_parse_float(temp_raw)
            temp_missing = (
                temp_parsed is None or
                check_prepopulated_error(temp_raw, DATA_ERROR_TYPES) is not None
            )

            c_raw = entry.get("c_value")
            c_parsed = try_parse_float(c_raw)
            c_missing = (
                c_parsed is None or
                check_prepopulated_error(c_raw, DATA_ERROR_TYPES) is not None
            )

            v_raw = entry.get("v_value")
            v_parsed = try_parse_float(v_raw)

            entry_for_validation = entry.copy()
            if c_parsed is not None:
                entry_for_validation["c_value"] = c_parsed
            if v_parsed is not None:
                entry_for_validation["v_value"] = v_parsed

            bounds_failed = validate_flory_entry(entry_for_validation)

            v_invalid = (
                v_parsed is None or
                check_prepopulated_error(v_raw, DATA_ERROR_TYPES) is not None or
                bounds_failed.get("v_value_out_of_range", False)
            )

            failed_fields = {
                "solvent_name": bool(solv_fail_reason or solv_clean in (None, "N/A", "Invalid chemical")),
                "c_value_out_of_range": c_missing,
                "v_value_out_of_range": v_invalid,
                "polymer_name": bool(poly_fail_reason or poly_clean in (None, "N/A", "Invalid chemical")),
                "temperature_missing": temp_missing,
                "D_out_of_range": bounds_failed.get("D_out_of_range", False)
            }

            clean_entry = entry.copy()
            clean_entry["polymer_name_original"] = polymer_raw
            clean_entry["polymer_name"] = poly_clean
            clean_entry["solvent_original"] = solvent_raw
            clean_entry["solvent"] = solv_clean
            clean_entry["source_paper"] = paper_name
            clean_entry["table_name"] = table_name
            if c_parsed is not None:
                clean_entry["c_value"] = c_parsed
            if v_parsed is not None:
                clean_entry["v_value"] = v_parsed
            if temp_parsed is not None:
                clean_entry["temperature_k"] = temp_parsed
            clean_entry["failed_fields"] = failed_fields

            flory_results.append(clean_entry)
            paper_flory_count += 1

    return paper_flory_count


def load_and_homogenise(processors: list[PDFProcessor], cache_path: str, ai_instance):
    """
    Processes all loaded PDFProcessor instances, extracts polymer and solvent names from their interpretation
    data, homogenises them using the 4-stage pipeline, updates the cache, and aggregates the results.
    Yields progress dictionary events during execution.
    """
    cache = load_cache(cache_path)

    mh_results = []
    flory_results = []

    stats = {
        "total_processed": 0,
        "cache_hits": 0,
        "ai_match_hits": 0,
        "ai_generated": 0,
        "failed": 0
    }

    total_papers = len(processors)

    papers_summary = []

    try:
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

            start_mh_len = len(mh_results)
            start_flory_len = len(flory_results)

            try:
                process_mark_houwink_entries(
                    proc, paper_name, cache, ai_instance, stats, mh_results
                )
            except BaseException as e:
                if isinstance(e, (KeyboardInterrupt, SystemExit)):
                    raise e

            try:
                process_flory_entries(
                    proc, paper_name, cache, ai_instance, stats, flory_results
                )
            except BaseException as e:
                if isinstance(e, (KeyboardInterrupt, SystemExit)):
                    raise e

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

            paper_flory_added = flory_results[start_flory_len:]
            paper_mh_added = mh_results[start_mh_len:]
            paper_flory_count = len(paper_flory_added)
            paper_mh_count = len(paper_mh_added)
            paper_failed_count = sum(
                1 for e in (paper_flory_added + paper_mh_added)
                if isinstance(e.get("failed_fields"), dict) and any(e["failed_fields"].values())
            )

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
    finally:
        save_cache(cache_path, cache)

    results = {
        "mark_houwink_entries": mh_results,
        "flory_entries": flory_results,
        "stats": stats,
        "papers_summary": papers_summary
    }
    yield {
        "status": "complete",
        "results": results
    }



def sort_and_save(
    all_processors: list[PDFProcessor],
    input_dir: str,
    results: dict | None = None,
    pdf_dir: str | None = None
) -> dict[str, int]:
    """
    Sorts papers processed by PDFProcessors into 'noData', 'unhealthy', and 'healthy' subfolders
    inside a 'sorted' directory created within input_dir.

    - noData: Papers that were not categorised such that they continued to the interpretation stage.
    - unhealthy: Papers with any interpreted table having < 70% successfully interpreted rows.
    - healthy: Papers where all interpreted tables have >= 70% successfully interpreted rows.

    Copies the original PDF file of each paper into its corresponding category folder.
    """
    import shutil

    sorted_dir = os.path.join(input_dir, "sorted")
    no_data_dir = os.path.join(sorted_dir, "noData")
    unhealthy_dir = os.path.join(sorted_dir, "unhealthy")
    healthy_dir = os.path.join(sorted_dir, "healthy")

    for d in [no_data_dir, unhealthy_dir, healthy_dir]:
        os.makedirs(d, exist_ok=True)

    counts = {
        "noData": 0,
        "unhealthy": 0,
        "healthy": 0
    }

    flory_entries = results.get("flory_entries", []) if results else []
    mh_entries = results.get("mark_houwink_entries", []) if results else []

    # Map paper_name -> table_name -> list of entries
    paper_tables_map = {}
    for entry in flory_entries + mh_entries:
        paper_name = entry.get("source_paper")
        table_name = entry.get("table_name", "table1")
        if not paper_name:
            continue
        if paper_name not in paper_tables_map:
            paper_tables_map[paper_name] = {}
        if table_name not in paper_tables_map[paper_name]:
            paper_tables_map[paper_name][table_name] = []
        paper_tables_map[paper_name][table_name].append(entry)

    for proc in all_processors:
        paper_name = proc.base_no_ext

        # Check if proc has interpretation data
        has_interp_data = (
            any(item is not None for item in proc.interpretation_flory_data_list) or
            any(item is not None for item in proc.interpretation_mh_data_list)
        )

        category = "noData"

        if has_interp_data:
            tables_data = paper_tables_map.get(paper_name, {})

            if not tables_data:
                # Fallback to inspecting raw proc interpretation data lists
                tables_data = {}
                for i, flory_data in enumerate(proc.interpretation_flory_data_list):
                    if flory_data and isinstance(flory_data, dict):
                        t_name = f"table{i + 1}"
                        entries = flory_data.get("flory_entries", [])
                        if entries:
                            if t_name not in tables_data:
                                tables_data[t_name] = []
                            for e in entries:
                                is_fail = (
                                    e.get("polymer_name") in ("Not found", "Invalid chemical", "N/A") or
                                    e.get("solvent") in ("Not found", "Invalid chemical", "N/A") or
                                    e.get("v_value") == "Not found" or
                                    e.get("c_value") == "Not found"
                                )
                                tables_data[t_name].append({"failed": is_fail})

                for i, mh_data in enumerate(proc.interpretation_mh_data_list):
                    if mh_data and isinstance(mh_data, dict):
                        t_name = f"table{i + 1}"
                        entries = mh_data.get("mh_entries", [])
                        if entries:
                            if t_name not in tables_data:
                                tables_data[t_name] = []
                            for e in entries:
                                is_fail = (
                                    e.get("polymer_name") in ("Not found", "Invalid chemical", "N/A") or
                                    e.get("solvent") in ("Not found", "Invalid chemical", "N/A") or
                                    e.get("K_value") == "Not found" or
                                    e.get("a_value") == "Not found"
                                )
                                tables_data[t_name].append({"failed": is_fail})

            if not tables_data:
                category = "unhealthy"
            else:
                is_healthy = True
                for t_name, entries in tables_data.items():
                    if not entries:
                        is_healthy = False
                        break
                    total_rows = len(entries)
                    successful_rows = 0
                    for entry in entries:
                        if "failed" in entry:
                            if not entry["failed"]:
                                successful_rows += 1
                        else:
                            ff = entry.get("failed_fields")
                            if isinstance(ff, dict):
                                if not any(ff.values()):
                                    successful_rows += 1
                            elif isinstance(ff, str) and ff == "None":
                                poly = entry.get("polymer_name")
                                solv = entry.get("solvent")
                                if poly and poly != "N/A" and solv and solv != "N/A":
                                    successful_rows += 1

                    success_rate = successful_rows / total_rows if total_rows > 0 else 0.0
                    if success_rate < INTERPRETATION_SUCCESS_THRESHOLD:
                        is_healthy = False
                        break

                category = "healthy" if is_healthy else "unhealthy"

        counts[category] += 1
        dest_dir = os.path.join(sorted_dir, category)

        # Copy PDF file to dest_dir
        src_pdf = None
        if proc.pdf_path and os.path.isfile(proc.pdf_path):
            src_pdf = proc.pdf_path
        
        if not src_pdf:
            candidates = [
                os.path.join(proc.extract_dir, proc.base_name),
                os.path.join(proc.extract_dir, f"{paper_name}.pdf")
            ]
            if pdf_dir:
                candidates.extend([
                    os.path.join(pdf_dir, f"{paper_name}.pdf"),
                    os.path.join(pdf_dir, paper_name, f"{paper_name}.pdf"),
                ])
            for cand in candidates:
                if cand and os.path.isfile(cand):
                    src_pdf = cand
                    break

        if src_pdf:
            try:
                shutil.copy2(src_pdf, os.path.join(dest_dir, f"{paper_name}.pdf"))
            except Exception:
                pass

    return counts

