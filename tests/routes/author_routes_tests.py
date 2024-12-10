import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.config.database import get_db


@pytest.fixture
def client(mock_db, mock_authors):
    # Mocking DB session to return mock authors
    mock_db.query.return_value.all.return_value = mock_authors
    # Overriding get_db dependency to use the mock DB session
    app.dependency_overrides[get_db] = lambda: mock_db
    return TestClient(app)