from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas.author import AuthorResponse, AuthorCreate, AuthorUpdate
from app.services.author_services import (find_all_authors, create_author,
                                          find_author_by_id, delete_author_by_id, find_and_update_author_by_id)

router = APIRouter()

@router.post('', status_code=201,
             response_model=AuthorResponse, name='Создание автора')
def create_author_endpoint(author: AuthorCreate, db: Session = Depends(get_db)) -> AuthorResponse:
    """
        Создание автора
    """
    return create_author(db, author)

@router.get('', response_model=list[AuthorResponse],
            name='Получение списка авторов')
def get_authors_endpoint(db: Session = Depends(get_db)) -> list[AuthorResponse]:
    """
        Получение списка авторов
    """
    return find_all_authors(db)

@router.get('/{author_id}', response_model=AuthorResponse,
            name='Получение информации об авторе по id')
def get_author_by_id_endpoint(author_id: int, db: Session = Depends(get_db)) -> AuthorResponse | HTTPException:
    """
        Получение информации об авторе по id
    """
    if author := find_author_by_id(db, author_id):
        return author
    raise HTTPException(status_code=404, detail='Author not found')

@router.put('/{author_id}', response_model=AuthorResponse,
            name='Обновление информации об авторе')
def update_author_endpoint(author_id: int, author: AuthorUpdate, db: Session = Depends(get_db)):
    """
        Обновление информации об авторе
    """
    if author := find_and_update_author_by_id(db, author_id, author):
        return author
    raise HTTPException(status_code=404, detail='Author not found')

@router.delete('/{author_id}', status_code=204,
               name='Удаление автора')
def delete_author_endpoint(author_id: int, db: Session = Depends(get_db)):
    """
        Удаление автора
    """
    delete_author_by_id(db, author_id)
