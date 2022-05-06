from typer import Typer, Option
from typing import Optional
from beerlog.core import add_beer_database, get_beers
from rich.table import Table
from rich.console import Console

main = Typer(help="Beer Manager Application")

console = Console()


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
    table = Table(title="Beerlog :beer_mug")
    headers = ['id', 'name', 'style', 'rate', 'date']
    for header in headers:
        table.add_column(header=header, style='magenta')

    for beer in lista:
        values = [str(getattr(beer, header)) for header in headers]
        print(values)
        table.add_row(*values)
        
    console.print(table)
