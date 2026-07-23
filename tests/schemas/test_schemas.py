from pydantic import ValidationError
import pytest

from app.schemas.cart import CartItem, UpdateCart
from app.schemas.order import OrderItem


def test_cart_schema():
    item = CartItem(user_id="u1", product_id=1, quantity=2)
    assert item.quantity == 2


def test_cart_update_schema():
    update = UpdateCart(quantity=5)
    assert update.quantity == 5


def test_order_item_schema():
    item = OrderItem(product_id=1, quantity=2, price=99.0)
    assert item.price == 99.0


def test_invalid_cart_quantity():
    with pytest.raises(ValidationError):
        CartItem(user_id="u1", product_id=1, quantity="bad")
