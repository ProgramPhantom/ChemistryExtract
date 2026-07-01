import os  
os.environ['ConEmuANSI'] = '1' # Stops blessed terminal probe. Might cause problems later!

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')
if hasattr(sys.__stdout__, 'reconfigure'):
    sys.__stdout__.reconfigure(encoding='utf-8')
if hasattr(sys.__stderr__, 'reconfigure'):
    sys.__stderr__.reconfigure(encoding='utf-8')
import click
from chemstractor.models import AllSupportedModels, ONLINE_MODELS, OFFLINE_MODELS

# Create display mapping to append a cloud emoji to server (online) models
choices_map = {}
for m in ONLINE_MODELS:
    choices_map[f"☁️  {m}"] = m
for m in OFFLINE_MODELS:
    choices_map[m] = m

CHOICES = list(choices_map.keys())

def prompt_for_model():
    """Prompts the user to select a model using inquirer."""
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

@click.group()
def cli():
    """CLI tool for extracting chemistry table data from PDFs."""
    pass

@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.argument('output_dir', required=False)
@click.option('--model', type=click.Choice(CHOICES), default=None, help="Model to use.")
def process(pdf_path, output_dir, model):
    """Process a single PDF file (extract, categorise, and summarise)."""
    if output_dir is None:
        output_dir = "."
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    from chemstractor.commands.process import process_command
    process_command(
        pdf_path=pdf_path,
        output_dir=output_dir,
        model=selected_model
    )

@cli.command()
@click.argument('pdf_dir', required=False)
@click.argument('output_dir', required=False)
@click.option('--model', type=click.Choice(CHOICES), default=None, help="Model to use.")
def process_all(pdf_dir, output_dir, model):
    """Process all PDF files in a directory."""
    if pdf_dir is None:
        pdf_dir = "./tests/material"
    if output_dir is None:
        output_dir = "./tests/runs"
        
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    from chemstractor.commands.process_all import process_all_command
    process_all_command(
        pdf_dir=pdf_dir,
        output_parent_dir=output_dir,
        model=selected_model
    )

@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--output-dir', default="./", help="Directory where the output folder appears.")
@click.option('--model', type=click.Choice(CHOICES), default=None, help="Model to use.")
def extract(pdf_path, output_dir, model):
    """Extract text and tables from a PDF."""
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    from chemstractor.commands.extract import extract_command
    extract_command(
        pdf_path=pdf_path,
        output_dir=output_dir,
        model=selected_model
    )

@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--output-dir', default="./", help="Directory where the output folder appears.")
@click.option('--model', type=click.Choice(CHOICES), default=None, help="Model to use.")
def categorise(pdf_path, output_dir, model):
    """Categorise tables extracted from a PDF."""
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    from chemstractor.commands.categorise import categorise_command
    categorise_command(
        pdf_path=pdf_path,
        output_dir=output_dir,
        model=selected_model
    )

@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--output-dir', default="./", help="Directory where the output folder appears.")
@click.option('--model', type=click.Choice(CHOICES), default=None, help="Model to use.")
def summarise(pdf_path, output_dir, model):
    """Summarise tables and metadata extracted from a PDF."""
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    from chemstractor.commands.summarise import summarise_command
    summarise_command(
        pdf_path=pdf_path,
        output_dir=output_dir,
        model=selected_model
    )

@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--output-dir', default="./", help="Directory where the output folder appears.")
@click.option('--model', type=click.Choice(CHOICES), default=None, help="Model to use.")
def metadata(pdf_path, output_dir, model):
    """Extract paper metadata (title, authors, doi)."""
    if model is None:
        model = prompt_for_model()
    selected_model = choices_map[model]
    from chemstractor.commands.metadata import metadata_command
    metadata_command(
        pdf_path=pdf_path,
        output_dir=output_dir,
        model=selected_model
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

if __name__ == '__main__':
    cli()
