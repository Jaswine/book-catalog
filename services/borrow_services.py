from http.client import HTTPException

from sqlalchemy.orm import Session

from models.book import Borrow, Book
from schemas.borrow import BorrowCreate, BorrowUpdate


def find_all_borrows(db: Session) -> list[Borrow]:
    """
        Получение списка всех записей о выдаче книги
        :param db: Session
        :return: Список всех записей о выдаче книги
    """
    return db.query(Borrow).all()


def create_borrow_and_check_book_exists(db: Session, borrow: BorrowCreate) -> Borrow:
    """
        Создание новой записи о выдаче книги и проверка существования книги
        :param db: Session
        :param borrow: BorrowCreate - Данные новой записи о выдаче
        :return: Запись о выдаче книги
    """
    try:
        book_db = db.query(Book).filter(Book.id == borrow.book_id).first()
        if book_db and book_db.copies_count > 0:
            # Уменьшаем количество копий книги
            book_db.copies_count -= 1
            db.commit()

            # Создаем запись о выдаче
            return create_borrow(db, borrow)
        raise HTTPException(status_code=400, detail="No available copies of the book")
    except Exception as e:
        print(f'Error: {str(e)}')
        raise HTTPException(status_code=404, detail="Book not found")

def create_borrow(db: Session, borrow: BorrowCreate) -> Borrow:
    """
        Создание записи о выдаче книги
        :param db: Session
        :param borrow: BorrowCreate - Данные новой записи о выдаче
        :return: Запись о выдаче книги
    """
    db_borrow = Borrow(
        book_id=borrow.book_id,
        reader_name=borrow.reader_name,
        issuing_book=borrow.issuing_book,
        returning_book=None,
    )
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)
    return db_borrow

def find_borrow_by_id(db: Session, borrow_id: int) -> Borrow | None:
    """
        Получение информации о выдаче по id
        :param db: Session
        :param borrow_id: int - Идентификатор выдачи
        :return: Данные выдачи или None
    """
    try:
        return db.query(Borrow).filter(Borrow.id == borrow_id).first()
    except Exception as e:
        print(f'Error: {str(e)}')
        return None


def update_borrow_returning_status_by_id(db: Session,
                                         borrow_id: int,
                                         borrow_data: BorrowUpdate) -> Borrow | None:
    """
        Обновление статуса возвращения книги по id
        :param db: Session
        :param borrow_id: int - Идентификатор выдачи
        :param borrow_data: BorrowUpdate - Данные для изменения
        :return: Данные выдачи или None
    """
    try:
        borrow_db = db.query(Borrow).filter(Borrow.id == borrow_id).first()
        if borrow_db:
            if borrow_db.returning_book is None and borrow_data.returning_book:
                book_db = db.query(Book).filter(Book.id == borrow_db.book_id).first()
                if book_db:
                    book_db.copies_count += 1

            borrow_db.returning_book = borrow_data.returning_book
            db.commit()
            db.refresh(borrow_db)
            return borrow_db
    except Exception as e:
        print(f'Error: {str(e)}')
        return None