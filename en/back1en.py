from aiogram import types, Dispatcher

from data_config import bot, dp
kb_text = ["City Cases 🌇 🌆 ", "Bot Telegram Language 🌐 "]


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
menu = InlineKeyboardMarkup()
menu.add(InlineKeyboardButton(text=kb_text[0], callback_data="кейсы_11"))
menu.add(InlineKeyboardButton(text=kb_text[1], callback_data="lang2"))
start_text = ["The bot is activated, the menu is open."]


@dp.callback_query_handler(text="en1")
async def call_dark(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, start_text[0], reply_markup=menu)


def register_message_handler_call_dark_en(dp: Dispatcher):
    dp.register_message_handler(call_dark)