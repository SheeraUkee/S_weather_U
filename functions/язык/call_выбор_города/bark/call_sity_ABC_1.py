from aiogram import types, Dispatcher

from config import bot, dp
from functions.язык.call_выбор_города.bark.text import text
from functions.язык.call_выбор_города.bark.keyboard import sity_abc

@dp.callback_query_handler(text="call_sity_1_en")
async def call_sity_1_en(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_abc)


def register_message_handler_call_sity_1_en(dp: Dispatcher):
    dp.register_message_handler(call_sity_1_en)