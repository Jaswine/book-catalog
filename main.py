from fastapi import FastAPI

from dotenv import load_dotenv
from config import database
from config.settings import Settings
from config.database import Base
from routes import author_routes, book_routes, borrow_routes
from models.author import Author
from models.book import Book, Borrow


load_dotenv()

database.Base = Base.metadata.create_all(bind=database.engine)

settings = Settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

app.include_router(author_routes.router, prefix='/authors', tags=['Authors'])
app.include_router(book_routes.router, prefix='/books', tags=['Books'])
app.include_router(borrow_routes.router, prefix='/borrows', tags=['Borrows'])