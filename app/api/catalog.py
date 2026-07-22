# Catalog endpoints
from fastapi import APIRouter

router = APIRouter(
    prefix="/catalog",
    tags=["Catalog"]
)


@router.get("/")
def catalog():

    return {
        "message": "Catalog API coming soon"
    }