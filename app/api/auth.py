# Auth endpoints
from fastapi import APIRouter

from app.services.auth_service import auth_service

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/status")
def auth_status():
    return auth_service.get_status()