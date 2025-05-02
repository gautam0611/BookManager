from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt, JWTError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Initialize the rate limiter
limiter = Limiter(key_func=get_remote_address)


# JWT Middleware
class JWTMiddleware:
    def __init__(self, secret_key: str, algorithm: str):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.auth_scheme = HTTPBearer()

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid or expired token")

    def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = self.auth_scheme(request)
        if not credentials:
            raise HTTPException(status_code=401, detail="Authorization header missing")
        return self.verify_token(credentials.credentials)


# CORS Middleware Configuration
def configure_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # Update to match your frontend origin
        allow_credentials=True,
        allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
        allow_headers=["*"],  # Allow all headers
    )
