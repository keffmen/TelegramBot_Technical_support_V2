from aiogram import Router, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Этот обработчик получает сообщения с командой start.
    """
    markup = InlineKeyboardBuilder()
    markup.add(types.InlineKeyboardButton(text='Оформить заявку',web_app=WebAppInfo(url='https://a43c-158-46-46-63.ngrok-free.app/web/')))
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!",
                         reply_markup=markup.as_markup())
