from typing import Type, List

from sqlalchemy.orm import Session

from models.book import Book
from schemas.book import BookCreate, BookUpdate


def find_all_books(db: Session) -> list[Type[Book]]:
    """
        Получение списка книг
        :param db:Session
        :return: Список книг
    """
    return db.query(Book).all()

def create_book(db: Session, book: BookCreate) -> Book:
    """
        Создание новой книги
        :param db: Session
        :param book: Book - Данные новой книги
        :return: Новая книга
    """
    db_book = Book(
        title=book.title,
        description=book.description,
        author_id=book.author_id,
        copies_count=book.copies_count,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def find_book_by_id(db: Session, book_id: int) -> Book | None:
    """
        Получение информации о книге по id
        :param db: Session
        :param book_id: int - Идентификатор книги
        :return: Данные книги или None
    """
    try:
        return db.query(Book).filter(Book.id == book_id).first()
    except Exception as e:
        print(f'Error: {str(e)}')
        return None

def update_book_by_id(db: Session, book_id: int, book: BookUpdate) -> Book | None:
    """
        Получение и изменение информации о книге по id
        :param db: Session
        :param book_id: int - Идентификатор книги
        :return: Данные книги или None
    """
    try:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if book:
            db_book.title = book.title
            db_book.description = book.description
            db_book.author_id = book.author_id
            db_book.copies_count = book.copies_count
            db.commit()
            db.refresh(db_book)
            return db_book
        else:
            return None
    except Exception as e:
        print(f'Error: {str(e)}')
        return None

def delete_book_by_id(db: Session, book_id: int) -> Book | None:
    """
        Удаление информации о книге по id
        :param db: Session
        :param book_id: int - Идентификатор книги
        :return: Данные книги или None
    """
    try:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if db_book:
            db.delete(db_book)
            db.commit()
            return db_book
        else:
            return None
    except Exception as e:
        print(f'Error: {str(e)}')
        return None