from sqlalchemy.orm import Session

from models.author import Author
from schemas.author import AuthorCreate, AuthorUpdate


def find_all_authors(db: Session) -> list[Author]:
    """
        Получение списка авторов
        :param db:Session
        :return: Список авторов
    """
    return db.query(Author).all()

def create_author(db: Session, author: AuthorCreate) -> AuthorCreate:
    """
        Создание нового автора
        :param db: Session
        :param author: AuthorCreate - Данные автора
        :return: Новый автор
    """
    db_author = Author(first_name=author.first_name,
                       last_name=author.last_name,
                       birth_date=author.birth_date)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def find_author_by_id(db: Session, author_id: int) -> Author | None:
    """
        Получение информации об авторе по id
        :param db: Session
        :param author_id: int - Идентификатор автора
        :return: Данные автора или None
    """
    try:
        return db.query(Author).filter(Author.id == author_id).first()
    except Exception as e:
        print(f'Error: {str(e)}')
        return None

def find_and_update_author_by_id(db: Session, author_id: int, author_data: AuthorUpdate) -> Author | None:
    """
        Обновление информации об авторе
        :param db: Session
        :param author_id: int - Идентификатор автора
        :return: Данные автора или None
    """
    try:
        author = db.query(Author).filter(Author.id == author_id).first()
        if author:
            author.first_name = author_data.first_name
            author.last_name = author_data.last_name
            author.birth_date = author_data.birth_date
            db.commit()
            db.refresh(author)
            return author
    except Exception as e:
        print(f'Error: {str(e)}')
        return None


def delete_author_by_id(db: Session, author_id: int) -> None:
    """
        Удаление автора
        :param db: Session
        :param author_id: int - Идентификатор автора
        :return: None
    """
    try:
        author = db.query(Author).filter(Author.id == author_id).first()
        if author:
            db.delete(author)
            db.commit()
            return None
    except Exception as e:
        print(f'Error: {str(e)}')
        return None