from datetime import date
from typing import Optional

from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[date]

class AuthorResponse(AuthorBase):
    id: int

    class Config:
        orm_mode = True

class AuthorCreate(AuthorBase):
    birth_date: str

class AuthorUpdate(AuthorBase):
    birth_date: str