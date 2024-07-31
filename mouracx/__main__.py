import argparse


def load(filepath):
    try:
        with open(filepath) as file:
            for line in file:
                print(line)
    except FileNotFoundError as e:
        print(f"File not found {e}")


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
    globals()[args.subcommand](args.filepath)

    #print("Executing mouracx from entry point")


if __name__ == "__main__":
    main()
