from aiogram import types, Dispatcher

from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dp.callback_query_handler(text="back")
async def morze_ABC(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Выберите город казахстана")


def register_message_handler_morze_ABC(dp: Dispatcher):
    dp.register_message_handler(morze_ABC)