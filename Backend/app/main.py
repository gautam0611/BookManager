from typing import List
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import schemas
from . import database

from . import crud

app = FastAPI()
router = APIRouter(prefix="/books", tags=["books"])

# Configure CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # Update to match your frontend origin
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allow all headers
# )


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


@router.post("/", response_model=schemas.BookCreate)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.create_book(db=db, book=book)
    return db_book


@router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, updated_book: dict, db: Session = Depends(get_db)):
    db_book = crud.update_book(db=db, book_id=book_id, updated_book=updated_book)
    return db_book


@router.get("/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db=db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.get("/", response_model=List[schemas.Book])
def get_all_books(db: Session = Depends(get_db)):
    db_books = crud.get_all_books(db=db)
    return db_books


@router.delete("/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db=db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


app.include_router(router)
