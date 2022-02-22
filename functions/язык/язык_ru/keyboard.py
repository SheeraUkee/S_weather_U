from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from functions.язык.язык_ru.text import text
lang = InlineKeyboardMarkup()
lang.insert(InlineKeyboardButton(text=text[0], callback_data="ru"))
lang.insert(InlineKeyboardButton(text=text[1], callback_data="en"))