# Recommendation endpoints
from fastapi import APIRouter

router = APIRouter(
    prefix="/recommendation",
    tags=["AI Recommendation"]
)


@router.post("/")
def recommend():

    return {
        "message": "Recommendation Engine coming soon"
    }