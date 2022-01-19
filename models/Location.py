from pydantic import BaseModel


class Location(BaseModel):
    city: str
    state: str
    country: str
