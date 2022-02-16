from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from functions.язык.call_выбор_города_по_Б_2_en.back.text_keyboart import kb_text
menu1 = InlineKeyboardMarkup()
menu1.insert(InlineKeyboardButton(text=kb_text[0], callback_data="cases"))
menu1.insert(InlineKeyboardButton(text=kb_text[1], callback_data="customization"))
menu1.insert(InlineKeyboardButton(text=kb_text[2], callback_data="language1"))

