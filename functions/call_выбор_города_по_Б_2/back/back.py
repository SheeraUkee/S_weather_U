from aiogram import types, Dispatcher

from config import bot, dp
from functions.комманда_стар_1.text import start_text
from functions.комманда_стар_1.keyboard import menu
@dp.callback_query_handler(text="back")
async def call_dark(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, start_text[0], reply_markup=menu)


def register_message_handler_call_dark(dp: Dispatcher):
    dp.register_message_handler(call_dark)