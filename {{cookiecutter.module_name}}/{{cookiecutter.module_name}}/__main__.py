import click


@click.group()
def main():
    pass


@main.command()
# @click.argument("SOME_ARG", required=True, type=int)
# @click.option("--some-path", required=False, type=click.Path(), help="Describe input path")
def cmd():
    pass


if __name__ == "__main__":
    main(prog_name="{{ cookiecutter.module_name }}")
