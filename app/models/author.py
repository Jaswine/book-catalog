from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from app.config.database import Base


class Author(Base):
    """
       Автор
    """
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String,index=True)
    last_name = Column(String, index=True)
    birth_date = Column(Date)

    books = relationship('Book', back_populates='author')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
