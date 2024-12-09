from datetime import date
from typing import Optional

from pydantic import BaseModel

class BorrowBase(BaseModel):
    book_id: int
    reader_name: str

class BorrowCreate(BorrowBase):
    issuing_book: str

class BorrowUpdate(BaseModel):
    returning_book: str

class BorrowResponse(BorrowBase):
    id: int
    issuing_book: Optional[date]
    returning_book: Optional[date]

    class Config:
        orm_mode = True
