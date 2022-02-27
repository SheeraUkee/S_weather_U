from aiogram import types, Dispatcher

from data_config import bot, dp


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
text = ["Back"]

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

sity_abc.add(InlineKeyboardButton(text=text[0], callback_data="en1"))
text = ["Select the case of the city."]


@dp.callback_query_handler(text="кейсы_11")
async def call_sity_2(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_abc)


def register_message_handler_call_sity_2en(dp: Dispatcher):
    dp.register_message_handler(call_sity_2)