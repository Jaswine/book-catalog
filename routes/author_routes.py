from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_db
from schemas.author import AuthorResponse, AuthorCreate, AuthorUpdate
from services.author_services import (find_all_authors, create_author,
                                      find_author_by_id, delete_author_by_id, find_and_update_author_by_id)

router = APIRouter()

@router.post("", status_code=201, response_model=AuthorResponse)
def create_author_endpoint_(author: AuthorCreate, db: Session = Depends(get_db)) -> AuthorResponse:
    """
        Создание автора
    """
    return create_author(db, author)

@router.get('', response_model=list[AuthorResponse])
def get_authors(db: Session = Depends(get_db)) -> list[AuthorResponse]:
    """
        Получение списка авторов
    """
    return find_all_authors(db)

@router.get("/{author_id}", response_model=AuthorResponse)
def get_author_by_id(author_id: int, db: Session = Depends(get_db)) -> AuthorResponse | HTTPException:
    """
        Получение информации об авторе по id
    """
    if author := find_author_by_id(db, author_id):
        return author
    raise HTTPException(status_code=404, detail="Author not found")

@router.put('/{author_id}', response_model=AuthorResponse)
def update_author(author_id: int, author: AuthorUpdate, db: Session = Depends(get_db)):
    """
        Обновление информации об авторе
    """
    if author := find_and_update_author_by_id(db, author_id, author):
        return author
    raise HTTPException(status_code=404, detail="Author not found")

@router.delete('/{author_id}', status_code=204)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    """
        Удаление автора
    """
    delete_author_by_id(db, author_id)
