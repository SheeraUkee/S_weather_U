from aiogram import types, Dispatcher

from data_config import bot, dp


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
text = ["Назад"]


sity_abc = InlineKeyboardMarkup()
# кнопка А
sity_abc.insert(InlineKeyboardButton(text="А", callback_data="А_m"))
# кнопка Б
sity_abc.insert(InlineKeyboardButton(text="Б", callback_data="Б_m"))
# кнопка Д
sity_abc.insert(InlineKeyboardButton(text="Д", callback_data="Д_m"))
# кнопка Е
sity_abc.insert(InlineKeyboardButton(text="Е", callback_data="Е_m"))
# кнопка Ж
sity_abc.insert(InlineKeyboardButton(text="Ж", callback_data="Ж_m"))
# кнопка З
sity_abc.insert(InlineKeyboardButton(text="З", callback_data="З_m"))
# кнопка К
sity_abc.insert(InlineKeyboardButton(text="К", callback_data="К_m"))
# кнопка Л
sity_abc.insert(InlineKeyboardButton(text="Л", callback_data="Л_m"))
# кнопка М
sity_abc.insert(InlineKeyboardButton(text="М", callback_data="М_m"))
# кнопка Н
sity_abc.insert(InlineKeyboardButton(text="Н", callback_data="Н_m"))
# кнопка П
sity_abc.insert(InlineKeyboardButton(text="П", callback_data="П_m"))
# кнопка Р
sity_abc.insert(InlineKeyboardButton(text="Р", callback_data="Р_m"))
# кнопка С
sity_abc.insert(InlineKeyboardButton(text="С", callback_data="С_m"))
# кнопка Т
sity_abc.insert(InlineKeyboardButton(text="Т", callback_data="Т_m"))
# кнопка У
sity_abc.insert(InlineKeyboardButton(text="У", callback_data="У_m"))
# кнопка Ф
sity_abc.insert(InlineKeyboardButton(text="Ф", callback_data="Ф_m"))
# кнопка Х
sity_abc.insert(InlineKeyboardButton(text="Х", callback_data="Х_m"))
# кнопка Ш
sity_abc.insert(InlineKeyboardButton(text="Ш", callback_data="Ш_m"))
# кнопка Щ
sity_abc.insert(InlineKeyboardButton(text="Щ", callback_data="Щ_m"))
# кнопка Э
sity_abc.insert(InlineKeyboardButton(text="Э", callback_data="Э_m"))
#  кнопка вернуться назад
sity_abc.add(InlineKeyboardButton(text="Назад", callback_data="back_M"))
text = ["Выборите кейс города."]


@dp.callback_query_handler(text="АЗБУКА_МОРЗЕ_2")
async def call_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_abc)


def register_message_handler_call_sity_M(dp: Dispatcher):
    dp.register_message_handler(call_sity)