from aiogram import types, Dispatcher

from config import bot, dp
from functions.call_выбор_города_3.text import text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
sity_M = [
    [
        "Абай_M",
        "Акколь_M",
        "Аксай_M",
        "Аксу_M",
        "Актау_M",
        "Актобе_M",
        "Алга_M",
        "Алматы_M",
        "Алтай_M",
        "Аральск_M",
        "Аркалык_M",
        "Арыс_M",
        "Атбасар_M",
        "Атырау_M",
        "Аягоз_M"
    ],
    [
        "Байконур_M",
        "Балхаш_M",
        "Булаево_M"
    ],
    [
        "Державинск_M"
    ],
    [
        "Ерейментау_M",
        "Есик_M",
        "Есиль_M"
    ],
    [
        "Жанаозен_M",
        "Жанатас_M",
        "Жаркент_M",
        "Жезказган_M",
        "Жем_M",
        "Жетысай_M",
        "Житикара_M"
    ],
    [
        "Зайсан_M",
        "Зыряновск_M"
    ],
    [
        "Кызылорда_M",
        "Кандыагаш_M",
        "Капшагай_M",
        "Караганды_M",
        "Каражал_M",
        "Каратау_M",
        "Каркаралинск_M",
        "Каскелен_M",
        "Кентау_M",
        "Кокшетау_M",
        "Костанай_M",
        "Кулсары_M",
        "Курчатов_M"
    ],
    [
        "Ленгер_M",
        "Лисаковск_M"
    ],
    [
        "Макинск_M",
        "Мамлютка_M"
    ],
    [
        "Нур-Султан_M"
    ],
    [
        "Павлодар_M",
        "Петропавловск_M",
        "Приозёрск_M"
    ],
    [
        "Риддер_M",
        "Рудный_M"
    ],
    [
        "Сарань_M",
        "Сарканд_M",
        "Сарыагаш_M",
        "Сатпаев_M",
        "Семей_M",
        "Сергеевка_M",
        "Серебрянск_M",
        "Степногорск_M",
        "Степняк_M"
    ],
    [
        "Тайынша_M",
        "Талгар_M",
        "Талдыкорган_M",
        "Тараз_M",
        "Текели_M",
        "Темир_M",
        "Темиртау_M",
        "Туркестан_M"
    ],
    [
        "Уральск_M",
        "Усть-Каменогорск_M",
        "Ушарал_M",
        "Уштобе_M"
    ],
    [
        "Форт-Шевченко_M"
    ],
    [
        "Хромтау_M"
    ],
    [
        "Шалкар_M",
        "Шар_M",
        "Шардара_M",
        "Шахтинск_M",
        "Шемонаиха_M",
        "Шу_M",
        "Шымкент_M"
    ],
    [
        "Щучинск_M"
    ],
    [
        "Экибастуз_M",
        "Эмба_M"
    ]
]

bark = ["Назад"]
sity = [
    [
        "Абай",
        "Акколь",
        "Аксай",
        "Аксу",
        "Актау",
        "Актобе",
        "Алга",
        "Алматы",
        "Алтай",
        "Аральск",
        "Аркалык",
        "Арыс",
        "Атбасар",
        "Атырау",
        "Аягоз"
    ],
    [
        "Байконур",
        "Балхаш",
        "Булаево"
    ],
    [
        "Державинск"
    ],
    [
        "Ерейментау",
        "Есик",
        "Есиль"
    ],
    [
        "Жанаозен",
        "Жанатас",
        "Жаркент",
        "Жезказган",
        "Жем",
        "Жетысай",
        "Житикара"
    ],
    [
        "Зайсан",
        "Зыряновск"
    ],
    [
        "Кызылорда",
        "Кандыагаш",
        "Капшагай",
        "Караганды",
        "Каражал",
        "Каратау",
        "Каркаралинск",
        "Каскелен",
        "Кентау",
        "Кокшетау",
        "Костанай",
        "Кулсары",
        "Курчатов"
    ],
    [
        "Ленгер",
        "Лисаковск"
    ],
    [
        "Макинск",
        "Мамлютка"
    ],
    [
        "Нур-Султан"
    ],
    [
        "Павлодар",
        "Петропавловск",
        "Приозёрск"
    ],
    [
        "Риддер",
        "Рудный"
    ],
    [
        "Сарань",
        "Сарканд",
        "Сарыагаш",
        "Сатпаев",
        "Семей",
        "Сергеевка",
        "Серебрянск",
        "Степногорск",
        "Степняк"
    ],
    [
        "Тайынша",
        "Талгар",
        "Талдыкорган",
        "Тараз",
        "Текели",
        "Темир",
        "Темиртау",
        "Туркестан"
    ],
    [
        "Уральск",
        "Усть-Каменогорск",
        "Ушарал",
        "Уштобе"
    ],
    [
        "Форт-Шевченко"
    ],
    [
        "Хромтау"
    ],
    [
        "Шалкар",
        "Шар",
        "Шардара",
        "Шахтинск",
        "Шемонаиха",
        "Шу",
        "Шымкент"
    ],
    [
        "Щучинск"
    ],
    [
        "Экибастуз",
        "Эмба"
    ]
]

sity_kz_A = InlineKeyboardMarkup()
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][0], callback_data=sity_M[0][0]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][1], callback_data=sity_M[0][1]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][2], callback_data=sity_M[0][2]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][3], callback_data=sity_M[0][3]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][4], callback_data=sity_M[0][4]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][5], callback_data=sity_M[0][5]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][6], callback_data=sity_M[0][6]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][7], callback_data=sity_M[0][7]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][8], callback_data=sity_M[0][8]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][9], callback_data=sity_M[0][9]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][10], callback_data=sity_M[0][10]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][11], callback_data=sity_M[0][11]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][12], callback_data=sity_M[0][12]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][13], callback_data=sity_M[0][13]))
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][14], callback_data=sity_M[0][14]))
#  кнопка вернуться назад
sity_kz_A.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))



sity_kz_Б = InlineKeyboardMarkup()
#   город Байконур
sity_kz_Б.insert(InlineKeyboardButton(text=sity[1][0], callback_data=sity_M[1][0]))
#   город Балхаш
sity_kz_Б.insert(InlineKeyboardButton(text=sity[1][1], callback_data=sity_M[1][1]))
#   город Булаево
sity_kz_Б.insert(InlineKeyboardButton(text=sity[1][2], callback_data=sity_M[1][2]))
#  кнопка вернуться назад
sity_kz_Б.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_Д = InlineKeyboardMarkup()
sity_kz_Д.insert(InlineKeyboardButton(text=sity[2][0], callback_data=sity_M[2][0]))
#  кнопка вернуться назад
sity_kz_Д.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_Е = InlineKeyboardMarkup()
sity_kz_Е.insert(InlineKeyboardButton(text=sity[3][0], callback_data=sity_M[3][0]))
sity_kz_Е.insert(InlineKeyboardButton(text=sity[3][1], callback_data=sity_M[3][1]))
sity_kz_Е.insert(InlineKeyboardButton(text=sity[3][2], callback_data=sity_M[3][2]))
#  кнопка вернуться назад
sity_kz_Е.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_Ж = InlineKeyboardMarkup()
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][0], callback_data=sity_M[4][0]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][1], callback_data=sity_M[4][1]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][2], callback_data=sity_M[4][2]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][3], callback_data=sity_M[4][3]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][4], callback_data=sity_M[4][4]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][5], callback_data=sity_M[4][5]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][6], callback_data=sity_M[4][6]))
#  кнопка вернуться назад
sity_kz_Ж.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_З = InlineKeyboardMarkup()
sity_kz_З.insert(InlineKeyboardButton(text=sity[5][0], callback_data=sity_M[5][0]))
sity_kz_З.insert(InlineKeyboardButton(text=sity[5][1], callback_data=sity_M[5][1]))
#  кнопка вернуться назад
sity_kz_З.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_К = InlineKeyboardMarkup()
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][0], callback_data=sity_M[6][0]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][1], callback_data=sity_M[6][1]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][2], callback_data=sity_M[6][2]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][3], callback_data=sity_M[6][3]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][4], callback_data=sity_M[6][4]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][5], callback_data=sity_M[6][5]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][6], callback_data=sity_M[6][6]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][7], callback_data=sity_M[6][7]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][8], callback_data=sity_M[6][8]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][9], callback_data=sity_M[6][9]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][10], callback_data=sity_M[6][10]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][11], callback_data=sity_M[6][11]))
sity_kz_К.insert(InlineKeyboardButton(text=sity[6][12], callback_data=sity_M[6][12]))
#  кнопка вернуться назад
sity_kz_К.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_Л = InlineKeyboardMarkup()
sity_kz_Л.insert(InlineKeyboardButton(text=sity[7][0], callback_data=sity_M[7][0]))
sity_kz_Л.insert(InlineKeyboardButton(text=sity[7][1], callback_data=sity_M[7][1]))
#  кнопка вернуться назад
sity_kz_Л.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_М = InlineKeyboardMarkup()
sity_kz_М.insert(InlineKeyboardButton(text=sity[8][0], callback_data=sity_M[8][0]))
sity_kz_М.insert(InlineKeyboardButton(text=sity[8][1], callback_data=sity_M[8][1]))
#  кнопка вернуться назад
sity_kz_М.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_Н = InlineKeyboardMarkup()
sity_kz_Н.insert(InlineKeyboardButton(text=sity[9][0], callback_data=sity_M[9][0]))
#  кнопка вернуться назад
sity_kz_Н.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_П = InlineKeyboardMarkup()
sity_kz_П.insert(InlineKeyboardButton(text=sity[10][0], callback_data=sity_M[10][0]))
sity_kz_П.insert(InlineKeyboardButton(text=sity[10][1], callback_data=sity_M[10][1]))
sity_kz_П.insert(InlineKeyboardButton(text=sity[10][2], callback_data=sity_M[10][2]))
#  кнопка вернуться назад
sity_kz_П.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_Р = InlineKeyboardMarkup()
sity_kz_Р.insert(InlineKeyboardButton(text=sity[11][0], callback_data=sity_M[11][0]))
sity_kz_Р.insert(InlineKeyboardButton(text=sity[11][1], callback_data=sity_M[11][1]))
#  кнопка вернуться назад
sity_kz_Р.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_С = InlineKeyboardMarkup()
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][0], callback_data=sity_M[12][0]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][1], callback_data=sity_M[12][1]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][2], callback_data=sity_M[12][2]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][3], callback_data=sity_M[12][3]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][4], callback_data=sity_M[12][4]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][5], callback_data=sity_M[12][5]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][6], callback_data=sity_M[12][6]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][7], callback_data=sity_M[12][7]))
sity_kz_С.insert(InlineKeyboardButton(text=sity[12][8], callback_data=sity_M[12][8]))
#  кнопка вернуться назад
sity_kz_С.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_Т = InlineKeyboardMarkup()
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][0], callback_data=sity_M[13][0]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][1], callback_data=sity_M[13][1]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][2], callback_data=sity_M[13][2]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][3], callback_data=sity_M[13][3]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][4], callback_data=sity_M[13][4]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][5], callback_data=sity_M[13][5]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][6], callback_data=sity_M[13][6]))
sity_kz_Т.insert(InlineKeyboardButton(text=sity[13][7], callback_data=sity_M[13][7]))
#  кнопка вернуться назад
sity_kz_Т.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_У = InlineKeyboardMarkup()
sity_kz_У.insert(InlineKeyboardButton(text=sity[14][0], callback_data=sity_M[14][0]))
sity_kz_У.insert(InlineKeyboardButton(text=sity[14][1], callback_data=sity_M[14][1]))
sity_kz_У.insert(InlineKeyboardButton(text=sity[14][2], callback_data=sity_M[14][2]))
sity_kz_У.insert(InlineKeyboardButton(text=sity[14][3], callback_data=sity_M[14][3]))
#  кнопка вернуться назад
sity_kz_У.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_Ф = InlineKeyboardMarkup()
sity_kz_Ф.insert(InlineKeyboardButton(text=sity[15][0], callback_data=sity_M[15][0]))
#  кнопка вернуться назад
sity_kz_Ф.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_Х = InlineKeyboardMarkup()
sity_kz_Х.insert(InlineKeyboardButton(text=sity[16][0], callback_data=sity_M[16][0]))
#  кнопка вернуться назад
sity_kz_Х.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_Ш = InlineKeyboardMarkup()
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][0], callback_data=sity_M[17][0]))
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][1], callback_data=sity_M[17][1]))
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][2], callback_data=sity_M[17][2]))
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][3], callback_data=sity_M[17][3]))
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][4], callback_data=sity_M[17][4]))
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][5], callback_data=sity_M[17][5]))
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][6], callback_data=sity_M[17][6]))
#  кнопка вернуться назад
sity_kz_Ш.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_Щ = InlineKeyboardMarkup()
sity_kz_Щ.insert(InlineKeyboardButton(text=sity[18][0], callback_data=sity_M[18][0]))
#  кнопка вернуться назад
sity_kz_Щ.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))


sity_kz_Э = InlineKeyboardMarkup()
sity_kz_Э.insert(InlineKeyboardButton(text=sity[19][0], callback_data=sity_M[19][0]))
sity_kz_Э.insert(InlineKeyboardButton(text=sity[19][1], callback_data=sity_M[19][1]))
#  кнопка вернуться назад
sity_kz_З.add(InlineKeyboardButton(text=bark[0], callback_data="АЗБУКА_МОРЗЕ"))

# 1. Ответ на кнопку А
@dp.callback_query_handler(text="А_m")
async def call_А_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_A)


# 2. Ответ на кнопку Б
@dp.callback_query_handler(text="Б_m")
async def call_Б_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Б)


# 3. Ответ на кнопку Д
@dp.callback_query_handler(text="Д_m")
async def call_Д_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Д)


# 3. Ответ на кнопку Е
@dp.callback_query_handler(text="Е_m")
async def call_Е_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Е)


# 4. Ответ на кнопку Ж
@dp.callback_query_handler(text="Ж_m")
async def call_Ж_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Ж)


# 5. Ответ на кнопку З
@dp.callback_query_handler(text="З_m")
async def call_З_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_З)


# 6. Ответ на кнопку К
@dp.callback_query_handler(text="К_m")
async def call_К_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_К)


# 7. Ответ на кнопку Л
@dp.callback_query_handler(text="Л_m")
async def call_Л_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Л)


# 8. Ответ на кнопку М
@dp.callback_query_handler(text="М_m")
async def call_М_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_М)


# 9. Ответ на кнопку Н
@dp.callback_query_handler(text="Н_m")
async def call_Н_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Н)


# 10. Ответ на кнопку П
@dp.callback_query_handler(text="П_m")
async def call_П_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_П)


# 11. Ответ на кнопку Р
@dp.callback_query_handler(text="Р_m")
async def call_Р_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Р)


# 12. Ответ на кнопку С
@dp.callback_query_handler(text="С_m")
async def call_С_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_С)


# 13. Ответ на кнопку Т
@dp.callback_query_handler(text="Т_m")
async def call_Т_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Т)


# 14. Ответ на кнопку У
@dp.callback_query_handler(text="У_m")
async def call_У_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_У)


# 15. Ответ на кнопку Ф
@dp.callback_query_handler(text="Ф_m")
async def call_Ф_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Ф)


# 16. Ответ на кнопку Х
@dp.callback_query_handler(text="Х_m")
async def call_Х_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Х)


# 17. Ответ на кнопку Ш
@dp.callback_query_handler(text="Ш_m")
async def call_Ш_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Ш)


# 18. Ответ на кнопку Щ
@dp.callback_query_handler(text="Щ_m")
async def call_Щ_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Щ)


# 19. Ответ на кнопку Э
@dp.callback_query_handler(text="Э_m")
async def call_Э_sity(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text[0], reply_markup=sity_kz_Э)


def register_message_handler_call_ABC_sity_m(dp: Dispatcher):
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