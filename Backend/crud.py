from sqlalchemy.orm import Session
from . import models

from schemas import Job


def create_job(db: Session, job: Job):
    db_job = models.Jobs(
        id=job.id,
        company_name=job.company_name,
        title=job.title,
        location=job.location,
        salary=job.salary,
        yoe=job.yoe,
        work_loc=job.workLoc,
        date_applied=job.dateApplied,
    )
    db.add(db_job)
    db.commit()
    db.refresh()

    return db_job


def update_job():
    pass


def get_job(db: Session, job_id: int):
    return db.query(models.Jobs).filter(models.Jobs.id == job_id).first()


def get_all_jobs(db: Session, company_name: str):
    return db.query(models.Jobs).filter(models.Jobs.company_name == company_name)


def delete_job(db: Session, job_id: int):
    return (
        db.query(models.Jobs)
        .filter(models.Jobs.id == job_id)
        .delete(synchronize_session=False)
    )
