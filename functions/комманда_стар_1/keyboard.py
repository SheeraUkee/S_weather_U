from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from functions.комманда_стар_1.text_keyboart import kb_text
menu = InlineKeyboardMarkup()
menu.insert(InlineKeyboardButton(text=kb_text[0], callback_data="кейсы"))
menu.insert(InlineKeyboardButton(text=kb_text[1], callback_data="АЗБУКА_МОРЗЕ"))
menu.insert(InlineKeyboardButton(text=kb_text[2], callback_data="язык"))

