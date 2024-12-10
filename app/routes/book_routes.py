from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas.book import BookCreate, BookResponse, BookUpdate
from app.services.book_services import (create_book, find_all_books,
                                        find_book_by_id, update_book_by_id, delete_book_by_id, )

router = APIRouter()

@router.post('', status_code=201, response_model=BookResponse,
             name='Добавление книги')
def create_book_endpoint(book: BookCreate,
                         db: Session = Depends(get_db)) -> BookResponse:
    """
        Добавление книги
    """
    return create_book(db, book)

@router.get('', response_model=list[BookResponse],
            name='Получение списка книг')
def show_all_books_endpoint(db: Session = Depends(get_db)) -> list[BookResponse]:
    """
        Получение списка книг
    """
    return find_all_books(db)

@router.get('/{book_id}', response_model=BookResponse,
            name='Получение информации о книге по id')
def show_book_by_id_endpoint(book_id: int,
                             db: Session = Depends(get_db)) -> BookResponse | HTTPException:
    """
        Получение информации о книге по id
    """
    if book := find_book_by_id(db, book_id):
        return book
    raise HTTPException(status_code=404, detail='Book not found')

@router.put('/{book_id}', response_model=BookResponse,
            name='Обновление информации о книге')
def update_book_endpoint(book_id: int,
                         book: BookUpdate,
                         db: Session = Depends(get_db)) -> BookResponse | HTTPException:
    """
       Обновелние информации книги по id
    """
    if book := update_book_by_id(db, book_id, book):
        return book
    raise HTTPException(status_code=404, detail='Book not found')

@router.delete('/{book_id}', status_code=204,
               name='Удаление книги')
def delete_book_endpoint(book_id: int,
                         db: Session = Depends(get_db)):
    """
        Удаление книги по id
    """
    delete_book_by_id(db, book_id)

