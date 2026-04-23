from beanie import Document
from pydantic import BaseModel

class User(Document):
    email: str
    username: str
    password: str

    class Settings:
        name = "users"

class UserSignUp(BaseModel):
    email: str
    username: str
    password: str

class UserSignIn(BaseModel):
    username: str
    password: str