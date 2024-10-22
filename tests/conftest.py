import pytest
from api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client

# Additional fixtures can be added here
