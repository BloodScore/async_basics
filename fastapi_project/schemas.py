from fastapi import Query
from pydantic import BaseModel, conlist

from enums import BuildTypes, Races


class Build(BaseModel):
    name: str
    description: str = Query(..., min_length=15)
    race: Races
    type: BuildTypes
    opponents: conlist(Races, min_items=1)

    class Config:
        orm_mode = True


class BuildToUpdate(Build):
    id: int

    class Config:
        orm_mode = True


class BuildForResponse(Build):
    opponents: str

    class Config:
        orm_mode = True
