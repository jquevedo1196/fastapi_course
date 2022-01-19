from pydantic import BaseModel
from typing import Optional


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married_color: Optional[bool] = None
