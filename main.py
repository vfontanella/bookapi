from fastapi import FastAPI

from api.v1.router.user import router as user_router
from api.v1.router.book import router as book_router

app = FastAPI()

app.include_router(user_router)
app.include_router(book_router)