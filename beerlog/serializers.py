from pydantic import BaseModel, validator
from datetime import datetime 

class Beerout(BaseModel):
    id: int
    name: str
    flavor: int
    cost: int
    style: str
    image: int
    rate: int = 0
    date: datetime

class Beerin(BaseModel):
    id: int
    name: str
    flavor: int
    cost: int
    style: str
    image: int
    rate: int = 0
    date: datetime

    @validator("image", "flavor", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise HTTPException(
                detail=f"{field.name} must be between 1 and 10", 
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return v


