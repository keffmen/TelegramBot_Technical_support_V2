from aiogram import Router
from aiohttp import web
from aiohttp.web_request import Request

router = Router()


async def form(request: Request):
    with open('web_forma/index.html', encoding='utf-8') as f:
        return web.Response(text=f.read(), content_type='text/html')


async def authorization(request: Request):
    with open('web_authorization/index.html', encoding='utf-8') as f:
        return web.Response(text=f.read(), content_type='text/html')




