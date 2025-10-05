from fastapi import APIRouter

from Controller.MyController import MyController
from Request.RequestTemplate import User

router = APIRouter(prefix="/user")


@router.get("/path/{value}")
async def root(value: int)->int:
    return await MyController.test_path(value)

@router.get("/query")
async def root(key1: int, key2: int)->int:
    return await MyController.test_param(key1, key2)


@router.post("/login")
async def root(user: User):
    return await MyController.test_body(user)
