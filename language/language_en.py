from aiogram import Dispatcher, types
from data_config import dp, bot

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb1 = InlineKeyboardMarkup()
kb1.insert(InlineKeyboardButton(text="en", callback_data="en1"))
kb1.insert(InlineKeyboardButton(text="ru", callback_data="back111"))


@dp.callback_query_handler(text="lang2")
async def language_en(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Select a language", reply_markup=kb1)



def register_chosen_inline_handler_language_en(dp: Dispatcher):
    dp.register_chosen_inline_handler(language_en)