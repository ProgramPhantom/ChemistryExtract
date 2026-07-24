import os
import json
import time
import re
import urllib.request
import urllib.parse
from datetime import datetime
from typing import Generator, Dict, Any, List, Optional


def sanitize_filename(name: str) -> str:
    """Sanitizes a string to be safe for filenames across operating systems."""
    cleaned = re.sub(r'[\\/*?:"<>|]', '_', name)
    cleaned = re.sub(r'\s+', '_', cleaned)
    return cleaned.strip('._')[:150]


def extract_pdf_url(work: Dict[str, Any]) -> Optional[str]:
    """Extracts a direct PDF URL from an OpenAlex work object if available."""
    # 1. Check best open access location
    best_oa = work.get("best_oa_location") or {}
    if isinstance(best_oa, dict) and best_oa.get("pdf_url"):
        return best_oa["pdf_url"]
    
    # 2. Check primary location
    primary_loc = work.get("primary_location") or {}
    if isinstance(primary_loc, dict) and primary_loc.get("pdf_url"):
        return primary_loc["pdf_url"]
    
    # 3. Check all locations
    locations = work.get("locations") or []
    for loc in locations:
        if isinstance(loc, dict) and loc.get("pdf_url"):
            return loc["pdf_url"]
            
    return None


def download_papers_from_openalex(
    query: str,
    output_dir: str,
    limit: int = 50,
    open_access_only: bool = True
) -> Generator[Dict[str, Any], None, None]:
    """Backend generator that queries OpenAlex API and downloads open-access paper PDFs.
    
    Yields status dictionary events for UI feedback.
    """
    start_time = time.time()
    os.makedirs(output_dir, exist_ok=True)
    
    yield {
        "status": "searching",
        "message": f"Searching OpenAlex for: '{query}'..."
    }
    
    # Construct OpenAlex API search URL
    base_url = "https://api.openalex.org/works"
    params = {
        "search": query,
        "per-page": min(limit, 100)
    }
    
    filter_conditions = ["has_fulltext:true"]
    if open_access_only:
        filter_conditions.append("is_oa:true")
    params["filter"] = ",".join(filter_conditions)
    
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    
    headers = {
        "User-Agent": "Chemstractor/0.1.0 (https://github.com/ProgramPhantom/ChemistryExtract)"
    }
    
    works: List[Dict[str, Any]] = []
    page = 1
    total_found = 0
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            if response.status != 200:
                yield {"status": "error", "message": f"OpenAlex API returned HTTP status {response.status}"}
                return
            payload = json.loads(response.read().decode('utf-8'))
            total_found = payload.get("meta", {}).get("count", 0)
            works.extend(payload.get("results", []))
    except Exception as e:
        yield {"status": "error", "message": f"Failed to query OpenAlex API: {str(e)}"}
        return

    # Handle pagination if limit > 100
    while len(works) < limit and len(works) < total_found:
        page += 1
        params["page"] = page
        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                if response.status == 200:
                    payload = json.loads(response.read().decode('utf-8'))
                    page_results = payload.get("results", [])
                    if not page_results:
                        break
                    works.extend(page_results)
                else:
                    break
        except Exception:
            break

    works = works[:limit]
    
    # Filter works with downloadable PDF URLs
    downloadable_works = []
    for work in works:
        pdf_url = extract_pdf_url(work)
        if pdf_url:
            downloadable_works.append((work, pdf_url))
            
    yield {
        "status": "found",
        "total_results": total_found,
        "downloadable_count": len(downloadable_works),
        "target_count": len(works)
    }
    
    if not downloadable_works:
        yield {
            "status": "complete",
            "downloaded_count": 0,
            "failed_count": 0,
            "output_dir": output_dir,
            "manifest_path": None,
            "elapsed_time": time.time() - start_time
        }
        return

    # Download PDFs
    manifest_papers = []
    downloaded_count = 0
    failed_count = 0
    
    for idx, (work, pdf_url) in enumerate(downloadable_works, start=1):
        work_id = work.get("id", "").split("/")[-1] or f"work_{idx}"
        title = work.get("title") or "Untitled Paper"
        doi = work.get("doi") or ""
        year = work.get("publication_year")
        authors = [
            auth.get("author", {}).get("display_name")
            for auth in work.get("authorships", [])
            if isinstance(auth, dict) and auth.get("author", {}).get("display_name")
        ]
        
        # Determine filename
        if doi:
            clean_doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
            filename_base = sanitize_filename(clean_doi)
        else:
            filename_base = sanitize_filename(f"{work_id}_{title[:40]}")
            
        filename = f"{filename_base}.pdf"
        target_filepath = os.path.join(output_dir, filename)
        
        yield {
            "status": "paper_start",
            "index": idx,
            "total": len(downloadable_works),
            "title": title,
            "doi": doi,
            "url": pdf_url
        }
        
        # Download PDF with stream validation
        pdf_downloaded = False
        error_reason = ""
        
        try:
            pdf_req = urllib.request.Request(pdf_url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            })
            with urllib.request.urlopen(pdf_req, timeout=35) as resp:
                content = resp.read()
                
                # Validation: Verify PDF signature (%PDF-) and minimum file size (10 KB)
                if not content.startswith(b"%PDF"):
                    error_reason = "URL returned non-PDF content (likely paywall page or HTML)"
                elif len(content) < 10240:
                    error_reason = f"File too small ({len(content)} bytes), likely corrupted or error response"
                else:
                    with open(target_filepath, "wb") as f:
                        f.write(content)
                    pdf_downloaded = True
                    file_size = len(content)
        except Exception as e:
            error_reason = f"HTTP/Network error: {str(e)}"
            
        if pdf_downloaded:
            downloaded_count += 1
            paper_info = {
                "filename": filename,
                "filepath": os.path.abspath(target_filepath),
                "openalex_id": work.get("id"),
                "doi": doi,
                "title": title,
                "publication_year": year,
                "authors": authors,
                "pdf_url": pdf_url,
                "downloaded_at": datetime.now().isoformat()
            }
            manifest_papers.append(paper_info)
            yield {
                "status": "paper_success",
                "index": idx,
                "total": len(downloadable_works),
                "title": title,
                "filename": filename,
                "size_bytes": file_size
            }
        else:
            failed_count += 1
            yield {
                "status": "paper_failed",
                "index": idx,
                "total": len(downloadable_works),
                "title": title,
                "reason": error_reason
            }
            
        # Polite delay between requests
        time.sleep(0.5)

    # Save download manifest
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
