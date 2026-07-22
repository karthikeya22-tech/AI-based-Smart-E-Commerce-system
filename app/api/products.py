# Product endpoints
from fastapi import APIRouter, Depends, HTTPException

from app.database import supabase
from app.dependencies import pagination

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
def get_products(page=Depends(pagination)):
    response = (
        supabase
        .table("products")
        .select("*")
        .range(
            page["offset"],
            page["offset"] + page["limit"] - 1
        )
        .execute()
    )

    return response.data


@router.get("/{product_id}")
def get_product(product_id: int):

    response = (
        supabase
        .table("products")
        .select("*")
        .eq("id", product_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return response.data[0]