from aiogram import types, Dispatcher

from data_config import bot, dp


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
text = ["Назад"]


sity_abc = InlineKeyboardMarkup()
sity_abc.insert(InlineKeyboardButton(text="А", callback_data="А"))
sity_abc.insert(InlineKeyboardButton(text="Б", callback_data="Б"))
sity_abc.insert(InlineKeyboardButton(text="Д", callback_data="Д"))
sity_abc.insert(InlineKeyboardButton(text="Е", callback_data="Е"))
sity_abc.insert(InlineKeyboardButton(text="Ж", callback_data="Ж"))
sity_abc.insert(InlineKeyboardButton(text="З", callback_data="З"))
sity_abc.insert(InlineKeyboardButton(text="К", callback_data="К"))
sity_abc.insert(InlineKeyboardButton(text="Л", callback_data="Л"))
sity_abc.insert(InlineKeyboardButton(text="М", callback_data="М"))
sity_abc.insert(InlineKeyboardButton(text="Н", callback_data="Н"))
sity_abc.insert(InlineKeyboardButton(text="П", callback_data="П"))
sity_abc.insert(InlineKeyboardButton(text="Р", callback_data="Р"))
sity_abc.insert(InlineKeyboardButton(text="С", callback_data="С"))
sity_abc.insert(InlineKeyboardButton(text="Т", callback_data="Т"))
sity_abc.insert(InlineKeyboardButton(text="У", callback_data="У"))
sity_abc.insert(InlineKeyboardButton(text="Ф", callback_data="Ф"))
sity_abc.insert(InlineKeyboardButton(text="Х", callback_data="Х"))
sity_abc.insert(InlineKeyboardButton(text="Ш", callback_data="Ш"))
sity_abc.insert(InlineKeyboardButton(text="Щ", callback_data="Щ"))
sity_abc.insert(InlineKeyboardButton(text="Э", callback_data="Э"))
sity_abc.add(InlineKeyboardButton(text=text[0], callback_data="back111"))
text = ["Выборите кейс города."]


@dp.callback_query_handler(text="кейсы_1")
async def call_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_abc)


def register_message_handler_call_sity(dp: Dispatcher):
    dp.register_message_handler(call_sity)