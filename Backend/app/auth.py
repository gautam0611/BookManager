from fastapi import Depends, FastAPI, HTTPException, APIRouter, Request, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app import models
from . import schemas
from . import database
from . import crud
from .utils import hash_password
from middleware import limiter, JWTMiddleware, configure_cors
from utils import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    verify_password,
    verify_token_access,
)

# FastAPI app and router
auth_router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    """
    Get the current user from the token.
    """
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_token_access(token, credentials_exception)
    user = db.query(models.AuthUser).filter(models.AuthUser.id == token_data.id).first()
    if user is None:
        raise credentials_exception
    return user


#####
# Auth Endpoints
#####


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


@auth_router.post("/login", response_model=schemas.DataToken)
def login(
    request: Request,
    userDetails: OAuth2PasswordBearer = Depends(),
    db: Session = Depends(get_db),
):
    """
    User login endpoint.
    """
    user = (
        db.query(models.AuthUser)
        .filter(models.AuthUser.user_name == userDetails.username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    if not verify_password(userDetails, user):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    access_token = create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
