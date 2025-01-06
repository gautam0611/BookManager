from datetime import datetime
from pydantic import BaseModel


class BookBase(BaseModel):
    company_name: str
    title: str
    location: str
    salary: int
    yoe: str
    workLoc: str
    dateApplied: datetime
    jobURL: str


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True


class BookCreate(BookBase):
    pass
