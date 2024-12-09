from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_db
from schemas.borrow import BorrowCreate, BorrowResponse, BorrowUpdate
from services.borrow_services import (create_borrow_and_check_book_exists, find_all_borrows,
                                      find_borrow_by_id, update_borrow_returning_status_by_id)

router = APIRouter()

@router.post('', status_code=201, response_model=BorrowResponse)
def create_borrow_endpoint(borrow: BorrowCreate,
                  db: Session = Depends(get_db)) -> BorrowResponse:
    """
        Создание записи о выдаче книги
    """
    return create_borrow_and_check_book_exists(db, borrow)


@router.get('', response_model=list[BorrowResponse])
def get_all_borrows_endpoint(db: Session = Depends(get_db)) -> list[BorrowResponse]:
    """
        Получение списка всех выдач
    """
    return find_all_borrows(db)

@router.get('/{borrow_id}', response_model=BorrowResponse)
def get_borrow_by_id_endpoint(borrow_id: int, db: Session = Depends(get_db)) -> BorrowResponse | HTTPException:
    """
        Получение информации о выдаче по id
    """
    if borrow := find_borrow_by_id(db, borrow_id):
        return borrow
    raise HTTPException(status_code=404, detail="Borrow not found")

@router.patch('/{borrow_id}/return', response_model=BorrowResponse)
def update_borrow_by_id(borrow_id: int,
                        borrow_data: BorrowUpdate,
                        db: Session = Depends(get_db)) -> BorrowResponse | HTTPException:
    """
        Обновление статуса выдачи книги по id
    """
    if borrow := update_borrow_returning_status_by_id(db, borrow_id, borrow_data):
        return borrow
    raise HTTPException(status_code=404, detail="Borrow not found")
