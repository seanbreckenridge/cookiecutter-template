import sys
import click

# target for python3 -m {{ cookiecutter.module_name }} and console_script using click
def main_wrapper() -> int:
    click.echo("Hello from {{ cookiecutter.module_name }}!")
    return 0

@click.command()
#@click.argument("SOME_ARG", required=True, type=int)
#@click.option("--some-path", required=False, type=click.Path(), help="Describe input path")
def main():
    main_wrapper()

if __name__ == "__main__":
    sys.exit(main_wrapper())

