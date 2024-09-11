import pkg_resources
import rich_click as click
from rich.console import Console
from rich.table import Table

from mouracx import core

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()
@click.version_option(pkg_resources.get_distribution("mouracx").version)
def main():
    """Moura Fluxo de Caixa

    This CLI application controls
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads file csv and shows at screen.

    ## Features
    - Validates data
    - Parses the file
    - Loads to database
    """
    table = Table(title="Moura Fluxo de Caixa")
    headers = ["data", "trasacao", "valor", "tipo", "created"]

    for header in headers:
        table.add_column(header, style="magenta")

    result = core.load(filepath)
    for item in result:
        table.add_row(*[str(value) for value in item.values()])

    console = Console()
    console.print(table)
