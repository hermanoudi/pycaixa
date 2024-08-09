import argparse
from mouracx.core import load # noqa


def main():
    parser = argparse.ArgumentParser(
        description="Moura Fluxo de Caixa CLI",
        epilog="Enjoy and use with cautions",
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "add"),
        default="help"
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="File path to load",
        default=None
    )

    args = parser.parse_args()
    print(*globals()[args.subcommand](args.filepath))

    #print("Executing mouracx from entry point")
