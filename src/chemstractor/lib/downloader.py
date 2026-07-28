import os
import json
import time
import re
import ssl
import urllib.request
import urllib.parse
from datetime import datetime
from typing import Generator, Dict, Any, List, Optional
from difflib import SequenceMatcher
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def create_ssl_context() -> ssl.SSLContext:
    """Creates a relaxed SSL context to prevent SSL verification failures on university/repo mirrors."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

SSL_CONTEXT = create_ssl_context()

BROWSER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/pdf,application/xhtml+xml,text/html;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Upgrade-Insecure-Requests": "1"
}

STOPWORDS = {"a", "an", "the", "and", "or", "of", "for", "with", "in", "on", "at", "by", "to", "from"}


def sanitize_filename(name: str) -> str:
    """Sanitizes a string to be safe for filenames across operating systems."""
    cleaned = re.sub(r'[\\/*?:"<>|]', '_', name)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip('._ ')
    return cleaned[:150]


def is_si_file(filename: str) -> bool:
    """Checks if a filename indicates a Supplementary/Supporting Information file."""
    name, _ = os.path.splitext(filename)
    name = name.lower()
    
    si_patterns = [
        r'[\s_\-\(\[\{]si[\s_\-\)\]\}]*$',
        r'[\s_\-\(\[\{]supp[\s_\-\)\]\}]*$',
        r'[\s_\-\(\[\{]supplementary[\s_\-\w]*$',
        r'[\s_\-\(\[\{]supporting[\s_\-\w]*$',
        r'[\s_\-\(\[\{]si[\s_\-\(\[\{]',
    ]
    for pat in si_patterns:
        if re.search(pat, name):
            return True
    return False


def normalize_filename_for_matching(filename: str) -> tuple[bool, str]:
    """Extracts SI status and normalizes filename for fuzzy comparison.
    Returns (is_si, normalized_name).
    """
    name, _ = os.path.splitext(filename)
    name = name.lower().strip()
    
    is_si = is_si_file(filename)
    
    # Strip SI suffixes/keywords
    si_strip_patterns = [
        r'[\s_\-\(\[\{]si[\s_\-\)\]\}]*$',
        r'[\s_\-\(\[\{]supp[\s_\-\)\]\}]*$',
        r'[\s_\-\(\[\{]supplementary[\s_\-\w]*$',
        r'[\s_\-\(\[\{]supporting[\s_\-\w]*$',
    ]
    for pat in si_strip_patterns:
        name = re.sub(pat, '', name).strip()
        
    # Strip leading 4-digit publication year if present e.g. "2020 - " or "2020_"
    name = re.sub(r'^(19|20)\d{2}\s*[\-_\s]\s*', '', name).strip()
    
    # Normalize common Roman numerals to arabic numbers in standalone tokens
    roman_map = {
        r'\bviii\b': '8',
        r'\bvii\b': '7',
        r'\bvi\b': '6',
        r'\biv\b': '4',
        r'\bv\b': '5',
        r'\biii\b': '3',
        r'\bii\b': '2',
        r'\bi\b': '1',
    }
    for r_pat, digit in roman_map.items():
        name = re.sub(r_pat, digit, name)

    # Clean non-alphanumeric characters (keep alphanumeric, replace others with space)
    cleaned = re.sub(r'[^a-z0-9]', ' ', name)
    # Collapse multiple spaces
    normalized = re.sub(r'\s+', ' ', cleaned).strip()
    
    return is_si, normalized


def is_fuzzy_duplicate(filename1: str, filename2: str, threshold: float = 0.90) -> bool:
    """Compares two filenames to determine if they are fuzzy duplicates.
    Ensures SI files are NOT matched against main paper files.
    """
    is_si1, norm1 = normalize_filename_for_matching(filename1)
    is_si2, norm2 = normalize_filename_for_matching(filename2)
    
    # Key Rule: SI file and Main paper file are NEVER duplicates of each other!
    if is_si1 != is_si2:
        return False
        
    if not norm1 or not norm2:
        return norm1 == norm2
        
    if norm1 == norm2:
        return True
        
    # Character sequence ratio
    char_ratio = SequenceMatcher(None, norm1, norm2).ratio()
    if char_ratio < threshold:
        return False
        
    # Significant word / token comparison to prevent false positives (e.g. organic vs inorganic)
    words1 = [w for w in norm1.split() if w not in STOPWORDS]
    words2 = [w for w in norm2.split() if w not in STOPWORDS]
    
    set1 = set(words1)
    set2 = set(words2)
    
    if not set1 or not set2:
        return char_ratio >= threshold
        
    # Jaccard similarity of non-stopword tokens
    jaccard = len(set1 & set2) / len(set1 | set2)
    
    return jaccard >= 0.75


def find_fuzzy_duplicate_in_dir(filename: str, output_dir: str, threshold: float = 0.90) -> Optional[str]:
    """Scans output_dir for any file that is a fuzzy duplicate of filename.
    Returns the matching existing filename if found, otherwise None.
    SI files and main paper files are never matched against each other.
    """
    if not os.path.exists(output_dir):
        return None
        
    for existing in os.listdir(output_dir):
        filepath = os.path.join(output_dir, existing)
        if os.path.isfile(filepath) and not existing.endswith(".json"):
            if is_fuzzy_duplicate(filename, existing, threshold=threshold):
                return existing
    return None


def extract_all_pdf_urls(
    work: Dict[str, Any],
    openalex_key: Optional[str] = None,
    email: Optional[str] = None
) -> List[str]:
    """Extracts a prioritized list of potential PDF and landing page URLs for a work.
    Prioritizes OpenAlex's direct cached PDF content service (content.openalex.org).
    """
    candidates = []
    
    # 0. OpenAlex Direct Cached PDF Content Service (content.openalex.org)
    work_id = work.get("id")
    if work_id:
        short_id = str(work_id).split("/")[-1]
        content_url = f"https://content.openalex.org/works/{short_id}.pdf"
        if openalex_key:
            content_url += f"?api_key={openalex_key}"
        elif email:
            content_url += f"?mailto={email.strip()}"
        candidates.append(content_url)
    
    # 1. Best OA location PDF
    best_oa = work.get("best_oa_location") or {}
    if isinstance(best_oa, dict) and best_oa.get("pdf_url"):
        url = best_oa["pdf_url"]
        if url not in candidates:
            candidates.append(url)
        
    # 2. Primary location PDF
    primary_loc = work.get("primary_location") or {}
    if isinstance(primary_loc, dict) and primary_loc.get("pdf_url"):
        url = primary_loc["pdf_url"]
        if url not in candidates:
            candidates.append(url)
            
    # 3. All other location PDFs
    for loc in work.get("locations") or []:
        if isinstance(loc, dict) and loc.get("pdf_url"):
            url = loc["pdf_url"]
            if url not in candidates:
                candidates.append(url)

    # 4. Landing page URLs (can be scraped for citation_pdf_url)
    if isinstance(best_oa, dict) and best_oa.get("landing_page_url"):
        l_url = best_oa["landing_page_url"]
        if l_url not in candidates:
            candidates.append(l_url)
            
    if isinstance(primary_loc, dict) and primary_loc.get("landing_page_url"):
        l_url = primary_loc["landing_page_url"]
        if l_url not in candidates:
            candidates.append(l_url)
            
    return candidates


def fetch_pdf_binary(url: str, depth: int = 0) -> tuple[Optional[bytes], str]:
    """Fetches PDF content using relaxed SSL, browser headers, and HTML meta tag scraping."""
    if depth > 2:
        return None, "Exceeded maximum redirect/extraction depth"
        
    session = requests.Session()
    session.headers.update(BROWSER_HEADERS)
    
    try:
        resp = session.get(url, timeout=30, allow_redirects=True, verify=False)
        if resp.status_code == 200:
            content = resp.content
            
            # Binary PDF check
            if content.startswith(b"%PDF"):
                if len(content) < 10240:
                    return None, f"File too small ({len(content)} bytes)"
                return content, "success"
                
            # If HTML landing page returned, attempt to extract meta citation_pdf_url
            try:
                html_str = content.decode('utf-8', errors='ignore')
                match = re.search(r'<meta\s+name=["\']citation_pdf_url["\']\s+content=["\']([^"\']+)["\']', html_str, re.IGNORECASE)
                if not match:
                    match = re.search(r'<meta\s+content=["\']([^"\']+)["\']\s+name=["\']citation_pdf_url["\']', html_str, re.IGNORECASE)
                    
                if match:
                    pdf_link = match.group(1).replace("&amp;", "&")
                    if pdf_link.startswith("/"):
                        parsed_base = urllib.parse.urlparse(resp.url)
                        pdf_link = f"{parsed_base.scheme}://{parsed_base.netloc}{pdf_link}"
                    return fetch_pdf_binary(pdf_link, depth + 1)
            except Exception:
                pass
                
            return None, "URL returned non-PDF content (paywall page or HTML)"
        else:
            return None, f"HTTP Error {resp.status_code}: {resp.reason}"
    except Exception as e:
        return None, f"Network error: {str(e)}"


def download_papers_from_openalex(
    query: str,
    output_dir: str,
    limit: int = 50,
    open_access_only: bool = True,
    year: Optional[int] = None,
    work_types: Optional[List[str]] = None,
    chemistry_only: bool = False,
    title_only: bool = False,
    semantic: bool = False,
    email: Optional[str] = None
) -> Generator[Dict[str, Any], None, None]:
    """Backend generator that queries OpenAlex API and downloads open-access paper PDFs.
    
    Continues fetching candidates from OpenAlex until 'limit' papers have been successfully downloaded.
    Yields status dictionary events for UI feedback.
    """
    start_time = time.time()
    os.makedirs(output_dir, exist_ok=True)
    
    msg = f"Searching OpenAlex for: '{query}'"
    if semantic:
        msg = f"Searching OpenAlex [Semantic Search] for: '{query}'"
    elif title_only:
        msg += " [Title search only]"
    if year:
        msg += f" (published in {year} or later)"
    if chemistry_only and not semantic:
        msg += " [Chemistry domain only]"
    
    yield {
        "status": "searching",
        "message": f"{msg}..."
    }
    
    base_url = "https://api.openalex.org/works"
    per_page = 100
    cursor = "*"
    
    filter_conditions = ["has_fulltext:true"]
    if open_access_only:
        filter_conditions.append("is_oa:true")
    if year is not None:
        filter_conditions.append(f"from_publication_date:{year}-01-01")
    if work_types:
        types_str = "|".join([t.strip().lower() for t in work_types if t.strip()])
        if types_str:
            filter_conditions.append(f"type:{types_str}")
    if chemistry_only and not semantic:
        filter_conditions.append("primary_topic.field.id:16")
    if title_only and not semantic:
        filter_conditions.append(f"title.search:{query}")
        
    polite_email = email.strip() if email else "henryvarley@outlook.com"
    headers = {
        "User-Agent": f"Chemstractor/0.1.0 (mailto:{polite_email})"
    }
    
    # Load OpenAlex API Key from .env if present
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except Exception:
        pass
        
    openalex_key = os.getenv("OPENALEX_KEY")
    if openalex_key:
        headers["api_key"] = openalex_key
    
    params = {
        "per-page": min(per_page, 50),
        "filter": ",".join(filter_conditions),
        "mailto": polite_email
    }
    if not semantic:
        params["cursor"] = cursor

    if openalex_key:
        params["api_key"] = openalex_key
        
    if semantic:
        # Semantic search expects natural language text; strip search query syntax quotes
        clean_semantic_query = re.sub(r'[\"\']', '', query).strip()
        params["search.semantic"] = clean_semantic_query
    elif not title_only:
        params["search"] = query

        
    def fetch_openalex_json(request_url: str) -> tuple[Optional[dict], str]:
        """Fetches OpenAlex JSON payload with automatic retry backoff on HTTP 429 / rate limits."""
        last_error_msg = "Unknown error"
        for attempt in range(5):
            try:
                req = urllib.request.Request(request_url, headers=headers)
                with urllib.request.urlopen(req, timeout=30, context=SSL_CONTEXT) as response:
                    if response.status == 200:
                        return json.loads(response.read().decode('utf-8')), "success"
                    elif response.status == 429:
                        last_error_msg = f"HTTP 429 (Rate Limit on attempt {attempt + 1})"
                        time.sleep(4 * (attempt + 1))
                    else:
                        return None, f"HTTP status {response.status}"
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    last_error_msg = f"HTTP 429 (Rate Limit on attempt {attempt + 1})"
                    time.sleep(4 * (attempt + 1))
                else:
                    try:
                        err_body = e.read().decode('utf-8', errors='ignore')
                        err_data = json.loads(err_body)
                        err_detail = err_data.get("message") or err_data.get("error") or err_body
                        return None, f"HTTP Error {e.code}: {err_detail}"
                    except Exception:
                        return None, f"HTTP Error {e.code}: {e.reason}"
            except Exception as e:
                last_error_msg = str(e)
                time.sleep(2)
        return None, f"OpenAlex API query failed: {last_error_msg} (exceeded 5 retries)"


    # Fetch initial page to get total matching works count
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    payload, err_msg = fetch_openalex_json(url)
    if not payload:
        yield {"status": "error", "message": f"Failed to query OpenAlex API: {err_msg}"}
        return
        
    total_found = payload.get("meta", {}).get("count", 0)
    page_works = payload.get("results", [])
    cursor = payload.get("meta", {}).get("next_cursor")

    yield {
        "status": "found",
        "total_results": total_found,
        "target_count": limit
    }

    manifest_papers = []
    downloaded_count = 0
    failed_count = 0
    skipped_count = 0
    no_oa_count = 0
    evaluated_count = 0
    seen_openalex_ids = set()

    while downloaded_count < limit:
        # If current page of works is exhausted, fetch next page using cursor (if not semantic)
        if not page_works:
            if not cursor or semantic:
                # No more pages available from OpenAlex (semantic search returns max 50 results)
                break
                
            params["cursor"] = cursor
            url = f"{base_url}?{urllib.parse.urlencode(params)}"
            
            payload, err_msg = fetch_openalex_json(url)
            if not payload or not payload.get("results"):
                break
                
            page_works = payload.get("results", [])
            cursor = payload.get("meta", {}).get("next_cursor")


            
        work = page_works.pop(0)
        work_id = work.get("id")
        if work_id in seen_openalex_ids:
            continue
        seen_openalex_ids.add(work_id)
        
        pub_year = work.get("publication_year")
        if year is not None and pub_year and pub_year < year:
            continue
            
        evaluated_count += 1
        title = work.get("title") or "Untitled Paper"
        doi = work.get("doi") or ""

        pdf_urls = extract_all_pdf_urls(work, openalex_key=openalex_key, email=polite_email)
        if not pdf_urls:
            no_oa_count += 1
            yield {
                "status": "paper_no_oa",
                "index": downloaded_count + 1,
                "evaluated": evaluated_count,
                "target": limit,
                "title": title,
                "reason": "No direct Open Access PDF URL available"
            }
            continue

        year = work.get("publication_year")
        authors = [
            auth.get("author", {}).get("display_name")
            for auth in work.get("authorships", [])
            if isinstance(auth, dict) and auth.get("author", {}).get("display_name")
        ]
        
        # Determine filename formatted as "{year} - {paper_name}.pdf"
        year_str = str(year) if year else "Unknown"
        clean_title = sanitize_filename(title)
        filename_base = f"{year_str} - {clean_title}"
        filename = f"{filename_base}.pdf"

        # Pre-save check: skip saving if a fuzzy duplicate already exists in output_dir
        duplicate_match = find_fuzzy_duplicate_in_dir(filename, output_dir)
        if duplicate_match:
            skipped_count += 1
            yield {
                "status": "paper_skipped",
                "index": downloaded_count + 1,
                "target": limit,
                "title": title,
                "filename": filename,
                "matched_filename": duplicate_match,
                "reason": f"Similar file already exists: {duplicate_match}"
            }
            continue

        target_filepath = os.path.join(output_dir, filename)
        
        # Prevent filename collisions
        counter = 1
        while os.path.exists(target_filepath):
            filename = f"{filename_base}_{counter}.pdf"
            target_filepath = os.path.join(output_dir, filename)
            counter += 1

        yield {
            "status": "paper_start",
            "index": downloaded_count + 1,
            "target": limit,
            "title": title,
            "doi": doi,
            "url": pdf_urls[0]
        }
        
        pdf_downloaded = False
        error_reason = ""
        file_size = 0
        used_url = pdf_urls[0]
        
        # Attempt download across all candidate URLs until one succeeds
        for candidate_url in pdf_urls:
            content, reason = fetch_pdf_binary(candidate_url)
            if content:
                with open(target_filepath, "wb") as f:
                    f.write(content)
                pdf_downloaded = True
                file_size = len(content)
                used_url = candidate_url
                break
            else:
                error_reason = reason

        if pdf_downloaded:
            downloaded_count += 1
            paper_info = {
                "filename": filename,
                "filepath": os.path.abspath(target_filepath),
                "openalex_id": work_id,
                "doi": doi,
                "title": title,
                "publication_year": year,
                "authors": authors,
                "pdf_url": used_url,
                "downloaded_at": datetime.now().isoformat()
            }
            manifest_papers.append(paper_info)
            yield {
                "status": "paper_success",
                "index": downloaded_count,
                "target": limit,
                "title": title,
                "filename": filename,
                "size_bytes": file_size
            }
        else:
            failed_count += 1
            yield {
                "status": "paper_failed",
                "index": downloaded_count + 1,
                "target": limit,
                "title": title,
                "reason": error_reason
            }
            
        # Polite delay between requests
        time.sleep(0.3)


    manifest_path = os.path.join(output_dir, "download_manifest.json")
    manifest_data = {
        "query": query,
        "downloaded_at": datetime.now().isoformat(),
        "total_evaluated": evaluated_count,
        "total_downloaded": downloaded_count,
        "total_failed": failed_count,
        "total_skipped": skipped_count,
        "total_no_oa": no_oa_count,
        "papers": manifest_papers
    }
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)
        
    yield {
        "status": "complete",
        "evaluated_count": evaluated_count,
        "downloaded_count": downloaded_count,
        "failed_count": failed_count,
        "skipped_count": skipped_count,
        "no_oa_count": no_oa_count,
        "output_dir": output_dir,
        "manifest_path": manifest_path,
        "elapsed_time": time.time() - start_time
    }



if __name__ == "__main__":
    from chemstractor.commands.commands import cli
    cli()

