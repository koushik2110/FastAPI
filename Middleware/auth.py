from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from Authentication.jwt import verify_token


class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Allow unauthenticated access for login
        if request.url.path == "/user/login":
            return await call_next(request)

        # Get Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Missing or invalid Authorization header"})

        token = auth_header.split(" ")[1]
        payload = await verify_token(token)

        if not payload:
            return JSONResponse(status_code=401, content={"detail": "Invalid or expired token"})

        # Attach user info to request.state for later use
        request.state.user = payload.get("sub")
        return await call_next(request)
