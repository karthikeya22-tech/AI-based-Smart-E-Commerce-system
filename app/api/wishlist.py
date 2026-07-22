# Wishlist endpoints
from fastapi import APIRouter

router = APIRouter(
    prefix="/wishlist",
    tags=["Wishlist"]
)


@router.get("/")
def get_wishlist():

    return {
        "message": "Wishlist API under development"
    }