import typer


main = typer.Typer(help="Beer Manager Application")


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
    ):
    "Adiciona uma nova cerveja"
    print(name, style)


@main.command("list")
def list_beer(style: str):
    "Lista cervejas de um stilo"
    print(style)