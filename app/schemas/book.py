from pydantic import BaseModel
from datetime import date
from typing import Optional, List


class BookBase(BaseModel):
    title: str
    description: str
    copies_count: int

class BookAuthorResponse(BaseModel):
    id: int
    first_name: str
    last_name: str

class BookBorrowResponse(BaseModel):
    id: int
    reader_name: str
    issuing_book: Optional[date] = None
    returning_book: Optional[date] = None

class BookResponse(BookBase):
    id: int
    author: BookAuthorResponse
    borrowed_books: List[BookBorrowResponse]

    class Config:
        orm_mode = True

class BookBaseWithAuthorId(BookBase):
    author_id: int

class BookCreate(BookBaseWithAuthorId):
    pass

class BookUpdate(BookBaseWithAuthorId):
    pass
