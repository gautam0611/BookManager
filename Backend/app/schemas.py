from datetime import datetime
from pydantic import BaseModel


class JobBase(BaseModel):
    company_name: str
    title: str
    location: str
    salary: int
    yoe: str
    workLoc: str
    dateApplied: datetime
    jobURL: str


class Job(JobBase):
    id: int

    class Config:
        from_attributes = True


class JobCreate(JobBase):
    pass
