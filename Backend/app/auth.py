from fastapi import Depends, FastAPI, HTTPException, APIRouter, Request
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import schemas
from . import database

from . import crud
from middleware import limiter, JWTMiddleware, configure_cors

# FastAPI app and router
app = FastAPI()
auth_router = APIRouter(prefix="/auth", tags=["auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


#####
# Auth Endpoints
#####


def hash_password(password: str):
    """
    Hash a password using bcrypt.
    """
    return pwd_context.hash(password)


@auth_router.post("/", response_model=schemas.CreateUser)
def create_user(
    request: Request, user: schemas.CreateUser, db: Session = Depends(get_db)
):
    """
    Create a new user.
    """
    hashed_password = hash_password(user.password)
    db_user = crud.create_user(db=db, user=user, hashed_password=hashed_password)
    return db_user
