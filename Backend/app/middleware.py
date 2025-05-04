from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt, JWTError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Initialize the rate limiter
limiter = Limiter(key_func=get_remote_address)


# CORS Middleware Configuration
def configure_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # Update to match your frontend origin
        allow_credentials=True,
        allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
        allow_headers=["*"],  # Allow all headers
    )
