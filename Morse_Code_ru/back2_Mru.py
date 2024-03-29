from aiogram import types, Dispatcher

from data_config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
text = ["Назад"]


sity_abc = InlineKeyboardMarkup()
# кнопка А
sity_abc.insert(InlineKeyboardButton(text="А", callback_data="А"))
# кнопка Б
sity_abc.insert(InlineKeyboardButton(text="Б", callback_data="Б"))
# кнопка Д
sity_abc.insert(InlineKeyboardButton(text="Д", callback_data="Д"))
# кнопка Е
sity_abc.insert(InlineKeyboardButton(text="Е", callback_data="Е"))
# кнопка Ж
sity_abc.insert(InlineKeyboardButton(text="Ж", callback_data="Ж"))
# кнопка З
sity_abc.insert(InlineKeyboardButton(text="З", callback_data="З"))
# кнопка К
sity_abc.insert(InlineKeyboardButton(text="К", callback_data="К"))
# кнопка Л
sity_abc.insert(InlineKeyboardButton(text="Л", callback_data="Л"))
# кнопка М
sity_abc.insert(InlineKeyboardButton(text="М", callback_data="М"))
# кнопка Н
sity_abc.insert(InlineKeyboardButton(text="Н", callback_data="Н"))
# кнопка П
sity_abc.insert(InlineKeyboardButton(text="П", callback_data="П"))
# кнопка Р
sity_abc.insert(InlineKeyboardButton(text="Р", callback_data="Р"))
# кнопка С
sity_abc.insert(InlineKeyboardButton(text="С", callback_data="С"))
# кнопка Т
sity_abc.insert(InlineKeyboardButton(text="Т", callback_data="Т"))
# кнопка У
sity_abc.insert(InlineKeyboardButton(text="У", callback_data="У"))
# кнопка Ф
sity_abc.insert(InlineKeyboardButton(text="Ф", callback_data="Ф"))
# кнопка Х
sity_abc.insert(InlineKeyboardButton(text="Х", callback_data="Х"))
# кнопка Ш
sity_abc.insert(InlineKeyboardButton(text="Ш", callback_data="Ш"))
# кнопка Щ
sity_abc.insert(InlineKeyboardButton(text="Щ", callback_data="Щ"))
# кнопка Э
sity_abc.insert(InlineKeyboardButton(text="Э", callback_data="Э"))
#  кнопка вернуться назад
sity_abc.add(InlineKeyboardButton(text=text[0], callback_data="back_M"))
text = ["Выборите кейс города."]


@dp.callback_query_handler(text="call_sity_1_M")
async def call_sity_1(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_abc)


def register_message_handler_call_sity_1_M(dp: Dispatcher):
    dp.register_message_handler(call_sity_1)