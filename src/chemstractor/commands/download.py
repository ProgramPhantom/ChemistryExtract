import os
import sys
import time
from rich.console import Console
from rich.tree import Tree
from rich.live import Live
from rich.spinner import Spinner
from rich.rule import Rule

from chemstractor.lib.downloader import download_papers_from_openalex, sanitize_filename


def download_command(
    query: str,
    name: str = None,
    output_dir: str = None,
    limit: int = 50,
    open_access_only: bool = True,
    year: int = None,
    types: str = None,
    chemistry_only: bool = False,
    title_only: bool = False,
    email: str = None
):
    """CLI execution layer for downloading papers via OpenAlex."""
    console = Console(file=sys.__stdout__)
    
    # Resolve target corpus output directory
    if output_dir is None:
        if not name:
            # Generate default corpus name from search query
            name = sanitize_filename(query).lower()
        output_dir = os.path.join("tests", "corpus", name)
        
    os.makedirs(output_dir, exist_ok=True)
    
    parsed_types = [t.strip() for t in types.split(",") if t.strip()] if types else None

    console.print(Rule(title=f"[bold green]DOWNLOAD CORPUS: {os.path.basename(output_dir)}[/bold green]", style="green"))
    console.print(f"[bold cyan]Query:[/bold cyan] {query}")
    if year:
        console.print(f"[bold cyan]Publication Year:[/bold cyan] {year} or later")
    if parsed_types:
        console.print(f"[bold cyan]Work Types:[/bold cyan] {', '.join(parsed_types)}")
    if chemistry_only:
        console.print(f"[bold cyan]Field Filter:[/bold cyan] Chemistry Field (topics.field.id:16)")
    if title_only:
        console.print(f"[bold cyan]Search Scope:[/bold cyan] Strict Title Only")
    if email:
        console.print(f"[bold cyan]Polite API Pool Email:[/bold cyan] {email}")
    console.print(f"[bold cyan]Target Corpus Folder:[/bold cyan] {os.path.abspath(output_dir)}")
    console.print(f"[bold cyan]Required PDFs:[/bold cyan] {limit} (Open Access Only: {open_access_only})")
    console.print()
    
    tree = Tree(f"[bold cyan]📥 Searching OpenAlex...[/bold cyan]")
    
    downloaded_papers = []
    failed_papers = []
    
    with Live(tree, console=console, auto_refresh=True, refresh_per_second=10):
        current_node = None
        for event in download_papers_from_openalex(
            query=query,
            output_dir=output_dir,
            limit=limit,
            open_access_only=open_access_only,
            year=year,
            work_types=parsed_types,
            chemistry_only=chemistry_only,
            title_only=title_only,
            email=email
        ):




            status = event.get("status")
            
            if status == "searching":
                tree.label = Spinner("dots", text=f"[bold cyan]{event['message']}[/bold cyan]")
                
            elif status == "found":
                total_res = event.get("total_results", 0)
                target = event.get("target_count", limit)
                tree.label = f"[green]✓[/green] Found [bold yellow]{total_res}[/bold yellow] matching works on OpenAlex (fetching until [bold cyan]{target}[/bold cyan] PDFs downloaded)"
                
            elif status == "paper_start":
                idx = event.get("index")
                target = event.get("target", limit)
                title = event.get("title")
                current_node = tree.add(Spinner("dots", text=f"[dim]({idx}/{target})[/dim] Downloading: [bold]{title[:60]}...[/bold]"))

                
            elif status == "paper_success":
                filename = event.get("filename")
                size_kb = event.get("size_bytes", 0) / 1024
                title = event.get("title")
                if current_node:
                    current_node.label = f"[green]✓[/green] [bold]{title[:65]}[/bold] [dim]({size_kb:.1f} KB -> {filename})[/dim]"
                downloaded_papers.append(event)
                
            elif status == "paper_failed":
                title = event.get("title")
                reason = event.get("reason", "Unknown error")
                if current_node:
                    current_node.label = f"[red]✗[/red] [dim]{title[:65]} (Failed: {reason})[/dim]"
                failed_papers.append(event)
                
            elif status == "error":
                tree.add(f"[bold red]Error: {event.get('message')}[/bold red]")
                
            elif status == "complete":
                elapsed = event.get("elapsed_time", 0.0)
                count = event.get("downloaded_count", 0)
                manifest = event.get("manifest_path")
                
                summary_node = tree.add(f"[bold green]Complete![/bold green] Downloaded [bold yellow]{count}[/bold yellow] PDFs in {elapsed:.2f}s")
                if manifest:
                    summary_node.add(f"Manifest saved to: [dim]{manifest}[/dim]")
                    
    console.print()
    if downloaded_papers:
        console.print(f"[bold green]Successfully saved {len(downloaded_papers)} papers to:[/bold green] [yellow]{os.path.abspath(output_dir)}[/yellow]")
        console.print(f"[dim]Run 'chemstractor process-all {output_dir}' to extract chemistry data from this new corpus.[/dim]")
    else:
        console.print("[bold yellow]No papers were successfully downloaded.[/bold yellow]")
    console.print()
