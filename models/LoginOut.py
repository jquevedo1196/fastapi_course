from pydantic import BaseModel, Field


class LoginOut(BaseModel):
    username: str = Field(
        ...,
        max_length=20,
        example="jquevedo1196"
    )
    message: str = Field(
        default="Login Succesfully!!!"
    )
