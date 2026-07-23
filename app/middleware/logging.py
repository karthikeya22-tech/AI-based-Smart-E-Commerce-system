import logging
from fastapi import Request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai_fashion_app")


async def logging_middleware(request: Request, call_next):
    """Log request metadata for observability."""
    logger.info("%s %s", request.method, request.url.path)
    response = await call_next(request)
    return response
