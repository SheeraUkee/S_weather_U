from aiogram import types, Dispatcher

from data_config import bot, dp


@dp.callback_query_handler(text="deleter1")
async def call_delet1(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)


def register_message_handler_call_delet_open111(dp: Dispatcher):
    dp.register_message_handler(call_delet1)