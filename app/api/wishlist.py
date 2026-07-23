# Wishlist endpoints
from fastapi import APIRouter

from app.services.wishlist_service import wishlist_service

router = APIRouter(
    prefix="/wishlist",
    tags=["Wishlist"]
)


@router.get("/")
def get_wishlist():
    return wishlist_service.get_wishlist()