from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from functions.язык.call_выбор_города_по_Б_2_en.kb_text import text

sity_abc = InlineKeyboardMarkup()
sity_abc.insert(InlineKeyboardButton(text="A", callback_data="A"))
sity_abc.insert(InlineKeyboardButton(text="B", callback_data="B"))
sity_abc.insert(InlineKeyboardButton(text="C", callback_data="C"))
sity_abc.insert(InlineKeyboardButton(text="D", callback_data="D"))
sity_abc.insert(InlineKeyboardButton(text="E", callback_data="E"))
sity_abc.insert(InlineKeyboardButton(text="F", callback_data="F"))
sity_abc.insert(InlineKeyboardButton(text="K", callback_data="K"))
sity_abc.insert(InlineKeyboardButton(text="L", callback_data="L"))
sity_abc.insert(InlineKeyboardButton(text="M", callback_data="M"))
sity_abc.insert(InlineKeyboardButton(text="N", callback_data="N"))
sity_abc.insert(InlineKeyboardButton(text="P", callback_data="P"))
sity_abc.insert(InlineKeyboardButton(text="R", callback_data="R"))
sity_abc.insert(InlineKeyboardButton(text="S", callback_data="S"))
sity_abc.insert(InlineKeyboardButton(text="T", callback_data="T"))
sity_abc.insert(InlineKeyboardButton(text="Z", callback_data="Z"))

sity_abc.add(InlineKeyboardButton(text=text[0], callback_data="back1"))