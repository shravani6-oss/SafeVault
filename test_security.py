import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app import app
from database import get_db, init_db


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "test-secret"

    init_db()

    with app.test_client() as client:
        yield client


def test_login_page(client):
    response = client.get("/login")

    assert response.status_code == 200


def test_invalid_login(client):
    response = client.post(
        "/login",
        data={
            "email": "wrong@example.com",
            "password": "wrongpassword"
        }
    )

    assert b"Invalid email or password" in response.data


def test_sql_injection_protection(client):
    malicious_email = "' OR '1'='1"

    response = client.post(
        "/login",
        data={
            "email": malicious_email,
            "password": "anything"
        }
    )

    assert b"Invalid email or password" in response.data


def test_unauthorized_dashboard(client):
    response = client.get("/dashboard")

    assert response.status_code == 302


def test_admin_access_protection(client):
    response = client.get("/admin")

    assert response.status_code == 302