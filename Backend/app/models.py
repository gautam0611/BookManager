from sqlalchemy import Column, Integer, String
from .database import Base


class Book(Base):
    __tablename__ = "Book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    number_of_pages = Column(Integer, unique=True, index=True)
    author = Column(String, unique=True, index=True)
    genre = Column(String, unique=True, index=True)
    published_date = Column(String, unique=True, index=True)
    date_added = Column(String, unique=True, index=True)
