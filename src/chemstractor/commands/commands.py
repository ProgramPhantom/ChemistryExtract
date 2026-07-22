import sys
import click
from chemstractor.AI import AI, AllSupportedModels, ONLINE_MODELS, OFFLINE_MODELS

# Create display mapping to append a cloud emoji to server (online) models
choices_map = {}
for m in ONLINE_MODELS:
    choices_map[f"☁️  {m}"] = m
    choices_map[m] = m
for m in OFFLINE_MODELS:
    choices_map[m] = m

CHOICES = [f"☁️  {m}" for m in ONLINE_MODELS] + OFFLINE_MODELS
CLEAN_CHOICES = ONLINE_MODELS + OFFLINE_MODELS

def prompt_for_model():
    """Prompts the user to select a model using inquirer."""
    if not sys.stdin.isatty():
        return AI.DEFAULT_MODEL
    try:
        import inquirer
        questions = [
            inquirer.List(
                'model',
                message="Select model",
                choices=CHOICES,
                default=CHOICES[0]
            )
        ]
        answers = inquirer.prompt(questions)
        if answers is None:
            click.echo("Cancelled.")
            sys.exit(0)
        return answers['model']
    except Exception as e:
        click.echo(f"Warning: Failed to prompt for model interactively ({e}). Defaulting to '{AI.DEFAULT_MODEL}'.")
        return AI.DEFAULT_MODEL

def prompt_for_corpus():
    """Resolves the corpus directory. Prompts the user interactively or defaults to 'medium' when non-interactive."""
    import os
    corpus_root = "./tests/corpus"
    if not os.path.exists(corpus_root):
        corpus_root = "tests/corpus"
        
    if os.path.exists(corpus_root) and os.path.isdir(corpus_root):
        subfolders = [
            d for d in os.listdir(corpus_root)
            if os.path.isdir(os.path.join(corpus_root, d))
        ]
        if subfolders:
            default_sub = "medium" if "medium" in subfolders else subfolders[0]
            if not sys.stdin.isatty():
                return os.path.join(corpus_root, default_sub)
            try:
                import inquirer
                questions = [
                    inquirer.List(
                        'corpus',
                        message="Select corpus",
                        choices=subfolders,
                        default=default_sub
                    )
                ]
                answers = inquirer.prompt(questions)
                if answers is None:
                    click.echo("Cancelled.")
                    sys.exit(0)
                return os.path.join(corpus_root, answers['corpus'])
            except Exception as e:
                click.echo(f"Warning: Failed to prompt for corpus interactively ({e}). Defaulting to '{default_sub}'.")
                return os.path.join(corpus_root, default_sub)
    return None

@click.group()
def cli():
    """CLI tool for extracting chemistry table data from PDFs."""
    pass

@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.argument('output_dir', required=False)
@click.option('--model', type=click.Choice(CLEAN_CHOICES), default=None, help="Model to use.")
@click.option('--direct', '-d', is_flag=True, help="Input is a process output folder rather than a PDF.")
@click.option('--interpret', '-i', is_flag=True, help="Interpret coeff tables.")
@click.option('--report', '-r', is_flag=True, help="Generate report after process completes.")
@click.option('--metadata', is_flag=True, help="Extract paper metadata.")
@click.option('--summarise', '-s', is_flag=True, help="Summarise table conditions.")
@click.option('--all', '-a', is_flag=True, help="Run all stages (metadata, summarise, interpret).")
@click.option('--flory', '-f', is_flag=True, default=False, help="Interpret Flory parameters.")
@click.option('--mark-houwink', '-m', is_flag=True, default=False, help="Interpret Mark-Houwink parameters.")
def process(pdf_path, output_dir, model, direct, interpret, report, metadata, summarise, all, flory, mark_houwink):
    """Process a single PDF file (extract, categorise, and summarise)."""
    if all:
        metadata = True
        summarise = True
        interpret = True
    if not flory and not mark_houwink:
        flory = True
        mark_houwink = False
    if output_dir is None and not direct:
        output_dir = "."
    if model is None:
        model = prompt_for_model()
    if flory or mark_houwink:
        interpret = True
    
    selected_model = choices_map[model]
    AI.get_instance().set_selected_model(selected_model)
    
    same_folder = True
    if direct:
        prompt_msg = (
            "Would you like to have the output of this command be the same as the input folder? "
            "(Pre-existing process output might be overridden)"
        )
        if sys.stdin.isatty():
            same_folder = click.confirm(prompt_msg, default=True)
        else:
            same_folder = True

    from rich.console import Console
    console = Console(file=sys.__stdout__)
    with console.status(f"[bold green]Loading AI model {selected_model} and components...", spinner="dots"):
        AI.get_instance().preload_model()
        from chemstractor.commands.process import process_command
    process_command(
        pdf_path=pdf_path,
        output_dir=output_dir,
        direct=direct,
        same_folder=same_folder,
        interpret=interpret,
        report=report,
        metadata=metadata,
        summarise=summarise,
        flory=flory,
        mark_houwink=mark_houwink
    )


@cli.command()
@click.argument('pdf_dir', required=False)
@click.argument('output_dir', required=False)
@click.option('--model', type=click.Choice(CLEAN_CHOICES), default=None, help="Model to use.")
@click.option('--direct', '-d', is_flag=True, help="Input is a directory of process output folders rather than PDFs.")
@click.option('--interpret', '-i', is_flag=True, help="Interpret coeff tables.")
@click.option('--report', '-r', is_flag=True, help="Generate report after process completes.")
@click.option('--combine', '-c', is_flag=True, help="Run combine process after processing completes.")
@click.option('--metadata', is_flag=True, help="Extract paper metadata.")
@click.option('--summarise', '-s', is_flag=True, help="Summarise table conditions.")
@click.option('--all', '-a', is_flag=True, help="Run all stages (metadata, summarise, interpret, combine).")
@click.option('--flory', '-f', is_flag=True, default=False, help="Interpret Flory parameters.")
@click.option('--mark-houwink', '-m', is_flag=True, default=False, help="Interpret Mark-Houwink parameters.")
@click.option('--fast', is_flag=True, help="Run in fast mode (skips summary/metadata, interprets Flory only, runs combine).")
@click.option('--cache-path', type=click.Path(), default=None, help="Path to the chemical cache JSON file.")
def process_all(pdf_dir, output_dir, model, direct, interpret, report, combine, metadata, summarise, all, flory, mark_houwink, fast, cache_path):
    """Process all PDF files in a directory."""
    if fast:
        metadata = False
        summarise = False
        interpret = True
        flory = True
        mark_houwink = False
        combine = True
    else:
        if all:
            metadata = True
            summarise = True
            interpret = True
            combine = True
        if not flory and not mark_houwink:
            flory = True
            mark_houwink = False

    if not direct and pdf_dir is None:
        pdf_dir = prompt_for_corpus()
    if model is None:
        model = prompt_for_model()
    if mark_houwink or flory:
        interpret = True

    selected_model = choices_map[model]
    AI.get_instance().set_selected_model(selected_model)

    from rich.console import Console
    console = Console(file=sys.__stdout__)
    with console.status(f"[bold green]Loading AI model {selected_model} and components...", spinner="dots"):
        AI.get_instance().preload_model()
        from chemstractor.commands.process_all import process_all_command
    process_all_command(
        pdf_dir=pdf_dir,
        output_parent_dir=output_dir,
        direct=direct,
        interpret=interpret,
        report=report,
        combine=combine,
        metadata=metadata,
        summarise=summarise,
        flory=flory,
        mark_houwink=mark_houwink,
        cache_path=cache_path
    )


@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--output-dir', default="./", help="Directory where the output folder appears.")
def extract(pdf_path, output_dir):
    """Extract text and tables from a PDF."""

    from rich.console import Console
    console = Console(file=sys.__stdout__)
    with console.status("[bold green]Loading AI models and components...", spinner="dots"):
        from chemstractor.commands.extract import extract_command
    extract_command(
        pdf_path=pdf_path,
        output_dir=output_dir
    )


@cli.command()
@click.argument('pdf_dir', required=False)
@click.argument('output_dir', required=False)
def extract_all(pdf_dir, output_dir):
    """Extract text and tables from all PDFs in a directory."""
    from rich.console import Console
    console = Console(file=sys.__stdout__)
    with console.status("[bold green]Loading AI models and components...", spinner="dots"):
        from chemstractor.commands.extract_all import extract_all_command
    extract_all_command(
        pdf_dir=pdf_dir,
        output_parent_dir=output_dir
    )



@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--output-dir', default="./", help="Directory where the output folder appears.")
@click.option('--model', type=click.Choice(CLEAN_CHOICES), default=None, help="Model to use.")
@click.option('--direct', '-d', is_flag=True, help="Input is a process output folder rather than a PDF.")
def categorise(pdf_path, output_dir, model, direct):
    """Categorise tables extracted from a PDF."""
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    AI.get_instance().set_selected_model(selected_model)
    
    same_folder = True
    if direct:
        prompt_msg = (
            "Would you like to have the output of this command be the same as the input folder? "
            "(Pre-existing process output might be overridden)"
        )
        if sys.stdin.isatty():
            same_folder = click.confirm(prompt_msg, default=True)
        else:
            same_folder = True

    from rich.console import Console
    console = Console(file=sys.__stdout__)
    with console.status(f"[bold green]Loading AI model {selected_model} and components...", spinner="dots"):
        AI.get_instance().preload_model()
        from chemstractor.commands.categorise import categorise_command
    categorise_command(
        pdf_path=pdf_path,
        output_dir=output_dir,
        direct=direct,
        same_folder=same_folder
    )


@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--output-dir', default="./", help="Directory where the output folder appears.")
@click.option('--model', type=click.Choice(CLEAN_CHOICES), default=None, help="Model to use.")
@click.option('--direct', '-d', is_flag=True, help="Input is a process output folder rather than a PDF.")
def summarise(pdf_path, output_dir, model, direct):
    """Summarise tables and metadata extracted from a PDF."""
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    AI.get_instance().set_selected_model(selected_model)
    
    same_folder = True
    if direct:
        prompt_msg = (
            "Would you like to have the output of this command be the same as the input folder? "
            "(Pre-existing process output might be overridden)"
        )
        if sys.stdin.isatty():
            same_folder = click.confirm(prompt_msg, default=True)
        else:
            same_folder = True

    from rich.console import Console
    console = Console(file=sys.__stdout__)
    with console.status(f"[bold green]Loading AI model {selected_model} and components...", spinner="dots"):
        AI.get_instance().preload_model()
        from chemstractor.commands.summarise import summarise_command
    summarise_command(
        pdf_path=pdf_path,
        output_dir=output_dir,
        direct=direct,
        same_folder=same_folder
    )


@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--output-dir', default="./", help="Directory where the output folder appears.")
@click.option('--model', type=click.Choice(CLEAN_CHOICES), default=None, help="Model to use.")
@click.option('--direct', '-d', is_flag=True, help="Input is a process output folder rather than a PDF.")
def metadata(pdf_path, output_dir, model, direct):
    """Extract paper metadata (title, authors, doi)."""
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    AI.get_instance().set_selected_model(selected_model)
    
    same_folder = True
    if direct:
        prompt_msg = (
            "Would you like to have the output of this command be the same as the input folder? "
            "(Pre-existing process output might be overridden)"
        )
        if sys.stdin.isatty():
            same_folder = click.confirm(prompt_msg, default=True)
        else:
            same_folder = True

    from rich.console import Console
    console = Console(file=sys.__stdout__)
    with console.status(f"[bold green]Loading AI model {selected_model} and components...", spinner="dots"):
        AI.get_instance().preload_model()
        from chemstractor.commands.metadata import metadata_command
    metadata_command(
        pdf_path=pdf_path,
        output_dir=output_dir,
        direct=direct,
        same_folder=same_folder
    )


@cli.command()
@click.argument('output_dir', type=click.Path(exists=True))
@click.argument('validation_dir', type=click.Path(exists=True))
def validate(output_dir, validation_dir):
    """Validate extracted tables against correct data."""
    from chemstractor.commands.validate import validate_command
    validate_command(
        output_dir=output_dir,
        validation_dir=validation_dir
    )


@cli.command()
@click.argument('outputs_dir', required=False)
@click.argument('validation_dir', required=False)
def validate_all(outputs_dir, validation_dir):
    """Validate all output folders in the given path against validation data."""
    import os
    
    if validation_dir is None:
        validation_dir = "./tests/validation"
        
    if outputs_dir is None:
        runs_parent = "./tests/runs"
        if not os.path.exists(runs_parent):
            runs_parent = "tests/runs"
            
        if os.path.exists(runs_parent):
            subdirs = [
                d for d in os.listdir(runs_parent)
                if os.path.isdir(os.path.join(runs_parent, d))
            ]
            if subdirs:
                subdirs.sort()
                outputs_dir = os.path.join(runs_parent, subdirs[-1])
            else:
                click.echo("Error: No run folders found in tests/runs/ to validate.", err=True)
                return
        else:
            click.echo("Error: tests/runs/ directory does not exist and no outputs path was provided.", err=True)
            return

    from chemstractor.commands.validate_all import validate_command as validate_all_command
    validate_all_command(
        outputs_dir=outputs_dir,
        validation_dir=validation_dir
    )


@cli.command()
@click.argument('process_output_dir', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--output', '-o', type=click.Path(), default=None, help="Output save location of the excel document.")
def report(process_output_dir, output):
    """Create an Excel report from a process output folder."""
    from chemstractor.commands.report import report_command
    report_command(
        process_output_dir=process_output_dir,
        output=output
    )


@cli.command()
@click.argument('process_output_dir', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--model', type=click.Choice(CLEAN_CHOICES), default=None, help="Model to use.")
def clean(process_output_dir, model):
    """Clean tables from a process output folder."""
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    AI.get_instance().set_selected_model(selected_model)

    from rich.console import Console
    console = Console(file=sys.__stdout__)
    with console.status(f"[bold green]Loading AI model {selected_model} and components...", spinner="dots"):
        AI.get_instance().preload_model()
        from chemstractor.commands.clean import clean_command
    clean_command(
        process_output_dir=process_output_dir
    )


@cli.command()
@click.argument('outputs_dir', required=False)
@click.option('--model', type=click.Choice(CLEAN_CHOICES), default=None, help="Model to use.")
def clean_all(outputs_dir, model):
    """Clean all output folders in the given path."""
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    AI.get_instance().set_selected_model(selected_model)

    from rich.console import Console
    console = Console(file=sys.__stdout__)
    with console.status(f"[bold green]Loading AI model {selected_model} and components...", spinner="dots"):
        AI.get_instance().preload_model()
        from chemstractor.commands.clean_all import clean_all_command
    clean_all_command(
        outputs_dir=outputs_dir
    )


@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--output-dir', default="./", help="Directory where the output folder appears.")
@click.option('--model', type=click.Choice(CLEAN_CHOICES), default=None, help="Model to use.")
@click.option('--direct', '-d', is_flag=True, help="Input is a process output folder rather than a PDF.")
@click.option('--flory', '-f', is_flag=True, default=False, help="Interpret Flory parameters.")
@click.option('--mark-houwink', '-m', is_flag=True, default=False, help="Interpret Mark-Houwink parameters.")
def interpret(pdf_path, output_dir, model, direct, flory, mark_houwink):
    """Interpret coeff tables extracted from a PDF or process output folder."""
    if not flory and not mark_houwink:
        flory = True
        mark_houwink = False
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    AI.get_instance().set_selected_model(selected_model)
    
    same_folder = True
    if direct:
        prompt_msg = (
            "Would you like to have the output of this command be the same as the input folder? "
            "(Pre-existing process output might be overridden)"
        )
        if sys.stdin.isatty():
            same_folder = click.confirm(prompt_msg, default=True)
        else:
            same_folder = True

    from rich.console import Console
    console = Console(file=sys.__stdout__)
    with console.status(f"[bold green]Loading AI model {selected_model} and components...", spinner="dots"):
        AI.get_instance().preload_model()
        from chemstractor.commands.interpret import interpret_command
    interpret_command(
        pdf_path=pdf_path,
        output_dir=output_dir,
        direct=direct,
        same_folder=same_folder,
        flory=flory,
        mark_houwink=mark_houwink
    )


@cli.command()
@click.argument('pdf_dir', required=False)
@click.argument('output_dir', required=False)
@click.option('--model', type=click.Choice(CLEAN_CHOICES), default=None, help="Model to use.")
@click.option('--direct', '-d', is_flag=True, help="Input is a directory of process output folders rather than PDFs.")
@click.option('--flory', '-f', is_flag=True, default=False, help="Interpret Flory parameters.")
@click.option('--mark-houwink', '-m', is_flag=True, default=False, help="Interpret Mark-Houwink parameters.")
def interpret_all(pdf_dir, output_dir, model, direct, flory, mark_houwink):
    """Interpret all tables in a directory of PDFs or process output folders."""
    if not flory and not mark_houwink:
        flory = True
        mark_houwink = False
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    AI.get_instance().set_selected_model(selected_model)

    from rich.console import Console
    console = Console(file=sys.__stdout__)
    with console.status(f"[bold green]Loading AI model {selected_model} and components...", spinner="dots"):
        AI.get_instance().preload_model()
        from chemstractor.commands.interpret_all import interpret_all_command
    interpret_all_command(
        pdf_dir=pdf_dir,
        output_parent_dir=output_dir,
        direct=direct,
        flory=flory,
        mark_houwink=mark_houwink
    )


@cli.command()
@click.argument('input_dir', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--output', '-o', type=click.Path(), default=None, help="Output save location of the combined Excel/JSON document.")
@click.option('--model', type=click.Choice(CLEAN_CHOICES), default=None, help="Model to use.")
@click.option('--cache-path', type=click.Path(), default=None, help="Path to the chemical cache JSON file.")
@click.option('--pdf-dir', type=click.Path(), default=None, help="Path to directory containing source PDF files.")
def combine(input_dir, output, model, cache_path, pdf_dir):
    """Combine and homogenise interpreted chemistry data from multiple papers."""
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    AI.get_instance().set_selected_model(selected_model)

    from rich.console import Console
    console = Console(file=sys.__stdout__)
    with console.status(f"[bold green]Loading AI model {selected_model} and components...", spinner="dots"):
        AI.get_instance().preload_model()
        from chemstractor.commands.combine import combine_command
    combine_command(
        input_dir=input_dir,
        output_path=output,
        cache_path=cache_path,
        pdf_dir=pdf_dir
    )





