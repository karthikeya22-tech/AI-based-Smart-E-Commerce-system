from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    id: int
    product_name: str
    category: Optional[str] = None
    article_type: Optional[str] = None
    gender: Optional[str] = None
    base_colour: Optional[str] = None
    season: Optional[str] = None
    usage: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[str] = None
    description: Optional[str] = None


class ProductCreate(BaseModel):
    product_name: str
    category: Optional[str] = None
    article_type: Optional[str] = None
    gender: Optional[str] = None
    base_colour: Optional[str] = None
    season: Optional[str] = None
    usage: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[str] = None
    description: Optional[str] = None