from aiogram import types, Dispatcher

from config import bot, dp
from functions.язык.комманда_стар_1_en.keyboard import menu
from functions.язык.комманда_стар_1_en.text import start_text


@dp.callback_query_handler(text="en")
async def en_start(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, start_text[0], reply_markup=menu)


def register_message_handler_en_start(dp: Dispatcher):
    dp.register_message_handler(en_start)
