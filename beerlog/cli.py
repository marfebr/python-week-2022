from typer import Typer, Option
from typing import Optional
from beerlog.core import add_beer_database, get_beers


main = Typer(help="Beer Manager Application")


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = Option(...),
    image: int = Option(...),
    cost: int = Option(...),
):
    "Adiciona uma nova cerveja"
    if add_beer_database(name, style, flavor, image, cost):
        print("\N{beer mug} add to database")
    else:
        print("\N{weary face}")


@main.command("list")
def list_beer(style: Optional[str] = None):
    """Lista cervejas de um stilo"""

    lista = get_beers()
    print(lista)
