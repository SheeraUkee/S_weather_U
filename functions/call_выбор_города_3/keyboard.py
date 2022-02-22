from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from functions.call_выбор_города_3.kb_text import sity, bark

sity_kz_A = InlineKeyboardMarkup()
#   город Абай
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][0], callback_data=sity[0][0]))
#   город Акколь
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][1], callback_data=sity[0][1]))
#   город Аксай
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][2], callback_data=sity[0][2]))
#   город Аксу
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][3], callback_data=sity[0][3]))
#   город Актау
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][4], callback_data=sity[0][4]))
#   город Актобе
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][5], callback_data=sity[0][5]))
#   город Алга
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][6], callback_data=sity[0][6]))
#   город Алматы
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][7], callback_data=sity[0][7]))
#   город Алтай
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][8], callback_data=sity[0][8]))
#   город Аральск
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][9], callback_data=sity[0][9]))
#   город Аркалык
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][10], callback_data=sity[0][10]))
#   город Арыс
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][11], callback_data=sity[0][11]))
#   город Атбасар
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][12], callback_data=sity[0][12]))
#   город Атырау
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][13], callback_data=sity[0][13]))
#   город Аягос
sity_kz_A.insert(InlineKeyboardButton(text=sity[0][14], callback_data=sity[0][14]))
#  кнопка вернуться назад
sity_kz_A.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))



sity_kz_Б = InlineKeyboardMarkup()
#   город Байконур
sity_kz_Б.insert(InlineKeyboardButton(text=sity[1][0], callback_data=sity[1][0]))
#   город Балхаш
sity_kz_Б.insert(InlineKeyboardButton(text=sity[1][1], callback_data=sity[1][1]))
#   город Булаево
sity_kz_Б.insert(InlineKeyboardButton(text=sity[1][2], callback_data=sity[1][2]))
#  кнопка вернуться назад
sity_kz_Б.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_Д = InlineKeyboardMarkup()
sity_kz_Д.insert(InlineKeyboardButton(text=sity[2][0], callback_data=sity[2][0]))
#  кнопка вернуться назад
sity_kz_Д.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_Е = InlineKeyboardMarkup()
sity_kz_Е.insert(InlineKeyboardButton(text=sity[3][0], callback_data=sity[3][0]))
sity_kz_Е.insert(InlineKeyboardButton(text=sity[3][1], callback_data=sity[3][1]))
sity_kz_Е.insert(InlineKeyboardButton(text=sity[3][2], callback_data=sity[3][2]))
#  кнопка вернуться назад
sity_kz_Е.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_Ж = InlineKeyboardMarkup()
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][0], callback_data=sity[4][0]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][1], callback_data=sity[4][1]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][2], callback_data=sity[4][2]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][3], callback_data=sity[4][3]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][4], callback_data=sity[4][4]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][5], callback_data=sity[4][5]))
sity_kz_Ж.insert(InlineKeyboardButton(text=sity[4][6], callback_data=sity[4][6]))
#  кнопка вернуться назад
sity_kz_Ж.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_З = InlineKeyboardMarkup()
sity_kz_З.insert(InlineKeyboardButton(text=sity[5][0], callback_data=sity[5][0]))
sity_kz_З.insert(InlineKeyboardButton(text=sity[5][1], callback_data=sity[5][1]))
#  кнопка вернуться назад
sity_kz_З.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


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
sity_kz_К.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_Л = InlineKeyboardMarkup()
sity_kz_Л.insert(InlineKeyboardButton(text=sity[7][0], callback_data=sity[7][0]))
sity_kz_Л.insert(InlineKeyboardButton(text=sity[7][1], callback_data=sity[7][1]))
#  кнопка вернуться назад
sity_kz_Л.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_М = InlineKeyboardMarkup()
sity_kz_М.insert(InlineKeyboardButton(text=sity[8][0], callback_data=sity[8][0]))
sity_kz_М.insert(InlineKeyboardButton(text=sity[8][1], callback_data=sity[8][1]))
#  кнопка вернуться назад
sity_kz_М.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_Н = InlineKeyboardMarkup()
sity_kz_Н.insert(InlineKeyboardButton(text=sity[9][0], callback_data=sity[9][0]))
#  кнопка вернуться назад
sity_kz_Н.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_П = InlineKeyboardMarkup()
sity_kz_П.insert(InlineKeyboardButton(text=sity[10][0], callback_data=sity[10][0]))
sity_kz_П.insert(InlineKeyboardButton(text=sity[10][1], callback_data=sity[10][1]))
sity_kz_П.insert(InlineKeyboardButton(text=sity[10][2], callback_data=sity[10][2]))
#  кнопка вернуться назад
sity_kz_П.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_Р = InlineKeyboardMarkup()
sity_kz_Р.insert(InlineKeyboardButton(text=sity[11][0], callback_data=sity[11][0]))
sity_kz_Р.insert(InlineKeyboardButton(text=sity[11][1], callback_data=sity[11][1]))
#  кнопка вернуться назад
sity_kz_Р.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


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
sity_kz_С.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


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
sity_kz_Т.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_У = InlineKeyboardMarkup()
sity_kz_У.insert(InlineKeyboardButton(text=sity[14][0], callback_data=sity[14][0]))
sity_kz_У.insert(InlineKeyboardButton(text=sity[14][1], callback_data=sity[14][1]))
sity_kz_У.insert(InlineKeyboardButton(text=sity[14][2], callback_data=sity[14][2]))
sity_kz_У.insert(InlineKeyboardButton(text=sity[14][3], callback_data=sity[14][3]))
#  кнопка вернуться назад
sity_kz_У.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_Ф = InlineKeyboardMarkup()
sity_kz_Ф.insert(InlineKeyboardButton(text=sity[15][0], callback_data=sity[15][0]))
#  кнопка вернуться назад
sity_kz_Ф.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_Х = InlineKeyboardMarkup()
sity_kz_Х.insert(InlineKeyboardButton(text=sity[16][0], callback_data=sity[16][0]))
#  кнопка вернуться назад
sity_kz_Х.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_Ш = InlineKeyboardMarkup()
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][0], callback_data=sity[17][0]))
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][1], callback_data=sity[17][1]))
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][2], callback_data=sity[17][2]))
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][3], callback_data=sity[17][3]))
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][4], callback_data=sity[17][4]))
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][5], callback_data=sity[17][5]))
sity_kz_Ш.insert(InlineKeyboardButton(text=sity[17][6], callback_data=sity[17][6]))
#  кнопка вернуться назад
sity_kz_Ш.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_Щ = InlineKeyboardMarkup()
sity_kz_Щ.insert(InlineKeyboardButton(text=sity[18][0], callback_data=sity[18][0]))
#  кнопка вернуться назад
sity_kz_Щ.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))


sity_kz_Э = InlineKeyboardMarkup()
sity_kz_Э.insert(InlineKeyboardButton(text=sity[19][0], callback_data=sity[19][0]))
sity_kz_Э.insert(InlineKeyboardButton(text=sity[19][1], callback_data=sity[19][1]))
#  кнопка вернуться назад
sity_kz_З.add(InlineKeyboardButton(text=bark[0], callback_data="call_sity_1"))