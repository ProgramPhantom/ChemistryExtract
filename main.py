from typing import Literal, get_args, Union
import click
import inquirer

OnlineModels = Literal["gemini-2.5-flash", "gemini-3.5-flash"]
OfflineModels = Literal["llama3.1"]
AllSupportedModels = Union[OnlineModels, OfflineModels]

ONLINE_MODELS = list(get_args(OnlineModels))
OFFLINE_MODELS = list(get_args(OfflineModels))

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
    
    from tests import run_tests
    run_tests(
        categorise_tables=answers['categorise_tables'],
        summarise_tables=answers['summarise_tables'],
        model=selected_model
    )

if __name__ == '__main__':
    cli()
