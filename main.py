import os
from log_config import *
import ssl
from aiohttp.web import run_app
from aiohttp.web_app import Application
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from handlers import (
    bot_upload,
    bot_commands,
    bot_messages,
    bot_errors,
    bot_startup,
    sait_form)


async def on_startup(bot: Bot, base_url: str):
    await bot.set_webhook(f"{base_url}/webhook")


def main() -> None:
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    HOST = os.getenv("HOST")

    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp["base_url"] = f"{HOST}"
    dp.startup.register(on_startup)
    dp.include_routers(
        bot_commands.router,
        bot_messages.router,
        bot_startup.router,
        bot_errors.router
    )
    app = Application()
    app["bot"] = bot

    app.router.add_post("/upload", bot_upload.upload)
    # Добавление статических файлов (CSS, JS) и папки assets
    app.router.add_static('/static/', path='static', name='static')
    app.router.add_static('/assets/', path='assets', name='assets')
    # Обработчик сайта
    app.router.add_get('/forma', sait_form.form)

    SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    ).register(app, path="/webhook")
    setup_application(app, dp, bot=bot)

    run_app(app, host='0.0.0.0', port=8443)


if __name__ == "__main__":
    main()
