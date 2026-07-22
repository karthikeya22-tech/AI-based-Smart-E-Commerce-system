import pytest
from pydantic import ValidationError

from app.schemas.cart import CartItem, UpdateCart


def test_cart_item():

    cart = CartItem(
        user_id="user1",
        product_id=10,
        quantity=3
    )

    assert cart.quantity == 3


def test_update_cart():

    update = UpdateCart(
        quantity=5
    )

    assert update.quantity == 5


def test_invalid_cart():

    with pytest.raises(ValidationError):
        CartItem(
            user_id="user1",
            product_id="abc",
            quantity="xyz"
        )