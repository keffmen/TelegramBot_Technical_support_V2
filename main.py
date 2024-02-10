import asyncio
import os
from log_config import *
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
    bot_startup)


async def on_startup(bot: Bot, base_url: str):
    await bot.set_webhook(f"{base_url}/webhook")


async def main() -> None:
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    SERVER = os.getenv("SERVER")

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp["base_url"] = SERVER
    dp.startup.register(on_startup)
    dp.include_routers(
        bot_commands.router,
        bot_messages.router,
        bot_startup.router,
        bot_errors.router
    )
    app = Application()
    app["bot"] = bot

    app.router.add_get("/upload", bot_upload.upload)
    SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    ).register(app, path="/webhook")
    setup_application(app, dp, bot=bot)

    run_app(app, host="127.0.0.1", port=8081)

if __name__ == "__main__":
    asyncio.run(main())
