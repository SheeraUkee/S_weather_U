from aiogram import types, Dispatcher

from data_config import bot, dp
sity = [
    [
        "Abay",
        "Akkol",
        "Aksay",
        "Aksu",
        "Aktau",
        "Aktobe",
        "Alga",
        "Almaty",
        "Aralsk",
        "Arkalyk",
        "Arys",
        "Atbasar",
        "Atyrau",
        "Ayagoz"
    ],
    [
        "Baikonur ",
        "Balkhash",
        "Bulayevo"
    ],
    [
        "Derzhavinsk"
    ],
    [
        "Ereymentau",
        "Esik",
        "Esil",
        "Ekibastuz",
        "Emba"
    ],
    [
        "Zhanaozen",
        "Zhanatas",
        "Zharkent",
        "Zhezkazgan",
        "Zhem",
        "Zhetisay",
        "Zhetikara"
    ],
    [
        "Zaisan",
        "Zyryanovsk"
    ],
    [
        "Kazalinsk",
        "Kandyagash",
        "Kapshagai",
        "Karaganda",
        "Karazhal",
        "Karatau",
        "Karkaralinsk",
        "Kentau",
        "Kokshetau",
        "Kostanay",
        "Kurchatov",
        "Kurchatov",
        "Khromtau"
    ],
    [
        "Lenger",
        "Lisakovsk"
    ],
    [
        "Makinsk",
        "Mamlyutka"
    ],
    [
        "Нур-Султан"
    ],
    [
        "Pavlodar",
        "Petropavlovsk",
        "Priozersk"
    ],
    [
        "Ridder",
        "Rudny"
    ],
    [
        "Saran",
        "Sarkand",
        "Saryagash",
        "Satpayev",
        "Semey",
        "Sergeyevka",
        "Serebryansk",
        "Stepnogorsk",
        "Stepnyak"
    ],
    [
        "Taiynsha",
        "Talgar",
        "Taldykorgan",
        "Taraz",
        "Tekeli",
        "Temir",
        "Temirtau",
        "Turkestan"
    ],
    [
        "Uralsk",
        "Ust-Kamenogorsk",
        "Usharal",
        "Ushtobe"
    ],
    [
        "Charsk"
    ],
    [
        "Shalkar",
        "Shardara",
        "Shakhtinsk",
        "Shemonaikha",
        "Shu",
        "Shymkent",
        "Shchuchinsk"
    ],
]
bark = ["Bark"]


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

sity_kz_A = InlineKeyboardMarkup()

sity_kz_A.insert(InlineKeyboardButton(text=sity[0][0], callback_data=sity[0][0]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][1], callback_data=sity[0][1]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][2], callback_data=sity[0][2]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][3], callback_data=sity[0][3]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][4], callback_data=sity[0][4]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][5], callback_data=sity[0][5]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][6], callback_data=sity[0][6]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][7], callback_data=sity[0][7]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][8], callback_data=sity[0][8]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][9], callback_data=sity[0][9]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][10], callback_data=sity[0][10]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][11], callback_data=sity[0][11]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][12], callback_data=sity[0][12]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][13], callback_data=sity[0][13]))
sity_kz_A.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_Б = InlineKeyboardMarkup()
sity_kz_Б.insert(InlineKeyboardButton(text=sity[1][0], callback_data=sity[1][0]))
sity_kz_Б.insert(InlineKeyboardButton(text=sity[1][1], callback_data=sity[1][1]))
sity_kz_Б.insert(InlineKeyboardButton(text=sity[1][2], callback_data=sity[1][2]))
#  кнопка вернуться назад
sity_kz_Б.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_Д = InlineKeyboardMarkup()
sity_kz_Д.insert(InlineKeyboardButton(text=sity[2][0], callback_data=sity[2][0]))
sity_kz_Д.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_Е = InlineKeyboardMarkup()
sity_kz_Е.insert(InlineKeyboardButton(text=sity[3][0], callback_data=sity[3][0]))
sity_kz_Е.insert(InlineKeyboardButton(text=sity[3][1], callback_data=sity[3][1]))
sity_kz_Е.insert(InlineKeyboardButton(text=sity[3][2], callback_data=sity[3][2]))
sity_kz_Е.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_Ж = InlineKeyboardMarkup()
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][0], callback_data=sity[4][0]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][1], callback_data=sity[4][1]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][2], callback_data=sity[4][2]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][3], callback_data=sity[4][3]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][4], callback_data=sity[4][4]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][5], callback_data=sity[4][5]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][6], callback_data=sity[4][6]))
#  кнопка вернуться назад
sity_kz_Ж.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_З = InlineKeyboardMarkup()
sity_kz_З.insert(InlineKeyboardButton(text=sity[5][0], callback_data=sity[5][0]))
sity_kz_З.insert(InlineKeyboardButton(text=sity[5][1], callback_data=sity[5][1]))
#  кнопка вернуться назад
sity_kz_З.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_К = InlineKeyboardMarkup()
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][0], callback_data=sity[6][0]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][1], callback_data=sity[6][1]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][2], callback_data=sity[6][2]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][3], callback_data=sity[6][3]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][4], callback_data=sity[6][4]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][5], callback_data=sity[6][5]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][6], callback_data=sity[6][6]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][7], callback_data=sity[6][7]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][8], callback_data=sity[6][8]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][9], callback_data=sity[6][9]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][10], callback_data=sity[6][10]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][11], callback_data=sity[6][11]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][12], callback_data=sity[6][12]))
#  кнопка вернуться назад
sity_kz_К.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_Л = InlineKeyboardMarkup()
sity_kz_Л.insert(InlineKeyboardButton(text=sity[7][0], callback_data=sity[7][0]))
sity_kz_Л.insert(InlineKeyboardButton(text=sity[7][1], callback_data=sity[7][1]))
#  кнопка вернуться назад
sity_kz_Л.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_М = InlineKeyboardMarkup()
sity_kz_М.insert(InlineKeyboardButton(text=sity[8][0], callback_data=sity[8][0]))
sity_kz_М.insert(InlineKeyboardButton(text=sity[8][1], callback_data=sity[8][1]))
#  кнопка вернуться назад
sity_kz_М.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_Н = InlineKeyboardMarkup()
sity_kz_Н.insert(InlineKeyboardButton(text=sity[9][0], callback_data=sity[9][0]))
#  кнопка вернуться назад
sity_kz_Н.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_П = InlineKeyboardMarkup()
sity_kz_П.insert(InlineKeyboardButton(text=sity[10][0], callback_data=sity[10][0]))
sity_kz_П.insert(InlineKeyboardButton(text=sity[10][1], callback_data=sity[10][1]))
sity_kz_П.insert(InlineKeyboardButton(text=sity[10][2], callback_data=sity[10][2]))
#  кнопка вернуться назад
sity_kz_П.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_Р = InlineKeyboardMarkup()
sity_kz_Р.insert(InlineKeyboardButton(text=sity[11][0], callback_data=sity[11][0]))
sity_kz_Р.insert(InlineKeyboardButton(text=sity[11][1], callback_data=sity[11][1]))
#  кнопка вернуться назад
sity_kz_Р.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_С = InlineKeyboardMarkup()
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][0], callback_data=sity[12][0]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][1], callback_data=sity[12][1]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][2], callback_data=sity[12][2]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][3], callback_data=sity[12][3]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][4], callback_data=sity[12][4]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][5], callback_data=sity[12][5]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][6], callback_data=sity[12][6]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][7], callback_data=sity[12][7]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][8], callback_data=sity[12][8]))
#  кнопка вернуться назад
sity_kz_С.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_Т = InlineKeyboardMarkup()
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][0], callback_data=sity[13][0]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][1], callback_data=sity[13][1]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][2], callback_data=sity[13][2]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][3], callback_data=sity[13][3]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][4], callback_data=sity[13][4]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][5], callback_data=sity[13][5]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][6], callback_data=sity[13][6]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][7], callback_data=sity[13][7]))
#  кнопка вернуться назад
sity_kz_Т.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_У = InlineKeyboardMarkup()
sity_kz_У.insert(InlineKeyboardButton(text=sity[14][0], callback_data=sity[14][0]))
sity_kz_У.insert(InlineKeyboardButton(text=sity[14][1], callback_data=sity[14][1]))
sity_kz_У.insert(InlineKeyboardButton(text=sity[14][2], callback_data=sity[14][2]))
sity_kz_У.insert(InlineKeyboardButton(text=sity[14][3], callback_data=sity[14][3]))
#  кнопка вернуться назад
sity_kz_У.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_Ф = InlineKeyboardMarkup()
sity_kz_Ф.insert(InlineKeyboardButton(text=sity[15][0], callback_data=sity[15][0]))
#  кнопка вернуться назад
sity_kz_Ф.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))


sity_kz_Х = InlineKeyboardMarkup()
sity_kz_Х.insert(InlineKeyboardButton(text=sity[16][0], callback_data=sity[16][0]))
#  кнопка вернуться назад
sity_kz_Х.add(InlineKeyboardButton(text=bark[0], callback_data="кейсы_3"))
text = ["Select the case of the city."]


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