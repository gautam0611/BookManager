from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import schemas
from . import database

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


@app.get("/book/{book_id}", response_model=schemas.Book)
def get_books(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_job(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.get("/all_books/{company_name}", response_model=schemas.Book)
def get_all_books(company_name: str, db: Session = Depends(get_db)):
    db_books = crud.get_all_books(db, company_name=company_name)
    if not db_books:
        raise HTTPException(status_code=404, detail="books not found for company")
    return db_books


@app.post("/book", response_model=schemas.Book)
def add_book(job: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = schemas.BookCreate(
        company_name=job.company_name,
        title=job.title,
        location=job.location,
        salary=job.salary,
        yoe=job.yoe,
        workLoc=job.workLoc,
        dateApplied=job.dateApplied,
        jobURL=job.jobURL,
    )
    return crud.create_job(db, db_book)


@app.put("/book/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, new_book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.update_book(db, book_id, new_book)


@app.delete("/book/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.delete_book(db, book_id)
