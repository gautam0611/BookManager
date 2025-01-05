from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import schemas
from . import database

from . import crud

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update to match your frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


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


@app.get("/all_jobs_by_company/{company_name}", response_model=schemas.Job)
def get_all_jobs_by_company(company_name: str, db: Session = Depends(get_db)):
    db_jobs = crud.get_all_jobs_by_company(db, company_name=company_name)
    if not db_jobs:
        raise HTTPException(status_code=404, detail="Jobs not found for company")
    return db_jobs


@app.get("/all_jobs", response_model=List[schemas.Job])
def get_all_jobs(db: Session = Depends(get_db)):
    db_jobs = crud.get_all_jobs(db)
    if not db_jobs:
        raise HTTPException(status_code=404, detail="No jobs found")
    return db_jobs


@app.post("/job", response_model=schemas.Job)
def add_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = schemas.JobCreate(
        company_name=job.company_name,
        title=job.title,
        location=job.location,
        salary=job.salary,
        yoe=job.yoe,
        workLoc=job.workLoc,
        dateApplied=job.dateApplied,
        jobURL=job.jobURL,
    )
    return crud.create_job(db, db_job)


@app.put("/job/{job_id}", response_model=schemas.Job)
def update_job(job_id: int, new_job: schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = crud.get_job(db, job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    return crud.update_job(db, job_id, new_job)


@app.delete("/job/{job_id}", response_model=dict)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    rows_deleted = crud.delete_job(db, job_id)
    if rows_deleted == 0:
        raise HTTPException(status_code=404, detail="Job not found")
    return rows_deleted
