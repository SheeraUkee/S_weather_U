from aiogram import types, Dispatcher

from data_config import bot, dp
kb_text = ["Кейсы городов 🌇🌆","АЗБУКА МОРЗЕ", "Язык телеграм бота 🌐"]


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
menu = InlineKeyboardMarkup()
menu.add(InlineKeyboardButton(text=kb_text[0], callback_data="кейсы_1"))
menu.add(InlineKeyboardButton(text=kb_text[1], callback_data="АЗБУКА_МОРЗЕ_2"))
menu.add(InlineKeyboardButton(text=kb_text[2], callback_data="lang1"))
start_text = ["Бот активирован, меню открыто."]


@dp.callback_query_handler(text="back111")
async def call_dark(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, start_text[0], reply_markup=menu)


def register_message_handler_call_dark(dp: Dispatcher):
    dp.register_message_handler(call_dark)