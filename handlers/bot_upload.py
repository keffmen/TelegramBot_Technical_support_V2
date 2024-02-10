from aiogram import Router
from aiohttp.web_request import Request
from aiogram.types import Message
from aiogram import Bot
router = Router()


async def upload(request: Request):
    print(request)