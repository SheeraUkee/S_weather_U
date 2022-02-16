from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from functions.язык.комманда_стар_1_en.kb_text import kb_text

menu = InlineKeyboardMarkup()
menu.insert(InlineKeyboardButton(text=kb_text[0], callback_data="cases"))
menu.insert(InlineKeyboardButton(text=kb_text[1], callback_data="customization"))
menu.insert(InlineKeyboardButton(text=kb_text[2], callback_data="language1"))
