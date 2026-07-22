import pytest
from pydantic import ValidationError

from app.schemas.order import (
    Order,
    OrderItem,
    CreateOrder
)


def test_order_item():

    item = OrderItem(
        product_id=1,
        quantity=2,
        price=499.0
    )

    assert item.quantity == 2


def test_create_order():

    order = CreateOrder(
        user_id="user1",
        items=[
            OrderItem(
                product_id=1,
                quantity=1,
                price=999.0
            )
        ]
    )

    assert len(order.items) == 1


def test_order_schema():

    order = Order(
        user_id="user1",
        total_price=1999.0,
        status="Pending"
    )

    assert order.status == "Pending"


def test_invalid_order():

    with pytest.raises(ValidationError):
        OrderItem(
            product_id="abc",
            quantity="xyz",
            price="invalid"
        )