# Order endpoints
from fastapi import APIRouter

from app.services.order_service import order_service

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("/")
def get_orders():
    return order_service.get_orders()