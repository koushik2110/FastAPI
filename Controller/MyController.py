from Authentication.jwt import create_token
from Request.RequestTemplate import User
from dotenv import load_dotenv

load_dotenv(verbose=True)


class MyController:
    @staticmethod
    async def test_path(value: int):
        return value

    @staticmethod
    async def test_param(*args):
        return sum(args)

    @staticmethod
    async def test_body(user: User):
        return await create_token(user.name)
