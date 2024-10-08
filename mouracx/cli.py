from datetime import datetime
from decimal import Decimal

import pkg_resources
import rich_click as click
from rich.console import Console
from rich.table import Table

from mouracx import core
from mouracx.settings import DATEFMT, DATEFMT_DATE

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
    headers = ["DATE", "ACCOUNT", "DESCRIPTION", "AMOUNT", "DEBIT-CREDIT"]

    for header in headers:
        table.add_column(header, style="magenta")

    result = core.load(filepath)
    for item in result:
        print(item)
        # table.add_row(*[str(value) for value in item.values()])
        table.add_row(
            str(item["transaction_date"].strftime(DATEFMT_DATE)),
            str(item["account_id"]),
            str(item["description"]),
            str(item["amount"]),
            str(item["debit_credit"]),
        )

    console = Console()
    console.print(table)


@main.command()
def show():
    """Shows all Movements at screen.

    ## Features
    - Show all movements in database
    """

    table = Table(title="Moura Fluxo de Caixa")
    headers = ["DATA", "TRANSACAO", "VALOR", "TIPO", "CURRENCY"]
    for header in headers:
        table.add_column(header, style="green")

    movements = core.list_movements()

    for item in movements:
        table.add_row(
            str(item["data"]),
            str(item["transacao"]),
            str(item["valor"]),
            str(item["tipo"]),
            str(item["currency"]),
        )
        # table.add_row(*[str(value) for value in item.values()])

    console = Console()
    console.print(table)


@main.command()
@click.argument("name", required=True)
@click.option("--type", required=False)
@click.option("--currency", required=False)
def add_account(name, type, currency):
    """Register account bank to transaction.

    ## Features
    - Add account
    """
    table = Table(title="Moura Fluxo de Caixa")
    headers = ["NOME", "TIPO", "CURRENCY", "CREATED_AT"]

    for header in headers:
        table.add_column(header, style="green")

    result = core.register_account(name, type, currency="BRL")
    created_at = datetime.now()
    table.add_row(
        str(result["account_name"]),
        str(result["account_type"]),
        str(result["currency"]),
        created_at.strftime(DATEFMT),
    )

    console = Console()
    console.print(table)


@main.command()
@click.argument("name", required=True)
def add_category(name):
    """Register category to transaction.

    ## Features
    - Add category
    """
    table = Table(title="Moura Fluxo de Caixa")
    headers = ["NOME", "CREATED_AT"]

    for header in headers:
        table.add_column(header, style="green")
    created_at = datetime.now()
    result = core.add_category(name)
    table.add_row(str(result["category_name"]), created_at.strftime(DATEFMT))

    console = Console()
    console.print(table)


@main.command()
@click.argument("account_name", required=True)
@click.option("--category_name", required=False)
@click.option("--description", required=False)
@click.option("--value_transaction", required=False)
@click.option("--debit_credit", required=False)
@click.option("--balance", required=False)
def add_transaction(
    account_name,
    category_name,
    description,
    value_transaction,
    debit_credit,
    balance,
):
    """Register bank transaction.

    ## Features
    - Add banck transaction
    """
    table = Table(title="Moura Fluxo de Caixa")
    headers = [
        "ACCOUNT",
        "DATE",
        "DESCRIPTION",
        "AMMOUNT",
        "DEBIT_CREDIT",
        "BALANCE",
    ]

    for header in headers:
        table.add_column(header, style="green")
    created_at = datetime.now()
    ammount = Decimal(value_transaction)
    result = core.add_transaction(
        account_name,
        created_at,
        category_name,
        description,
        ammount,
        debit_credit,
        balance,
    )
    print(result)
    table.add_row(
        str(result["account_id"]),
        str(result["transaction_date"].strftime(DATEFMT)),
        created_at.strftime(DATEFMT),
        str(result["amount"]),
        str(result["debit_credit"]),
        str(result["balance"]),
        created_at.strftime(DATEFMT),
    )

    console = Console()
    console.print(table)
