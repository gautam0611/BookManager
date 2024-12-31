from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models

from .schemas import Job


def create_job(db: Session, job: Job):
    db_job = models.Jobs(
        company_name=job.company_name,
        title=job.title,
        location=job.location,
        salary=job.salary,
        yoe=job.yoe,
        workLoc=job.workLoc,  # Ensure this matches the model
        dateApplied=job.dateApplied,
        jobURL=job.jobURL,
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job


def update_job(db: Session, job_id: int, updated_job: dict):
    db_job = db.query(models.Jobs).filter(models.Jobs.id == job_id).first()

    if not db_job:
        raise HTTPException(status_code=404, detail="Job does not exist")

    for key, val in updated_job.items():
        if hasattr(db_job, key):
            setattr(db_job, key, val)

    db.add()
    db.commit()
    db.refresh(db_job)

    return db_job


def get_job(db: Session, job_id: int):
    return db.query(models.Jobs).filter(models.Jobs.id == job_id).first()


def get_all_jobs(db: Session):
    return db.query(models.Jobs).all()


def get_all_jobs_by_company(db: Session, company_name: str):
    return db.query(models.Jobs).filter(models.Jobs.company_name == company_name)


def delete_job(db: Session, job_id: int):
    rows_deleted = (
        db.query(models.Jobs)
        .filter(models.Jobs.id == job_id)
        .delete(synchronize_session=False)
    )
    db.commit()  # Ensure changes are committed
    return {"job_id": job_id, "rows_deleted": rows_deleted}
