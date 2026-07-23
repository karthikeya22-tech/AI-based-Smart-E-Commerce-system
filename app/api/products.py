# Product endpoints
from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import pagination
from app.services.product_service import product_service

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
def get_products(page=Depends(pagination)):
    return product_service.list_products(page["page"], page["limit"])


@router.get("/{product_id}")
def get_product(product_id: int):
    product = product_service.get_product(product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product