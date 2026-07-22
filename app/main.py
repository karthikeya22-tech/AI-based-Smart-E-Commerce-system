from fastapi import FastAPI

from app.api import (
    auth,
    cart,
    catalog,
    orders,
    products,
    recommendation,
    reverse_search,
    wishlist
)

app = FastAPI(
    title="AI Smart E-Commerce API",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(wishlist.router)
app.include_router(orders.router)
app.include_router(catalog.router)
app.include_router(recommendation.router)
app.include_router(reverse_search.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Smart E-Commerce API 🚀"
    }