from config.database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Book(Base):
    """
        Книга
    """
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    author_id = Column(Integer, ForeignKey("authors.id"))
    copies_count = Column(Integer, default=0)

    author = relationship('Author', back_populates='books', foreign_keys=[author_id])
    borrowed_books = relationship('Borrow', back_populates='book')

    def __str__(self):
        return f'{self.title}: {self.copies_count}'


class Borrow(Base):
    """
        Выдача
    """
    __tablename__ = 'borrows'

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    reader_name = Column(String)
    issuing_book = Column(Date, default=func.current_date())
    returning_book = Column(Date, default=None, nullable=True)

    book = relationship('Book', back_populates='borrowed_books', foreign_keys=[book_id])

    def __str__(self):
        return f'{self.reader_name} - {self.book.title}'
