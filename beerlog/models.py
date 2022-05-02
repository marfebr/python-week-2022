from typing import Optional
from sqlmodel import SQLModel, Field, select
from pydantic import validator
from statistics import mean
from datetime import datetime


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    flavor: int
    cost: int
    style: str
    image: int
    rate: int = 0
    date: datetime  = Field(default_factory=datetime.now)

    @validator("flavor", "cost", "image")
    def validate_rating(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} o valor deve ser entre 1 e 10")
        return v

    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values['cost'], values['image']])
        return int(rate)


# brewdog = Beer(name='Brewdog', style='NEIPA', flavor=6, image=8, cost=8)
# print(select(Beer).where(Beer.name == 'teste'))
