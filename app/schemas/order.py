# Order schema
from typing import List

from pydantic import BaseModel


class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: float


class Order(BaseModel):
    user_id: str
    total_price: float
    status: str


class CreateOrder(BaseModel):
    user_id: str
    items: List[OrderItem]