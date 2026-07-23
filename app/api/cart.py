# Cart endpoints
from fastapi import APIRouter

from app.services.cart_service import cart_service

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.get("/")
def get_cart():
    return cart_service.get_cart()