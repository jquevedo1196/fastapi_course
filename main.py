from fastapi import FastAPI, Body, Query, Path
from typing import Optional

from models.Person import Person
from models.Location import Location

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# Request and responsebody
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return f"Hola {person.first_name} {person.last_name}"


@app.get("/person/detail")
def show_person(
        name: Optional[str] = Query(
            None,
            min_length=1,
            max_length=50,
            title="Person Name",
            description="This is the person name. It's between 1 and 50 chars"
        ),
        age: Optional[str] = Query(
            ...,
            min_length=1,
            max_length=3,
            title="Person Age",
            description="Person age. It's required"
        )
):
    return {name: age}


@app.get("/person/detail/{person_id}")
def show_person(
        person_id: int = Path(
            ...,
            gt=0,
            lt=100000,
            title="Person identifier",
            description="This is a required element",
        )
):
    return {person_id: "It exist!"}


@app.put("/person/{person_id}")
def show_person(
        person_id: int = Path(
            ...,
            gt=0,
            title="Person identifier",
            description="This is a required element",
        ),
        person: Person = Body(...),
        location: Location = Body(...),
):
    results = person.dict()
    results.update(location.dict())
    person.dict()
    return {person_id: results}
