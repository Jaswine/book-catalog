from fastapi import FastAPI

from dotenv import load_dotenv

from app.config import database
from app.config.settings import Settings
from app.config.database import Base, engine
from app.routes import author_routes, book_routes, borrow_routes

load_dotenv()

Base = Base.metadata.create_all(bind=engine)

settings = Settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

app.include_router(author_routes.router, prefix='/authors', tags=['Authors'])
app.include_router(book_routes.router, prefix='/books', tags=['Books'])
app.include_router(borrow_routes.router, prefix='/borrows', tags=['Borrows'])