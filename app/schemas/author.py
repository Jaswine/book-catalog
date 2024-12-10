from datetime import date
from typing import Optional, List

from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[date]

class AuthorBookResponse(BaseModel):
    id: int
    title: str
    copies_count: int

class AuthorResponse(AuthorBase):
    id: int
    books: List[AuthorBookResponse]

    class Config:
        orm_mode = True

class AuthorCreate(AuthorBase):
    birth_date: str = None

class AuthorUpdate(AuthorBase):
    birth_date: str = None