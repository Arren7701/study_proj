import pytest
from app.http.llmops_app import run_app

@pytest.fixture
def client():
    run_app.config["TESTING"] = True
    with run_app.test_client() as client:
        yield client