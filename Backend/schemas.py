import datetime
from pydantic import BaseModel


class Job(BaseModel):
    id: int
    company_name: str
    title: str
    location: str
    salary: int
    yoe: str
    workLoc: str
    dateApplied: datetime
    jobURL: str
