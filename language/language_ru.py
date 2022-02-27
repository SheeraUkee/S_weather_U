from aiogram import Dispatcher, types
from data_config import dp, bot

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb2 = InlineKeyboardMarkup()
kb2.insert(InlineKeyboardButton(text="Английский", callback_data="en1"))
kb2.insert(InlineKeyboardButton(text="Русский", callback_data="back111"))


@dp.callback_query_handler(text="lang1")
async def language_ru(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Выберите язак", reply_markup=kb2)



def register_chosen_inline_handler_language_ru(dp: Dispatcher):
    dp.register_chosen_inline_handler(language_ru)