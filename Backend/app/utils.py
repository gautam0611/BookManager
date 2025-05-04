from fastapi import Depends, FastAPI, HTTPException, APIRouter, Request
from jose import JWTError, jwt
from app import schemas
from .schemas import DataToken
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# authentication variables
SECRET_KEY = "9bd34ad4e2e69153fb348ae014c6bb87c6cac2a81a6801b7c774d0da0cda6c15"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def hash_password(password: str):
    """
    Hash a password using bcrypt.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    """
    Verify a password against a hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    """
    Create an access token using JWT.
    """
    # Implementation of JWT token creation
    to_encode = data.copy()
    expire = datetime.now() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token_access(token: str, credentials_exception):
    """
    Verify a password against a hashed password.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.DataToken(id=id)
    except JWTError:
        raise credentials_exception
    return token_data
