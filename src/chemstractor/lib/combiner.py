import os
import json
import difflib
import typing
from pydantic import BaseModel
from chemstractor.lib.processor import PDFProcessor

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

def generate_new_clean_name(dirty_name: str, ai_instance) -> str:
    """Uses the AI to generate a new canonical name for a chemical string, or 'N/A' if it is not a chemical."""
    class ChemicalGeneration(BaseModel):
        clean_name: str

    prompt = (
        f"You are an expert chemist. You will be given a raw, dirty, or abbreviated chemical name extracted from scientific literature.\n"
        f"Your task is to convert it into a standard, clean, and canonical name. E.g., expand acronyms where clear (like 'PMMA' to 'poly(methyl methacrylate)'), "
        f"or correct typos/formatting issues (like 'T0luene' to 'toluene' or 'THF-d8' to 'THF-d8' or 'CDCl3' to 'chloroform-d').\n\n"
        f"Raw chemical name: '{dirty_name}'\n\n"
        f"Rules:\n"
        f"1. Create a clean, nicely formatted chemical name using standard nomenclature.\n"
        f"2. If the input is not a chemical name or compound (e.g. it is noise, a page number, a citation, or completely ambiguous text that does not represent a chemical), you MUST respond exactly with 'N/A'.\n"
        f"3. Do not include extra text, explanations, or quotes."
    )

    system_instruction = (
        "Generate a clean, standard chemical name. Use 'N/A' if the text does not represent a chemical compound."
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
        return "N/A"

def homogenise_and_track(raw_name: str, cache: dict, ai_instance, stats: dict) -> tuple[str, str, str]:
    """
    Homogenises a raw name and updates stats.
    Returns:
    (clean_name, source, fail_reason)
    source is one of "cache", "ai_match", "ai_generate", or "fail".
    """
    try:
        if not raw_name or not raw_name.strip():
            stats["total_processed"] += 1
            stats["failed"] += 1
            return "N/A", "fail", "Empty input string"

        raw_name_clean = raw_name.strip()
        stats["total_processed"] += 1

        # 1. Check cache (including fuzzy matches)
        cached_val = find_fuzzy_match(raw_name_clean, cache)
        if cached_val:
            stats["cache_hits"] += 1
            return cached_val, "cache", ""

        # 2. Select from existing clean names in the cache
        clean_names = sorted(list(set(cache.values())))
        clean_names = [n for n in clean_names if n and n.upper() != "N/A"]

        match_val = "not found"
        if clean_names:
            match_val = select_from_existing_names(raw_name_clean, clean_names, ai_instance)

        if match_val != "not found" and match_val in clean_names:
            cache[raw_name_clean] = match_val
            stats["ai_match_hits"] += 1
            return match_val, "ai_match", ""

        # 3. Generate new clean name
        generated_val = generate_new_clean_name(raw_name_clean, ai_instance)
        if generated_val == "N/A" or not generated_val:
            stats["failed"] += 1
            return raw_name_clean, "fail", "AI marked as N/A"

        # Save the generated name to the cache
        cache[raw_name_clean] = generated_val
        stats["ai_generated"] += 1
        return generated_val, "ai_generate", ""
    except BaseException as e:
        if isinstance(e, (KeyboardInterrupt, SystemExit)):
            raise e
        stats["failed"] += 1
        return raw_name, "fail", f"Unexpected error during name homogenisation: {str(e)}"


def gather_and_homogenise(processors: list[PDFProcessor], cache_path: str, ai_instance) -> dict:
    """
    Processes all loaded PDFProcessor instances, extracts polymer and solvent names from their interpretation
    data, homogenises them using the 4-stage pipeline, updates the cache, and aggregates the results.
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

    for proc in processors:
        paper_name = proc.base_no_ext

        # Check if interpretation results are present
        if not proc.interpretation_flory_data_list and not proc.interpretation_mh_data_list:
            continue

        try:
            num_tables = max(len(proc.interpretation_flory_data_list), len(proc.interpretation_mh_data_list))
            for i in range(num_tables):
                table_name = f"table{i + 1}"

                # Process Mark-Houwink entries
                mh_data = proc.interpretation_mh_data_list[i] if i < len(proc.interpretation_mh_data_list) else None
                if mh_data:
                    mh_entries = mh_data.get("mh_entries", [])
                    for entry in mh_entries:
                        polymer_raw = entry.get("polymer_name", "")
                        solvent_raw = entry.get("solvent", "")

                        poly_clean, poly_source, poly_fail_reason = homogenise_and_track(
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

                        solv_clean, solv_source, solv_fail_reason = homogenise_and_track(
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

                # Process Flory entries
                flory_data = proc.interpretation_flory_data_list[i] if i < len(proc.interpretation_flory_data_list) else None
                if flory_data:
                    flory_entries = flory_data.get("flory_entries", [])
                    for entry in flory_entries:
                        polymer_raw = entry.get("polymer_name", "")
                        solvent_raw = entry.get("solvent", "")

                        poly_clean, poly_source, poly_fail_reason = homogenise_and_track(
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

                        solv_clean, solv_source, solv_fail_reason = homogenise_and_track(
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
        except BaseException as e:
            if isinstance(e, (KeyboardInterrupt, SystemExit)):
                raise e
            failures.append({
                "source_paper": paper_name,
                "table": "N/A",
                "field": "Paper processing",
                "value": "N/A",
                "reason": f"Unexpected error during homogenisation: {str(e)}"
            })


    save_cache(cache_path, cache)

    return {
        "mark_houwink_entries": mh_results,
        "flory_entries": flory_results,
        "failures": failures,
        "stats": stats
    }
