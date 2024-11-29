from fastapi import FastAPI
from sqlalchemy.orm import Session
from Backend import schemas
import database

app = FastAPI()


# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
CRUD Operations down below
"""


@app.get("/job/{job_id}", response_model=schemas.Job)
def get_jobs(
    job_id: int,
):
    pass


@app.get("/all_jobs/{company_name}", response_model=schemas.Job)
def get_all_jobs():
    pass


@app.post("/job", response_model=schemas.Job)
def add_job():
    pass


@app.put("/job/{job_id}", response_model=schemas.Job)
def update_job(job_id: int):
    pass


@app.delete("/job/{job_id}", response_model=schemas.Job)
def delete_job(job_id: int):
    pass
