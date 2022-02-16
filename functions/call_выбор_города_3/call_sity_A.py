from aiogram import types, Dispatcher

from config import bot, dp
from functions.call_выбор_города_3.text import text
from functions.call_выбор_города_3.keyboard import sity_kz_A, sity_kz_Б, sity_kz_Д, sity_kz_Е, \
    sity_kz_Ж, sity_kz_З, sity_kz_К, sity_kz_Л, sity_kz_М, sity_kz_Н, sity_kz_П, sity_kz_Р, \
    sity_kz_С, sity_kz_Т, sity_kz_У, sity_kz_Ф, sity_kz_Х, sity_kz_Ш, sity_kz_Щ, sity_kz_Э

# 1. Ответ на кнопку А
@dp.callback_query_handler(text="А")
async def call_А_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_A)


# 2. Ответ на кнопку Б
@dp.callback_query_handler(text="Б")
async def call_Б_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Б)


# 3. Ответ на кнопку Д
@dp.callback_query_handler(text="Д")
async def call_Д_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Д)


# 3. Ответ на кнопку Е
@dp.callback_query_handler(text="Е")
async def call_Е_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Е)


# 4. Ответ на кнопку Ж
@dp.callback_query_handler(text="Ж")
async def call_Ж_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Ж)


# 5. Ответ на кнопку З
@dp.callback_query_handler(text="З")
async def call_З_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_З)


# 6. Ответ на кнопку К
@dp.callback_query_handler(text="К")
async def call_К_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_К)


# 7. Ответ на кнопку Л
@dp.callback_query_handler(text="Л")
async def call_Л_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Л)


# 8. Ответ на кнопку М
@dp.callback_query_handler(text="М")
async def call_М_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_М)


# 9. Ответ на кнопку Н
@dp.callback_query_handler(text="Н")
async def call_Н_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Н)


# 10. Ответ на кнопку П
@dp.callback_query_handler(text="П")
async def call_П_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_П)


# 11. Ответ на кнопку Р
@dp.callback_query_handler(text="Р")
async def call_Р_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Р)


# 12. Ответ на кнопку С
@dp.callback_query_handler(text="С")
async def call_С_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_С)


# 13. Ответ на кнопку Т
@dp.callback_query_handler(text="Т")
async def call_Т_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Т)


# 14. Ответ на кнопку У
@dp.callback_query_handler(text="У")
async def call_У_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_У)


# 15. Ответ на кнопку Ф
@dp.callback_query_handler(text="Ф")
async def call_Ф_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Ф)


# 16. Ответ на кнопку Х
@dp.callback_query_handler(text="Х")
async def call_Х_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Х)


# 17. Ответ на кнопку Ш
@dp.callback_query_handler(text="Ш")
async def call_Ш_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Ш)


# 18. Ответ на кнопку Щ
@dp.callback_query_handler(text="Щ")
async def call_Щ_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Щ)


# 19. Ответ на кнопку Э
@dp.callback_query_handler(text="Э")
async def call_Э_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Э)


def register_message_handler_call_ABC_sity(dp: Dispatcher):
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
    dp.register_message_handler(call_Ф_sity)
    dp.register_message_handler(call_Х_sity)
    dp.register_message_handler(call_Ш_sity)
    dp.register_message_handler(call_Щ_sity)
    dp.register_message_handler(call_Э_sity)