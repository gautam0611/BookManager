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
