import pytest
from pydantic import ValidationError

from app.schemas.user import User, UserCreate


def test_user_creation():

    user = User(
        id="user123",
        email="john@example.com",
        full_name="John Doe",
        phone="9876543210"
    )

    assert user.email == "john@example.com"


def test_user_create():

    user = UserCreate(
        email="alice@example.com",
        password="password123",
        full_name="Alice"
    )

    assert user.full_name == "Alice"


def test_invalid_email():

    with pytest.raises(ValidationError):
        UserCreate(
            email="invalid-email",
            password="123456",
            full_name="John"
        )