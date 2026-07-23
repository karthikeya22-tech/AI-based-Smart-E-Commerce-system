import pytest
from pydantic import ValidationError

from app.schemas.product import Product, ProductCreate


def test_product_creation():

    product = Product(
        id=1,
        product_name="Blue Casual Shirt",
        category="Shirts",
        article_type="Casual Shirt",
        gender="Men",
        base_colour="Blue",
        season="Summer",
        usage="Casual",
        price=999.0,
        image_url="https://example.com/shirt.jpg",
        description="Comfortable cotton shirt"
    )

    assert product.id == 1
    assert product.product_name == "Blue Casual Shirt"
    assert product.price == 999.0


def test_product_create_schema():

    product = ProductCreate(
        product_name="Black Shoes",
        category="Shoes",
        price=1499.0
    )

    assert product.product_name == "Black Shoes"


def test_invalid_product():

    with pytest.raises(ValidationError):
        Product(
            id="abc",
            product_name=123
        )