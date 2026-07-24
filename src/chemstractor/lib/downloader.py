import os
import json
import time
import re
import ssl
import urllib.request
import urllib.parse
from datetime import datetime
from typing import Generator, Dict, Any, List, Optional


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


def sanitize_filename(name: str) -> str:
    """Sanitizes a string to be safe for filenames across operating systems."""
    cleaned = re.sub(r'[\\/*?:"<>|]', '_', name)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip('._ ')
    return cleaned[:150]


def extract_all_pdf_urls(work: Dict[str, Any]) -> List[str]:
    """Extracts a prioritized list of potential PDF and landing page URLs for a work."""
    candidates = []
    
    # 1. Best OA location PDF
    best_oa = work.get("best_oa_location") or {}
    if isinstance(best_oa, dict) and best_oa.get("pdf_url"):
        candidates.append(best_oa["pdf_url"])
        
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
        
    try:
        req = urllib.request.Request(url, headers=BROWSER_HEADERS)
        with urllib.request.urlopen(req, timeout=30, context=SSL_CONTEXT) as resp:
            content = resp.read()
            
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
                        parsed_base = urllib.parse.urlparse(url)
                        pdf_link = f"{parsed_base.scheme}://{parsed_base.netloc}{pdf_link}"
                    return fetch_pdf_binary(pdf_link, depth + 1)
            except Exception:
                pass
                
            return None, "URL returned non-PDF content (paywall page or HTML)"
    except urllib.error.HTTPError as e:
        return None, f"HTTP Error {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return None, f"Network error: {e.reason}"
    except Exception as e:
        return None, f"HTTP/Network error: {str(e)}"


def download_papers_from_openalex(
    query: str,
    output_dir: str,
    limit: int = 50,
    open_access_only: bool = True,
    year: Optional[int] = None,
    work_types: Optional[List[str]] = None,
    chemistry_only: bool = False,
    title_only: bool = False,
    email: Optional[str] = None
) -> Generator[Dict[str, Any], None, None]:
    """Backend generator that queries OpenAlex API and downloads open-access paper PDFs.
    
    Continues fetching candidates from OpenAlex until 'limit' papers have been successfully downloaded.
    Yields status dictionary events for UI feedback.
    """
    start_time = time.time()
    os.makedirs(output_dir, exist_ok=True)
    
    msg = f"Searching OpenAlex for: '{query}'"
    if year:
        msg += f" (published in {year} or later)"
    if chemistry_only:
        msg += " [Chemistry domain only]"
    if title_only:
        msg += " [Title search only]"
    
    yield {
        "status": "searching",
        "message": f"{msg}..."
    }
    
    base_url = "https://api.openalex.org/works"
    per_page = 50
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
    if chemistry_only:
        filter_conditions.append("primary_topic.field.id:16")
    if title_only:
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
        "per-page": per_page,
        "cursor": cursor,
        "filter": ",".join(filter_conditions),
        "mailto": polite_email
    }
    if openalex_key:
        params["api_key"] = openalex_key
    if not title_only:
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
    seen_openalex_ids = set()

    while downloaded_count < limit:
        # If current page of works is exhausted, fetch next page using cursor
        if not page_works:
            if not cursor:
                # No more pages available from OpenAlex
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
            
        pdf_urls = extract_all_pdf_urls(work)
        if not pdf_urls:
            continue
            
        title = work.get("title") or "Untitled Paper"
        doi = work.get("doi") or ""

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
        "total_downloaded": downloaded_count,
        "total_failed": failed_count,
        "papers": manifest_papers
    }
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)
        
    yield {
        "status": "complete",
        "downloaded_count": downloaded_count,
        "failed_count": failed_count,
        "output_dir": output_dir,
        "manifest_path": manifest_path,
        "elapsed_time": time.time() - start_time
    }



if __name__ == "__main__":
    from chemstractor.commands.commands import cli
    cli()

