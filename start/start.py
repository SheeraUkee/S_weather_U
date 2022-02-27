from aiogram import types, Dispatcher

from data_config import bot, dp


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
kb_text = ["Кейсы городов 🌇🌆", "АЗБУКА МОРЗЕ", "Язык телеграм бота 🌐"]

menu = InlineKeyboardMarkup()
menu.add(InlineKeyboardButton(text=kb_text[0], callback_data="кейсы_1"))
menu.add(InlineKeyboardButton(text=kb_text[1], callback_data="АЗБУКА_МОРЗЕ_2"))
menu.add(InlineKeyboardButton(text=kb_text[2], callback_data="lang1"))


text = ["Бот активирован, меню открыто."]
@dp.message_handler(commands=["start"])
async def command_start1(message: types.Message):
    await bot.send_message(message.from_user.id, text[0], reply_markup=menu)
    await message.delete()


def register_message_handler_command_start1(dp: Dispatcher):
    dp.register_message_handler(command_start1)