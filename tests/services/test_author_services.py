import pytest
from datetime import date
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.config.database import Base
from app.models.author import Author
from app.services.author_services import find_all_authors, create_author, find_author_by_id
from app.schemas.author import AuthorCreate


@pytest.fixture
def mock_db():
    """
        Мок-объект для базы данных
    """
    mock = MagicMock(Session)
    mock.query.return_value.filter.return_value.first.return_value = None
    return mock

@pytest.fixture
def mock_author1(mock_db):
    """
        Мок-автор 1
    """
    return Author(id=1, first_name='Roronoa', last_name='Zoro', birth_date=date.today())

@pytest.fixture
def mock_author2(mock_db):
    """
        Мок-автор 2
    """
    return Author(id=2, first_name='Vinsmoke', last_name='Sanji', birth_date=date.today())

@pytest.fixture
def mock_authors(mock_author1, mock_author2):
    """
        Мок-список авторов
    """
    return [mock_author1, mock_author2]


def test_find_all_authors(mock_db, mock_authors):
    """
        Тест на получение всех авторов
    """
    mock_db.query().all.return_value = mock_authors

    result = find_all_authors(mock_db)

    assert len(result) == len(mock_authors)

def test_create_author(mock_db, mock_author2):
    """
        Тест на создание нового автора
    """
    author_data = AuthorCreate(first_name='Roronoa', last_name='Zoro', birth_date='1990-01-01')

    mock_db.add.return_value = None
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = mock_author2

    result = create_author(mock_db, author_data)

    print(result.first_name, result.last_name)
    assert result.first_name == author_data.first_name
    assert result.last_name == author_data.last_name

def test_find_author_by_id(mock_db, mock_authors):
    """
        Тест на получение автора по id
    """
    mock_db.query().filter.return_value.first.return_value = mock_authors[0]

    result = find_author_by_id(mock_db, mock_authors[0].id)

    assert result.first_name == mock_authors[0].first_name
    assert result.last_name == mock_authors[0].last_name
