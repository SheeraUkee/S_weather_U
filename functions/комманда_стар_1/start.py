from aiogram import types, Dispatcher

from config import bot, dp
from functions.комманда_стар_1.text import start_text
from functions.комманда_стар_1.keyboard import menu
@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, start_text[0], reply_markup=menu)
    await message.delete()


def register_message_handler_command_start(dp: Dispatcher):
    dp.register_message_handler(command_start)