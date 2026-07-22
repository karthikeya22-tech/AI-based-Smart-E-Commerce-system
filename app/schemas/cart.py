# Cart schema
from pydantic import BaseModel


class CartItem(BaseModel):
    user_id: str
    product_id: int
    quantity: int = 1


class UpdateCart(BaseModel):
    quantity: int