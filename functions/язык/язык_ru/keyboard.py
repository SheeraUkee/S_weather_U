from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from functions.язык.язык_ru.text import text
lang = InlineKeyboardMarkup()
lang.insert(InlineKeyboardButton(text=text[0], callback_data="ru"))
lang.insert(InlineKeyboardButton(text=text[1], callback_data="en"))
lang.insert(InlineKeyboardButton(text=text[2], callback_data="АЗБУКА_МОРЗЕ"))