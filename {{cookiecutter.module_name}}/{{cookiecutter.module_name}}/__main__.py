import sys

import click


@click.group()
@click.option("--debug", is_flag=True, default=False, help="Display debug messages")
def main(debug):
    pass


@main.command()
# @click.argument("SOME_ARG", required=True, type=int)
# @click.option("--some-path", required=False, type=click.Path(), help="Describe input path")
def command_name():
    pass


if __name__ == "__main__":
    main()
