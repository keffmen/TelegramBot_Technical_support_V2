import asyncio
import os
from log_config import *
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import (
    bot_commands,
    bot_messages,
    bot_errors,
    bot_startup)


async def main() -> None:
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        bot_commands.router,
        bot_messages.router,
        bot_startup.router,
        bot_errors.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
