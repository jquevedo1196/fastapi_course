from pydantic import BaseModel, Field, EmailStr
from typing import Optional

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
    is_married: Optional[bool] = Field(None)
    email: EmailStr = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Jesus",
                "last_name": "Quevedo",
                "age": 25,
                "hair_color": "black",
                "is_married": False,
                "email": "algo@algo.com"
            }
        }
