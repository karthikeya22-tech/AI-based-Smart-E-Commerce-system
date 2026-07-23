from fastapi import Request
from fastapi.responses import JSONResponse


class RateLimitMiddleware:
    def __init__(self, app, limit: int = 60):
        self.app = app
        self.limit = limit

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        await self.app(scope, receive, send)
