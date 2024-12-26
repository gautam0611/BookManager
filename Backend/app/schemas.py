from datetime import datetime
from pydantic import BaseModel


class JobBase(BaseModel):
    company_name: str
    title: str
    location: str
    salary: str
    yoe: str
    workLoc: str
    dateApplied: str
    jobURL: str


class Job(JobBase):
    id: int

    class Config:
        orm_mode = True
        # from_attributes = True


class JobCreate(JobBase):
    pass
