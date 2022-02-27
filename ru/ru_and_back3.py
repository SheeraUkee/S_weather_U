import requests
from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
KEY = "54ffac44c73196951917bf3cbb5f6f80"
URL = "https://api.openweathermap.org/data/2.5/weather"
from data_config import dp, bot
key_sity = [
    "Обновить 🔁",
    "Назад ↩️",
    "Удалить 🗑"
]

@dp.callback_query_handler(text=[
        "Абай",# 1.
        "Акколь",# 2.
        "Аксай",# 3.
        "Аксу",# 4.
        "Актау",# 5.
        "Актобе",# 6.
        "Алга",# 7.
        "Алматы",# 8.
        "Алтай",# 9.
        "Аральск",# 10.
        "Аркалык",# 11.
        "Арыс",# 12.
        "Атбасар",# 13.
        "Атырау",# 14.
        "Аягоз",
        "Байконур",
        "Балхаш",
        "Державинск",
        "Ерейментау",
        "Есик",
        "Есиль",
        "Жанаозен",
        "Жанатас",
        "Жаркент",
        "Жезказган",
        "Жем",
        "Жетысай",
        "Житикара",
        "Булаево",
        "Зайсан",
        "Зыряновск",
        "Казалинск",
        "Кандыагаш",
        "Капшагай",
        "Караганды",
        "Каражал",
        "Каратау",
        "Каркаралинск",
        "Кентау",
        "Кокшетау",
        "Костанай",
        "Кулсары",
        "Курчатов",
        "Кызылорда",
        "Ленгер",
        "Лисаковск",
        "Макинск",
        "Мамлютка",
        "Нур-Султан",
        "Павлодар",
        "Петропавловск",
        "Приозёрск",
        "Риддер",
        "Рудный",
        "Сарань",
        "Сарканд",
        "Сарыагаш",
        "Сатпаев",
        "Семей",
        "Сергеевка",
        "Серебрянск",
        "Степногорск",
        "Степняк",
        "Тайынша",
        "Талгар",
        "Талдыкорган",
        "Тараз",
        "Текели",
        "Темир",
        "Темиртау",
        "Туркестан",
        "Уральск",
        "Усть-Каменогорск",
        "Ушарал",
        "Уштобе",
        "Форт-Шевченко",
        "Хромтау",
        "Шалкар",
        "Шар",
        "Шардара",
        "Шахтинск",
        "Шемонаиха",
        "Шу",
        "Шымкент",
        "Щучинск"
        "Экибастуз",
        "Эмба",
        "12"
    ])
async def call_weather_sity_key(call: types.CallbackQuery):
    a = "Almaty, KZ"

    call_sity = call.data
    call_index = call_sity[0]
    call_call = str(call.data) + "1"
    print(call_call)
    def_info_weather = InlineKeyboardMarkup()
    def_info_weather.add(InlineKeyboardButton(text=key_sity[0], callback_data=call.data))
    def_info_weather.insert(InlineKeyboardButton(text=key_sity[2], callback_data="delet"))
    def_info_weather.add(InlineKeyboardButton(text=key_sity[1], callback_data = call_index))

    if call.data == "Экибастуз":
        a = "Ekibastuz, KZ"
        area = "Павлодарская область"
    elif call.data == "Эмба":
        a = "Emba, KZ"
        area = "Актюбинская область"
    test = a
    if call.data == "Щучинск":
        a = "Shchuchinsk, KZ"
        area = "Акмолинская область"
    if call.data == "Шалкар":
        a = "Shalkar, KZ"
        area = "Актюбинская область"
    elif call.data == "Шар":
        a = "Shardara, KZ"
        area = "Южно-Казахстанская область"
    elif call.data == "Шардара":
        a = "Shardara, KZ"
        area = "Южно-Казахстанская область"
    elif call.data == "Шахтинск":
        a = "Shakhtinsk, KZ"
        area = "Карагандинская область"
    elif call.data == "Шемонаиха":
        a = "Shemonaikha, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Шу":
        a = "Shu, KZ"
        area = "Жамбыльская область"
    elif call.data == "Шымкент":
        a = "Shymkent, KZ"
        area = "Южно-Казахстанская область"
    if call.data == "Хромтау":
        a = "Khromtau, KZ"
        area = "Актюбинская область"
    if call.data == "Форт-Шевченко":
        a = "Fort-Shevchenko, KZ"
        area = "Мангистауская область"
    if call.data == "Уральск":
        a = "Uralsk, KZ"
        area = "Западно-Казахстанская область"
    elif call.data == "Усть-Каменогорск":
        a = "Ust-Kamenogorsk, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Ушарал":
        a = "Usharal, KZ"
        area = "Алматинская область"
    elif call.data == "Уштобе":
        a = "Ushtobe, KZ"
        area = "Алматинская область"
    if call.data == "Тайынша":
        a = "Taiynsha, KZ"
        area = "Северо-Казахстанская область"
    elif call.data == "Талгар":
        a = "Talgar, KZ"
        area = "Алматинская область"
    elif call.data == "Талдыкорган":
        a = "Taldykorgan, KZ"
        area = "Алматинская область"
    elif call.data == "Тараз":
        a = "Taraz, KZ"
        area = "Жамбыльская область"
    elif call.data == "Текели":
        a = "Tekeli, KZ"
        area = "Алматинская область"
    elif call.data == "Темир":
        a = "Temir, KZ"
        area = "Актюбинская область"
    elif call.data == "Темиртау":
        a = "Temirtau, KZ"
        area = "Карагандинская область"
    elif call.data == "Туркестан":
        a = "Turkestan, KZ"
        area = "Южно-Казахстанская область"
    if call.data == "Сарань":
        a = "Saran, KZ"
        area = "Карагандинская область"
    elif call.data == "Сарканд":
        a = "Sarkand, KZ"
        area = "Алматинская область"
    elif call.data == "Сарыагаш":
        a = "Saryagash, KZ"
        area = "	Южно-Казахстанская область"
    elif call.data == "Сатпаев":
        a = "Satpaev, KZ"
        area = "Карагандинская область"
    elif call.data == "Семей":
        a = "Semey, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Сергеевка":
        a = "Sergeyevka, KZ"
        area = "Северо-Казахстанская область"
    elif call.data == "Серебрянск":
        a = "Serebryansk, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Степногорск":
        a = "Stepnogorsk, KZ"
        area = "Акмолинская область"
    elif call.data == "Степняк":
        a = "Stepnyak, KZ"
        area = "Акмолинская область"
    if call.data == "Риддер":
        a = "Ridder, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Рудный":
        a = "Rudny, KZ"
        area = "Восточно-Казахстанская область"
    if call.data == "Павлодар":
        a = "Pavlodar, KZ"
        area = "Павлодарская область"
    elif call.data == "Петропавловск":
        a = "Petropavlovsk, KZ"
        area = "Северо-Казахстанская область"
    elif call.data == "Приозёрск, KZ":
        a = "Priozersk, KZ"
        area = "Карагандинская область"
    if call.data == "Нур-Султан":
        a = "Nur-Sultan, KZ"
        area = "Акмолинская область"
    if call.data == "Макинск":
        a = "Makinsk, KZ"
        area = "Акмолинская область"
    elif call.data == "Мамлютка":
        a = "Mamlyutka, KZ"
        area = "Северо-Казахстанская область"
    if call.data == "Абай":# 1.
        a = "Abai, KZ"
        area = "Карагандинская область"
    elif call.data == "Акколь":# 2.
        a = "Akkol, KZ"
        area = "Акмолинская область"
    elif call.data == "Аксай":# 3.
        a = "Aksay, KZ"
        area = "Западно-Казахстанская область"
    elif call.data == "Аксу":# 4.
        a = "Aksu, KZ"
        area = "Павлодарская область"
    elif call.data == "Актау":# 5.
        a = "Aktau, KZ"
        area = "Мангистауская область"
    elif call.data == "Актобе":# 6.
        a = "Aktobe, KZ"
        area = "Актюбинская область"
    elif call.data == "Алга":# 7.
        a = "Alga, KZ"
        area = "Актюбинская область"
    elif call.data == "Алматы":# 8.
        a = "Almaty, KZ"
        area = "Алматы"
    elif call.data == "Алтай":# 9.
        a = "Altaysk, KZ"
        area = "Кызылординская область"
    elif call.data == "Аральск":# 10.
        a = "Aralsk, KZ"
        area = "Кызылординская область"
    elif call.data == "Аркалык":# 11.
        a = "Arkalyk, KZ"
        area = "Костанайская область"
    elif call.data == "Арыс":# 12.
        a = "Arys, KZ"
        area = "Южно-Казахстанская область"
    elif call.data == "Атбасар":# 13.
        a = "Atbasar, KZ"
        area = "Акмолинская область"
    elif call.data == "Атырау":# 14.
        a = "Atyrau, KZ"
        area = "Атырауская область"
    elif call.data == "Аягоз":# 15.
        a = "Ayagoz, KZ"
        area = "Восточно-Казахстанская область"
    if call.data == "Байконур":
        a = "Baikonur, KZ"
        area = "Арендуется Российской Федерацией"
    elif call.data == "Балхаш":
        a = "Balkhash, KZ"
        area = "Карагандинская область"
    elif call.data == "Булаево":
        a = "Bulaevo, KZ"
        area = "Северо-Казахстанская область"
    if call.data == "Державинск":
        a = "Derzhavinsk, KZ"
        area = "Акмолинская область"
    if call.data == "Ерейментау":
        a = "Ereymentau, KZ"
        area = "Акмолинская область"
    elif call.data == "Есик":
        a = "Esik, KZ"
        area = "Алматинская область"
    elif call.data == "Есиль":
        a = "Esil, KZ"
        area = "Акмолинская область"
    if call.data == "Жанаозен":
        a = "Zhanaozen, KZ"
        area = "Мангистауская область"
    elif call.data == "Жанатас":
        a = "Janatas, KZ"
        area = "Жамбыльская область"
    elif call.data == "Жаркент":
        a = "Zharkent, KZ"
        area = "Алматинская область"
    elif call.data == "Жезказган":
        a = "Zhezkazgan , KZ"
        area = "Карагандинская область"
    elif call.data == "Жем":
        a = "Zhem, KZ"
        area = "Актюбинская область"
    elif call.data == "Жетысай":
        a = "Zhetisay, KZ"
        area = "Южно-Казахстанская область"
    elif call.data == "Житикара":
        a = "Zhetikara, KZ"
        area = "Костанайская область"
    if call.data == "Зайсан":
        a = "Ereymentau, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Зыряновск":
        a = "Esik, KZ"
        area = "Восточно-Казахстанская область"
    if call.data == "Кандыагаш":
        a = "Kandyagash, KZ"
        area = "Актюбинская область"
    elif call.data == "Капшагай":
        a = "Kapshagai, KZ"
        area = "Алматинская область"
    elif call.data == "Караганда":
        a = "Karaganda, KZ"
        area = "Карагандинская область"
    elif call.data == "Каражал":
        a = "Karazhal, KZ"
        area = "Карагандинская область"
    elif call.data == "Каратау":
        a = "Karatau, KZ"
        area = "Жамбыльская область"
    elif call.data == "Каркаралинск":
        a = "Karkaralinsk, KZ"
        area = "Карагандинская область"
    elif call.data == "Кентау":
        a = "Kentau, KZ"
        area = "Южно-Казахстанская область"
    elif call.data == "Кокшетау":
        a = "Kokshetau, KZ"
        area = "Акмолинская область"
    elif call.data == "Костанай":
        a = "Kostanay, KZ"
        area = "Костанайская область"
    elif call.data == "Кулсары":
        a = "Kulsary, KZ"
        area = "Атырауская область"
    elif call.data == "Курчатов":
        a = "Kurchatov, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Кызылорда":
        a = "Kyzylorda, KZ"
        area = "Кызылординская область"
    if call.data == "Ленгер":
        a = "Lenger, KZ"
        area = "Южно-Казахстанская область"
    elif call.data == "Лисаковск":
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
        tran = "Облачно с прояснениями ⛅ ️️"

    elif weather_main == "Mist":
        tran = "Туман ☁ ️"

    elif weather_main == "Fog":
        tran = "Туман ☁ ️"

    elif weather_main == "Smoke":
        tran = "Пасмурно ☁ ️"

    elif weather_main == "Clear":
        tran = "Ясно ☀️"

    elif weather_main == "Snow":
        tran = "Снег 🥶"

    elif weather_main == "Rain":
        tran = "Дождь 🌧"

    else:
        tran = "⁉️⁉️"
    sss = call.data


    p = "Город " + sss + "\n" + area + "\n" + tran + "\n" + str(
        int(weather_temp)) + " °C" + "\n" + "По ощущениям " + \
        str(int(weather_feels_like)) + " °C" + "\n" + "Влажность " + str(weather_humidity) + \
        " %" + "\n" + "Видимость " + str(float(weather_visibility / 1000)) + " км." + "\n" + "Скорость ветра " + \
        str(weather_wind) + " м./с. "

    print(p)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, p, reply_markup=def_info_weather)






def register_message_handler_call_sity_info_key(dp: Dispatcher):
    dp.register_message_handler(call_weather_sity_key)