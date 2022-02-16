from aiogram import types, Dispatcher

from config import bot, dp
from functions.call_выбор_города_3.text import text
from functions.язык.call_выбор_города.keyboard import sity_kz_A, sity_kz_Б, sity_kz_Д, sity_kz_Е, \
    sity_kz_Ж, sity_kz_З, sity_kz_К, sity_kz_Л, sity_kz_М, sity_kz_Н, sity_kz_П, sity_kz_Р, \
    sity_kz_С, sity_kz_Т, sity_kz_У

# 1. Ответ на кнопку А
@dp.callback_query_handler(text="A")
async def call_А_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_A)


# 2. Ответ на кнопку Б
@dp.callback_query_handler(text="B")
async def call_Б_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Б)


# 3. Ответ на кнопку Д
@dp.callback_query_handler(text="C")
async def call_Д_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Д)


# 3. Ответ на кнопку Е
@dp.callback_query_handler(text="D")
async def call_Е_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Е)


# 4. Ответ на кнопку Ж
@dp.callback_query_handler(text="E")
async def call_Ж_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Ж)


# 5. Ответ на кнопку З
@dp.callback_query_handler(text="F")
async def call_З_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_З)


# 6. Ответ на кнопку К
@dp.callback_query_handler(text="K")
async def call_К_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_К)


# 7. Ответ на кнопку Л
@dp.callback_query_handler(text="L")
async def call_Л_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Л)


# 8. Ответ на кнопку М
@dp.callback_query_handler(text="M")
async def call_М_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_М)


# 9. Ответ на кнопку Н
@dp.callback_query_handler(text="N")
async def call_Н_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Н)


# 10. Ответ на кнопку П
@dp.callback_query_handler(text="P")
async def call_П_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_П)


# 11. Ответ на кнопку Р
@dp.callback_query_handler(text="R")
async def call_Р_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Р)


# 12. Ответ на кнопку С
@dp.callback_query_handler(text="S")
async def call_С_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_С)


# 13. Ответ на кнопку Т
@dp.callback_query_handler(text="T")
async def call_Т_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Т)


# 14. Ответ на кнопку У
@dp.callback_query_handler(text="Z")
async def call_У_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_У)


def register_message_handler_call_ABC_sity_en(dp: Dispatcher):
    dp.register_message_handler(call_А_sity)
    dp.register_message_handler(call_Б_sity)
    dp.register_message_handler(call_Д_sity)
    dp.register_message_handler(call_Е_sity)
    dp.register_message_handler(call_Ж_sity)
    dp.register_message_handler(call_З_sity)
    dp.register_message_handler(call_К_sity)
    dp.register_message_handler(call_Л_sity)
    dp.register_message_handler(call_М_sity)
    dp.register_message_handler(call_Н_sity)
    dp.register_message_handler(call_П_sity)
    dp.register_message_handler(call_Р_sity)
    dp.register_message_handler(call_С_sity)
    dp.register_message_handler(call_Т_sity)
    dp.register_message_handler(call_У_sity)
