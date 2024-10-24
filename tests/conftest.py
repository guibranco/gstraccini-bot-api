import pytest
from src.api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
