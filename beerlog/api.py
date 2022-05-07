from typing import List

from fastapi import FastAPI, Response, status

from beerlog.core import get_beers
from beerlog.database import get_session
from beerlog.models import Beer
from beerlog.serializers import Beerin, Beerout

api = FastAPI(title="Beerlog")


@api.get("/beers", response_model=List[Beerout])
def list_beers():
    beers = get_beers()
    return beers


@api.post("/beers", response_model=Beerout)
async def add_beer(beerin: Beerin, response: Response):
    beer = Beer(**beerin.dict())
    print(beer)
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)
    
    response.status_code = status.HTTP_201_CREATED
    return beer
