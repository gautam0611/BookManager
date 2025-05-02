from sqlalchemy import Column, Integer, String
from .database import Base, engine


class Book(Base):
    __tablename__ = "Book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), unique=True, index=True)
    number_of_pages = Column(Integer, unique=True, index=True)
    author = Column(String(255), unique=True, index=True)
    genre = Column(String(255), unique=True, index=True)
    published_date = Column(String(255), unique=True, index=True)
    date_added = Column(String(255), unique=True, index=True)


Base.metadata.create_all(bind=engine)
