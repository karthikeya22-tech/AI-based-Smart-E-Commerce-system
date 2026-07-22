# Reverse image search endpoints
from fastapi import APIRouter

router = APIRouter(
    prefix="/search",
    tags=["Reverse Search"]
)


@router.post("/")
def reverse_search():

    return {
        "message": "Reverse Search coming soon"
    }