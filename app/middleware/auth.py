from fastapi import Request
from fastapi.responses import JSONResponse


async def auth_middleware(request: Request, call_next):
    """Placeholder auth middleware that preserves request flow."""
    response = await call_next(request)
    return response
