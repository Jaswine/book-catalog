from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    description: str
    author_id: int
    copies_count: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True
