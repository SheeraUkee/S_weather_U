from aiogram import types, Dispatcher

from config import bot, dp
from functions.язык.язык_ru.keyboard import lang
from functions.язык.язык_ru.text import lang_text


@dp.callback_query_handler(text="язык")
async def call_lang1(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, lang_text[0], reply_markup=lang)


def register_message_handler_call_lang1(dp: Dispatcher):
    dp.register_message_handler(call_lang1)
