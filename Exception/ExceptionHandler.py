from fastapi import Request
from starlette.responses import JSONResponse

from Exception.CustomError import CustomError


def exception_handler(request: Request, exception: Exception):
    return JSONResponse(status_code=500, content=CustomError(
                            error=str(exception),
                            path=str(request.url),
                            type=exception.__class__.__name__
                            ).dict())