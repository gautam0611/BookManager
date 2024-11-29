from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Backend import schemas
import database

from . import crud

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
def get_jobs(job_id: int, db: Session = Depends(get_db)):
    db_job = crud.get_job(db, job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job


@app.get("/all_jobs/{company_name}", response_model=schemas.Job)
def get_all_jobs(company_name: str, db: Session = Depends(get_db)):
    db_jobs = crud.get_all_jobs(db, company_name=company_name)
    if not db_jobs:
        raise HTTPException(status_code=404, detail="Jobs not found for company")
    return db_jobs


@app.post("/job", response_model=schemas.Job)
def add_job(job: schemas.Job, db: Session = Depends(get_db)):
    return crud.create_job(db, job)


@app.put("/job/{job_id}", response_model=schemas.Job)
def update_job(job_id: int, new_job: schemas.Job):
    pass


@app.delete("/job/{job_id}", response_model=schemas.Job)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    return crud.delete_job(db, job_id)
