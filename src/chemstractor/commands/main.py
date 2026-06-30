import sys
import os
import click
import inquirer
from chemstractor.models import AllSupportedModels, ONLINE_MODELS, OFFLINE_MODELS

# Create display mapping to append a cloud emoji to server (online) models
choices_map = {}
for m in ONLINE_MODELS:
    choices_map[f"☁️  {m}"] = m
for m in OFFLINE_MODELS:
    choices_map[m] = m

CHOICES = list(choices_map.keys())

@click.group()
def cli():
    """CLI tool for extracting chemistry table data from PDFs."""
    pass

@cli.command()
def test_all():
    """Run extraction tests on PDFs in the materials folder."""
    questions = [
        inquirer.Confirm(
            'categorise_tables',
            message="Categorise table?",
            default=True
        ),
        inquirer.Confirm(
            'summarise_tables',
            message="Create table summary",
            default=True
        ),
        inquirer.List(
            'model',
            message="Select model",
            choices=CHOICES,
            default=CHOICES[0]
        ),
    ]
    
    answers = inquirer.prompt(questions)
    if answers is None:
        click.echo("Cancelled.")
        return
        
    selected_display = answers['model']
    selected_model = choices_map[selected_display]
    
    click.echo(f"Running tests with model='{selected_model}', categorise_tables={answers['categorise_tables']}, summarise_tables={answers['summarise_tables']}...")
    
    from chemstractor.commands.test_all import test_all_command
    test_all_command(
        categorise_tables=answers['categorise_tables'],
        summarise_tables=answers['summarise_tables'],
        model=selected_model
    )

@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--output-dir', default="./", help="Directory where the output folder appears.")
@click.option('--model', type=click.Choice(CHOICES), default=CHOICES[0], help="Model to use.")
def extract(pdf_path, output_dir, model):
    """Extract text and tables from a PDF."""
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
@click.option('--model', type=click.Choice(CHOICES), default=CHOICES[0], help="Model to use.")
def categorise(pdf_path, output_dir, model):
    """Categorise tables extracted from a PDF."""
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
@click.option('--model', type=click.Choice(CHOICES), default=CHOICES[0], help="Model to use.")
def summarise(pdf_path, output_dir, model):
    """Summarise tables and metadata extracted from a PDF."""
    selected_model = choices_map[model]
    from chemstractor.commands.summarise import summarise_command
    summarise_command(
        pdf_path=pdf_path,
        output_dir=output_dir,
        model=selected_model
    )

if __name__ == '__main__':
    cli()
