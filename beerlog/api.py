from fastapi import FastAPI
from beerlog.core import get_beers
from beerlog.serializers import Beerout, Beerin
from typing import List
from beerlog.database import get_session
from beerlog.models import Beer

api = FastAPI(title="Beerlog")

@api.get("/beers", response_model=List[Beerout])
def list_beers():
    beers = get_beers()
    return beers

@api.post('/beers', response_model=Beerout)
def add_beer(beerin: Beerin):
    beer = Beer(**beerin.dict())
    with get_session as session:
        session.add(beer)
        session.commit()
        session.refresh()
        return beer



