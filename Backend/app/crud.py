from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models

from .schemas import Book


def create_job(db: Session, book: Book):
    db_book = models.Jobs(
        company_name=job.company_name,
        title=job.title,
        location=job.location,
        salary=job.salary,
        yoe=job.yoe,
        workLoc=job.workLoc,  # Ensure this matches the model
        dateApplied=job.dateApplied,
        jobURL=job.jobURL,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


def update_job(db: Session, book_id: int, updated_job: dict):
    db_book = db.query(models.Books).filter(models.Books.id == book_id).first()

    if not db_book:
        raise HTTPException(status_code=404, detail="Job does not exist")

    for key, val in updated_job.items():
        if hasattr(db_book, key):
            setattr(db_book, key, val)

    db.add()
    db.commit()
    db.refresh(db_book)

    return db_book


def get_job(db: Session, book_id: int):
    return db.query(models.Jobs).filter(models.Books.id == book_id).first()


def get_all_jobs(db: Session, company_name: str):
    return db.query(models.Jobs).filter(models.Books.company_name == company_name)


def delete_job(db: Session, book_id: int):
    return (
        db.query(models.Books)
        .filter(models.Books.id == book_id)
        .delete(synchronize_session=False)
    )
