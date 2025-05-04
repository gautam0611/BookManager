# run.py
from fastapi import FastAPI
from app.auth import auth_router
from app.book import book_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(book_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=f"127.0.0.1", port=8000)
