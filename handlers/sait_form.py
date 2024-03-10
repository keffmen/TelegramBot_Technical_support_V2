from aiogram import Router
from aiohttp import web
from aiohttp.web_request import Request

router = Router()


async def form(request: Request):
    with open('templates/index.html', encoding='utf-8') as f:
        return web.Response(text=f.read(), content_type='text/html')
