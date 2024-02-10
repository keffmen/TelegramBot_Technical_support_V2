from aiogram import Router
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import json_response
from aiogram.types import Message
from aiogram import Bot

router = Router()


async def upload(request: Request):
    # data = await request.json()
    print(f'Полученны данные:')
    response = web.Response(text='Данные получены!',
                            status=200,
                            headers={'X-Custom-Server-Header': 'Custom Data'})
    return response
