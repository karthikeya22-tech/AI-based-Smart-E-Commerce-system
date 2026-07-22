# FastAPI application entrypoint
from fastapi import FastAPI

app = FastAPI(
    title="AI Smart E-Commerce API",
    version="1.0.0",
    description="Backend API for AI-Based Smart E-Commerce"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Smart E-Commerce API 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }