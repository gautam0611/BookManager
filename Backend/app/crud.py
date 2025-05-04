from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models

from .schemas import Book


#########
# Book CRUD Operations
#########
def create_book(db: Session, book: Book):
    db_book = models.Book(
        title=book.title,
        number_of_pages=book.number_of_pages,
        author=book.author,
        genre=book.genre,
        published_date=book.published_date,
        date_added=book.date_added,
    )
    # Check if the book already exists
    existing_book = (
        db.query(models.Book).filter(models.Book.title == book.title).first()
    )
    if existing_book:
        raise HTTPException(
            status_code=400,
            detail="Book with this title already exists",
        )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


def update_book(db: Session, book_id: int, updated_book: dict):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if not db_book:
        raise HTTPException(status_code=404, detail="Book does not exist")

    for key, val in updated_book.items():
        if hasattr(db_book, key):
            setattr(db_book, key, val)

    db.add()
    db.commit()
    db.refresh(db_book)

    return db_book


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_all_books(db: Session):
    return db.query(models.Book).all()


def get_all_books_by_author(db: Session, author: str):
    return db.query(models.Book).filter(models.Book.author == author)


def delete_book(db: Session, book_id: int):
    rows_deleted = (
        db.query(models.Book)
        .filter(models.Book.id == book_id)
        .delete(synchronize_session=False)
    )
    db.commit()  # Ensure changes are committed
    return {"book_id": book_id, "rows_deleted": rows_deleted}


#########
# Auth CRUD Operations
#########
def create_user(db: Session, user: Book):
    db_user = models.AuthUser(**user.model_dump())

    # Check if the user already exists
    existing_user = (
        db.query(models.AuthUser)
        .filter(models.AuthUser.user_name == user.username)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User with this username already exists",
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
