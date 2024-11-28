import asyncio
import logging
import sys
from tg_module import secret
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, types
from aiogram.types import inline_keyboard_markup, inline_keyboard_button
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart


dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    web_app_url = "https://stars-start.ru/webapp"
    btn_1 = inline_keyboard_button.InlineKeyboardButton(text="🌐 Открыть приложение",
                                                        web_app=types.WebAppInfo(url=web_app_url))
    keyboard = inline_keyboard_markup.InlineKeyboardMarkup(inline_keyboard=[[btn_1]])
    await message.answer("Нажмите, чтобы открыть мини-приложение:", reply_markup=keyboard)


@dp.message()
async def message_handler(message: types.Message):
    pass


async def main() -> None:
    bot = Bot(token=secret.tg_token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

