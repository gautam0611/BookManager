from datetime import datetime
from typing import Optional
from pydantic import BaseModel


#########
# Book Schemas
#########
class BookBase(BaseModel):
    title: str
    number_of_pages: int
    author: str
    genre: str
    published_date: str
    date_added: str


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True


class BookCreate(BookBase):
    pass


#########
# Auth Schemas
#########
class CreateUser(BaseModel):
    username: str
    password: str


class UserLogin(CreateUser):
    pass


# Tokens
class DataToken(BaseModel):
    id: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str
