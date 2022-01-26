from typing import Optional

from fastapi import FastAPI, Body, Query, Path, status, Form, Header, Cookie, UploadFile, File, HTTPException

from pydantic import EmailStr

from models.LoginOut import LoginOut
from models.Person import Person
from models.Location import Location
#asdComentario
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


@app.get("/person/detail", deprecated=True)
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


persons = [1, 2, 3, 4, 5]

@app.get("/person/detail/{person_id}", tags=["Persons"])
def show_person(
        person_id: int = Path(
            ...,
            gt=0,
            lt=100000,
            title="Person identifier",
            description="This is a required element"
        )
):
    if person_id not in persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No existe el usuario"
        )
    return {person_id: "It exist!"}


@app.put("/person/{person_id}", status_code=status.HTTP_200_OK, tags=["Persons"])
def show_person(
        person_id: int = Path(
            ...,
            gt=0,
            title="Person identifier",
            description="This is a required element",
        ),
        person: Person = Body(...),
        location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    person.dict()
    return person


@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK
)
def login(username: str = Form(...), password: str = Form(...)):
    return LoginOut(username=username)


@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK
)
def contact(
        first_name: str = Form(
            ...,
            min_length=1,
            max_length=20
        ),
        last_name: str = Form(
            ...,
            min_length=1,
            max_length=20
        ),
        email: EmailStr = Form(...),
        message: str = Form(
            ...,
            min_length=20
        ),
        user_agent: Optional[str] = Header(default=None),
        ads: Optional[str] = Cookie(default=None)
):
    return user_agent


@app.post(
    path="/post-image",
    status_code=status.HTTP_200_OK,
    summary="Upload image to user profile"
)
def post_image(
        image: UploadFile = File(...)
):
    """
    Upload image file

    This path operation upload an image for the user
    :param image: The image to save in DB
    :return: Some information of image uploaded
    """
    return {
        "FileName": image.filename,
        "Format": image.content_type,
        "Size(Kb)": round(len(image.file.read()) / 1024, ndigits=2)
    }
