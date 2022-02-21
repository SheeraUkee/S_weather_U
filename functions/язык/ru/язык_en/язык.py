from aiogram import types, Dispatcher

from config import bot, dp
from functions.язык.ru.язык_en.keyboard import lang
from functions.язык.ru.язык_en.text import lang_text


@dp.callback_query_handler(text="language1")
async def call_lang_en(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, lang_text[0], reply_markup=lang)


def register_message_handler_call_lang_en(dp: Dispatcher):
    dp.register_message_handler(call_lang_en)
