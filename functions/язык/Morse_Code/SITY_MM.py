import time

import requests
from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

KEY = "54ffac44c73196951917bf3cbb5f6f80"
URL = "https://api.openweathermap.org/data/2.5/weather"
from config import dp, bot
from functions.call_sity_4.text import key_sity


@dp.callback_query_handler(text=[
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
    "Аягоз_M",
    "Байконур_M",
    "Балхаш_M",
    "Державинск_M",
    "Ерейментау_M",
    "Есик_M",
    "Есиль_M",
    "Жанаозен_M",
    "Жанатас_M",
    "Жаркент_M",
    "Жезказган_M",
    "Жем_M",
    "Жетысай_M",
    "Житикара_M",
    "Булаево_M",
    "Зайсан_M",
    "Зыряновск_M",
    "Казалинск_M",
    "Кандыагаш_M",
    "Капшагай_M",
    "Караганды_M",
    "Каражал_M",
    "Каратау_M",
    "Каркаралинск_M",
    "Кентау_M",
    "Кокшетау_M",
    "Костанай_M",
    "Кулсары_M",
    "Курчатов_M",
    "Кызылорда_M",
    "Ленгер_M",
    "Лисаковск_M",
    "Макинск_M",
    "Мамлютка_M",
    "Нур-Султан_M",
    "Павлодар_M",
    "Петропавловск_M",
    "Приозёрск_M",
    "Риддер_M",
    "Рудный_M",
    "Сарань_M",
    "Сарканд_M",
    "Сарыагаш_M",
    "Сатпаев_M",
    "Семей_M",
    "Сергеевка_M",
    "Серебрянск_M",
    "Степногорск_M",
    "Степняк_M",
    "Тайынша_M",
    "Талгар_M",
    "Талдыкорган_M",
    "Тараз_M",
    "Текели_M",
    "Темир_M",
    "Темиртау_M",
    "Туркестан_M",
    "Уральск_M",
    "Усть-Каменогорск_M",
    "Ушарал_M",
    "Уштобе_M",
    "Форт-Шевченко_M",
    "Хромтау_M",
    "Шалкар_M",
    "Шар_M",
    "Шардара_M",
    "Шахтинск_M",
    "Шемонаиха_M",
    "Шу_M",
    "Шымкент_M",
    "Щучинск_M"
    "Экибастуз_M",
    "Эмба_M"
])
async def call_weather_sity_key_mm(call: types.CallbackQuery):
    a = "Almaty, KZ"

    call_sity = call.data
    call_index = call_sity[0]
    call_call = str(call.data) + "1"
    print(call_call)
    def_info_weather = InlineKeyboardMarkup()
    def_info_weather.add(InlineKeyboardButton(text=key_sity[0], callback_data=call.data))
    def_info_weather.insert(InlineKeyboardButton(text=key_sity[2], callback_data="delet"))
    def_info_weather.add(InlineKeyboardButton(text=key_sity[1], callback_data=call_index + "_m"))

    if call.data == "Экибастуз_M":
        a = "Ekibastuz, KZ"
        area = "Павлодарская область"

    elif call.data == "Эмба_M":
        a = "Emba, KZ"
        area = "Актюбинская область"

    if call.data == "Щучинск_M":
        a = "Shchuchinsk, KZ"
        area = "Акмолинская область"

    if call.data == "Шалкар_M":
        a = "Shalkar, KZ"
        area = "Актюбинская область"

    elif call.data == "Шар_M":
        a = "Shardara, KZ"
        area = "Южно-Казахстанская область"

    elif call.data == "Шардара_M":
        a = "Shardara, KZ"
        area = "Южно-Казахстанская область"

    elif call.data == "Шахтинск_M":
        a = "Shakhtinsk, KZ"
        area = "Карагандинская область"

    elif call.data == "Шемонаиха_M":
        a = "Shemonaikha, KZ"
        area = "Восточно-Казахстанская область"

    elif call.data == "Шу_M":
        a = "Shu, KZ"
        area = "Жамбыльская область"

    elif call.data == "Шымкент_M":
        a = "Shymkent, KZ"
        area = "Южно-Казахстанская область"

    if call.data == "Хромтау_M":
        a = "Khromtau, KZ"
        area = "Актюбинская область"

    if call.data == "Форт-Шевченко_M":
        a = "Fort-Shevchenko, KZ"
        area = "Мангистауская область"

    if call.data == "Уральск_M":
        a = "Uralsk, KZ"
        area = "Западно-Казахстанская область"

    elif call.data == "Усть-Каменогорск_M":
        a = "Ust-Kamenogorsk, KZ"
        area = "Восточно-Казахстанская область"

    elif call.data == "Ушарал_M":
        a = "Usharal, KZ"
        area = "Алматинская область"

    elif call.data == "Уштобе_M":
        a = "Ushtobe, KZ"
        area = "Алматинская область"

    if call.data == "Тайынша_M":
        a = "Taiynsha, KZ"
        area = "Северо-Казахстанская область"

    elif call.data == "Талгар_M":
        a = "Talgar, KZ"
        area = "Алматинская область"

    elif call.data == "Талдыкорган_M":
        a = "Taldykorgan, KZ"
        area = "Алматинская область"

    elif call.data == "Тараз_M":
        a = "Taraz, KZ"
        area = "Жамбыльская область"

    elif call.data == "Текели_M":
        a = "Tekeli, KZ"
        area = "Алматинская область"

    elif call.data == "Темир_M":
        a = "Temir, KZ"
        area = "Актюбинская область"

    elif call.data == "Темиртау_M":
        a = "Temirtau, KZ"
        area = "Карагандинская область"

    elif call.data == "Туркестан_M":
        a = "Turkestan, KZ"
        area = "Южно-Казахстанская область"

    if call.data == "Сарань_M":
        a = "Saran, KZ"
        area = "Карагандинская область"

    elif call.data == "Сарканд_M":
        a = "Sarkand, KZ"
        area = "Алматинская область"

    elif call.data == "Сарыагаш_M":
        a = "Saryagash, KZ"
        area = "	Южно-Казахстанская область"

    elif call.data == "Сатпаев_M":
        a = "Satpaev, KZ"
        area = "Карагандинская область"

    elif call.data == "Семей_M":
        a = "Semey, KZ"
        area = "Восточно-Казахстанская область"

    elif call.data == "Сергеевка_M":
        a = "Sergeyevka, KZ"
        area = "Северо-Казахстанская область"

    elif call.data == "Серебрянск_M":
        a = "Serebryansk, KZ"
        area = "Восточно-Казахстанская область"

    elif call.data == "Степногорск_M":
        a = "Stepnogorsk, KZ"
        area = "Акмолинская область"

    elif call.data == "Степняк_M":
        a = "Stepnyak, KZ"
        area = "Акмолинская область"

    if call.data == "Риддер_M":
        a = "Ridder, KZ"
        area = "Восточно-Казахстанская область"

    elif call.data == "Рудный_M":
        a = "Rudny, KZ"
        area = "Восточно-Казахстанская область"

    if call.data == "Павлодар_M":
        a = "Pavlodar, KZ"
        area = "Павлодарская область"

    elif call.data == "Петропавловск_M":
        a = "Petropavlovsk, KZ"
        area = "Северо-Казахстанская область"

    elif call.data == "Приозёрск_M":
        a = "Priozersk, KZ"
        area = "Карагандинская область"

    if call.data == "Нур-Султан_M":
        a = "Nur-Sultan, KZ"
        area = "Акмолинская область"

    if call.data == "Макинск_M":
        a = "Makinsk, KZ"
        area = "Акмолинская область"

    elif call.data == "Мамлютка_M":
        a = "Mamlyutka, KZ"
        area = "Северо-Казахстанская область"

    if call.data == "Абай_M":  # 1.
        a = "Abai, KZ"
        area = "Карагандинская область"

    elif call.data == "Акколь_M":  # 2.
        a = "Akkol, KZ"
        area = "Акмолинская область"

    elif call.data == "Аксай_M":  # 3.
        a = "Aksay, KZ"
        area = "Западно-Казахстанская область"

    elif call.data == "Аксу_M":  # 4.
        a = "Aksu, KZ"
        area = "Павлодарская область"

    elif call.data == "Актау_M":  # 5.
        a = "Aktau, KZ"
        area = "Мангистауская область"

    elif call.data == "Актобе_M":  # 6.
        a = "Aktobe, KZ"
        area = "Актюбинская область"

    elif call.data == "Алга_M":  # 7.
        a = "Alga, KZ"
        area = "Актюбинская область"

    elif call.data == "Алматы_M":  # 8.
        a = "Almaty, KZ"
        area = "Алматы"

    elif call.data == "Алтай_M":  # 9.
        a = "Altaysk, KZ"
        area = "Кызылординская область"

    elif call.data == "Аральск_M":  # 10.
        a = "Aralsk, KZ"
        area = "Кызылординская область"

    elif call.data == "Аркалык_M":  # 11.
        a = "Arkalyk, KZ"
        area = "Костанайская область"

    elif call.data == "Арыс_M":  # 12.
        a = "Arys, KZ"
        area = "Южно-Казахстанская область"

    elif call.data == "Атбасар_M":  # 13.
        a = "Atbasar, KZ"
        area = "Акмолинская область"

    elif call.data == "Атырау_M":  # 14.
        a = "Atyrau, KZ"
        area = "Атырауская область"

    elif call.data == "Аягоз_M":  # 15.
        a = "Ayagoz, KZ"
        area = "Восточно-Казахстанская область"

    if call.data == "Байконур_M":
        a = "Baikonur, KZ"
        area = "Арендуется Российской Федерацией"

    elif call.data == "Балхаш_M":
        a = "Balkhash, KZ"
        area = "Карагандинская область"

    elif call.data == "Булаево_M":
        a = "Bulaevo, KZ"
        area = "Северо-Казахстанская область"

    if call.data == "Державинск_M":
        a = "Derzhavinsk, KZ"
        area = "Акмолинская область"

    if call.data == "Ерейментау_M":
        a = "Ereymentau, KZ"
        area = "Акмолинская область"

    elif call.data == "Есик_M":
        a = "Esik, KZ"
        area = "Алматинская область"

    elif call.data == "Есиль_M":
        a = "Esil, KZ"
        area = "Акмолинская область"

    if call.data == "Жанаозен_M":
        a = "Zhanaozen, KZ"
        area = "Мангистауская область"

    elif call.data == "Жанатас_M":
        a = "Janatas, KZ"
        area = "Жамбыльская область"

    elif call.data == "Жаркент_M":
        a = "Zharkent, KZ"
        area = "Алматинская область"

    elif call.data == "Жезказган_M":
        a = "Zhezkazgan , KZ"
        area = "Карагандинская область"

    elif call.data == "Жем_M":
        a = "Zhem, KZ"
        area = "Актюбинская область"

    elif call.data == "Жетысай_M":
        a = "Zhetisay, KZ"
        area = "Южно-Казахстанская область"

    elif call.data == "Житикара_M":
        a = "Zhetikara, KZ"
        area = "Костанайская область"

    if call.data == "Зайсан_M":
        a = "Ereymentau, KZ"
        area = "Восточно-Казахстанская область"

    elif call.data == "Зыряновск_M":
        a = "Esik, KZ"
        area = "Восточно-Казахстанская область"

    if call.data == "Кандыагаш_M":
        a = "Kandyagash, KZ"
        area = "Актюбинская область"

    elif call.data == "Капшагай_M":
        a = "Kapshagai, KZ"
        area = "Алматинская область"

    elif call.data == "Караганда_M":
        a = "Karaganda, KZ"
        area = "Карагандинская область"

    elif call.data == "Каражал_M":
        a = "Karazhal, KZ"
        area = "Карагандинская область"

    elif call.data == "Каратау_M":
        a = "Karatau, KZ"
        area = "Жамбыльская область"

    elif call.data == "Каркаралинск_M":
        a = "Karkaralinsk, KZ"
        area = "Карагандинская область"

    elif call.data == "Кентау_M":
        a = "Kentau, KZ"
        area = "Южно-Казахстанская область"

    elif call.data == "Кокшетау_M":
        a = "Kokshetau, KZ"
        area = "Акмолинская область"

    elif call.data == "Костанай_M":
        a = "Kostanay, KZ"
        area = "Костанайская область"

    elif call.data == "Кулсары_M":
        a = "Kulsary, KZ"
        area = "Атырауская область"

    elif call.data == "Курчатов_M":
        a = "Kurchatov, KZ"
        area = "Восточно-Казахстанская область"

    elif call.data == "Кызылорда_M":
        a = "Kyzylorda, KZ"
        area = "Кызылординская область"

    if call.data == "Ленгер_M":
        a = "Lenger, KZ"
        area = "Южно-Казахстанская область"

    elif call.data == "Лисаковск_M":
        a = "Lisakovsk, KZ"
        area = "Костанайская область"

    test = a

    city = test.capitalize()
    params = {
        "q": city,
        "appid": KEY,
        "units": "metric"
    }

    data = requests.get(URL, params)
    weather_city = data.json()

    # print(weather_city)
    weather_temp = weather_city["main"]["temp"]
    weather_main = weather_city["weather"][0]["main"]
    weather_feels_like = weather_city["main"]["feels_like"]
    weather_humidity = weather_city["main"]["humidity"]
    weather_visibility = weather_city["visibility"]
    weather_wind = weather_city["wind"]["speed"]

    print("\n")
    print(weather_temp, weather_main, weather_feels_like, weather_humidity, weather_visibility, weather_wind, end="\n")

    if weather_main == "Clouds":
        tran = "Облачно с прояснениями ️️"

    elif weather_main == "Mist":
        tran = "Туман ️"

    elif weather_main == "Fog":
        tran = "Туман"

    elif weather_main == "Smoke":
        tran = "Пасмурно"

    elif weather_main == "Clear":
        tran = "Ясно"

    elif weather_main == "Snow":
        tran = "Снег"

    elif weather_main == "Rain":
        tran = "Дождь"

    sss = call.data

    p = "Город " + sss + "\n" + area + "\n" + tran + "\n" + str(
        int(weather_temp)) + " градусов" + "\n" + "По ощущениям " + \
        str(int(weather_feels_like)) + " градусов" + "\n" + "Влажность " + str(weather_humidity) + \
        " процентов" + "\n" + "Видимость " + str(
        float(weather_visibility / 1000)) + " километров" + "\n" + "Скорость ветра " + \
        str(weather_wind) + " метров в секунду "
    assas = []

    for i in p:
        assas.append(i)
        if i == "Г" or i == "г":
            await bot.send_message(call.from_user.id, "_")
            time.sleep(1)
            await bot.send_message(call.from_user.id, "_")
            time.sleep(3)
            await bot.send_message(call.from_user.id, "_")
            time.sleep(1)
            await bot.send_message(call.from_user.id, "_")
            time.sleep(3)
            await bot.send_message(call.from_user.id, ".")
            time.sleep(5)

        elif i == "О" or i == "о":
            await bot.send_message(call.from_user.id, "_")
            time.sleep(1)
            await bot.send_message(call.from_user.id, "_")
            time.sleep(3)
            await bot.send_message(call.from_user.id, "_")
            time.sleep(1)
            await bot.send_message(call.from_user.id, "_")
            time.sleep(3)
            await bot.send_message(call.from_user.id, "_")
            time.sleep(1)
            await bot.send_message(call.from_user.id, "_")
            time.sleep(5)

        elif i == "" or i == "":
            pass
        elif i == "" or i == "":
            pass
        elif i == "" or i == "":
            pass
        elif i == "" or i == "":
            pass
        elif i == "" or i == "":
            pass
        elif i == "" or i == "":
            pass
        elif i == "" or i == "":
            pass
        elif i == "" or i == "":
            pass
        elif i == "" or i == "":
            pass
        elif i == "" or i == "":
            pass
        elif i == "" or i == "":
            pass
        else:
            await bot.send_message(call.from_user.id, "_!_")



    print(assas)


def register_message_handler_call_sity_info_key_mm(dp: Dispatcher):
    dp.register_message_handler(call_weather_sity_key_mm)
