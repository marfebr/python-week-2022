from datetime import datetime

from pydantic import BaseModel, validator


class Beerout(BaseModel):
    id: int
    name: str
    flavor: int
    style: str
    image: int
    cost: int
    rate: int = 0
    date: datetime


class Beerin(BaseModel):
    name: str
    flavor: int
    style: str
    image: int
    cost: int


    @validator("image", "flavor", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise HTTPException(
                detail=f"{field.name} must be between 1 and 10",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v
