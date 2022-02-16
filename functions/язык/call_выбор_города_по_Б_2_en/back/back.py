from aiogram import types, Dispatcher

from config import bot, dp
from functions.язык.call_выбор_города_по_Б_2_en.back.text import start_text
from functions.язык.call_выбор_города_по_Б_2_en.back.keyboard import menu1
@dp.callback_query_handler(text="back1")
async def call_dark_en(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, start_text[0], reply_markup=menu1)


def register_message_handler_call_dark_en(dp: Dispatcher):
    dp.register_message_handler(call_dark_en)