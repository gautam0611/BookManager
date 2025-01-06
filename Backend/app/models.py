from sqlalchemy import Column, Integer, String, Date
from .database import Base


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, unique=True, index=True)
    title = Column(String, unique=True, index=True)
    location = Column(String, unique=True, index=True)
    salary = Column(Integer, unique=True, index=True)
    yoe = Column(String, unique=True, index=True)
    workLoc = Column(String, unique=True, index=True)
    dateApplied = Column(Date, unique=True, index=True)
    jobURL = Column(String, unique=True, index=True)
