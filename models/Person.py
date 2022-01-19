from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

from enums.HairColors import HairColor


class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        le=150
    )
    hair_color: HairColor = Field(None)
    is_married_color: Optional[bool] = Field(None)
