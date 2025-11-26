from typing import List
from fastapi import Depends, HTTPException, APIRouter, Request
from sqlalchemy.orm import Session
from Backend.settings import database
from Backend.api.book import crud
from run import app

from Backend.api.book import schemas

book_router = APIRouter(prefix="/books", tags=["books"])


# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


#################
# Book Endpoints
#################
@book_router.post("/", response_model=schemas.BookCreate)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.create_book(db=db, book=book)
    return db_book


@book_router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, updated_book: dict, db: Session = Depends(get_db)):
    db_book = crud.update_book(db=db, book_id=book_id, updated_book=updated_book)
    return db_book


@book_router.get("/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db=db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@book_router.get("/", response_model=List[schemas.Book])
def get_all_books(db: Session = Depends(get_db)):
    db_books = crud.get_all_books(db=db)
    return db_books


@book_router.delete("/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db=db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
