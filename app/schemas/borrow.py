from datetime import date
from typing import Optional
from pydantic import BaseModel

from app.schemas.book import BookAuthorResponse

class BorrowBase(BaseModel):
    reader_name: str

class BorrowBookResponse(BaseModel):
    id: int
    title: str
    copies_count: int
    author: BookAuthorResponse

class BorrowResponse(BorrowBase):
    id: int
    issuing_book: Optional[date]
    returning_book: Optional[date]
    book: BorrowBookResponse

    class Config:
        orm_mode = True

class BorrowBaseWithBookId(BorrowBase):
    book_id: int

class BorrowCreate(BorrowBaseWithBookId):
    issuing_book: str

class BorrowUpdate(BaseModel):
    returning_book: str