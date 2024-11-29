from sqlalchemy import Column, Integer, String, Date
from database import Base


class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, unique=True, index=True)
    title = Column(String, unique=True, index=True)
    location = Column(String, unique=True, index=True)
    salary = Column(Integer, unique=True, index=True)
    yoe = Column(String, unique=True, index=True)
    work_loc = Column(String, unique=True, index=True)
    date_applied = Column(Date, unique=True, index=True)