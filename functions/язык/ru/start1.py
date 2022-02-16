from aiogram import types, Dispatcher

from config import bot, dp
from functions.комманда_стар_1.text import start_text
from functions.комманда_стар_1.keyboard import menu

@dp.callback_query_handler(text="ru")
async def command_start1(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, start_text[0], reply_markup=menu)


def register_message_handler_command_start1(dp: Dispatcher):
    dp.register_message_handler(command_start1)