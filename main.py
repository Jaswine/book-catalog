from fastapi import FastAPI

from config import database
from config.settings import Settings
from config.database import Base
from routes import author_routes, book_routes
from models.author import Author
from models.book import Book, Borrow


Base.metadata.create_all(bind=database.engine)

settings = Settings()
app = FastAPI()

app.include_router(author_routes.router, prefix="/authors", tags=["Authors"])
app.include_router(book_routes.router, prefix="/books", tags=["Books"])