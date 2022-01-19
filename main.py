from fastapi import FastAPI, Body

from models.Person import Person

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

#Request and responsebody
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return f"Hola {person.first_name} {person.last_name}"