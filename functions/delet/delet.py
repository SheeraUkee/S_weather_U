from aiogram import types, Dispatcher

from config import bot, dp


@dp.callback_query_handler(text="delet")
async def call_delet(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)


def register_message_handler_call_delet_open(dp: Dispatcher):
    dp.register_message_handler(call_delet)