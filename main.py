import uvicorn
from fastapi import FastAPI

from Exception.ExceptionHandler import exception_handler
from Middleware.auth import JWTAuthMiddleware
from routes.router import router

app = FastAPI()

app.add_middleware(JWTAuthMiddleware)
app.add_exception_handler(Exception, exception_handler)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, port=4002, host="127.0.0.1")