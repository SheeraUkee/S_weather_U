import requests
from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

KEY = "54ffac44c73196951917bf3cbb5f6f80"
URL = "https://api.openweathermap.org/data/2.5/weather"
from data_config import dp, bot
key_sity = ["Update 🔁", "Back ↩️", "Delete 🗑"]


@dp.callback_query_handler(text=[
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
        "Ayagoz",
        "Baikonur ",
        "Balkhash",
        "Bulayevo",
        "Derzhavinsk",
        "Ereymentau",
        "Esik",
        "Esil",
        "Ekibastuz",
        "Emba",
        "Zhanaozen",
        "Zhanatas",
        "Zharkent",
        "Zhezkazgan",
        "Zhem",
        "Zhetisay",
        "Zhetikara",
        "Zaisan",
        "Zyryanovsk",
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
        "Khromtau",
        "Lenger",
        "Lisakovsk",
        "Makinsk",
        "Mamlyutka",
        "Нур-Султан"
        "Pavlodar",
        "Petropavlovsk",
        "Priozersk"
        "Ridder",
        "Rudny"
        "Saran",
        "Sarkand",
        "Saryagash",
        "Satpayev",
        "Semey",
        "Sergeyevka",
        "Serebryansk",
        "Stepnogorsk",
        "Stepnyak",
        "Taiynsha",
        "Talgar",
        "Taldykorgan",
        "Taraz",
        "Tekeli",
        "Temir",
        "Temirtau",
        "Turkestan",
        "Uralsk",
        "Ust-Kamenogorsk",
        "Usharal",
        "Ushtobe",
        "Charsk",
        "Shalkar",
        "Shardara",
        "Shakhtinsk",
        "Shemonaikha",
        "Shu",
        "Shymkent",
        "Shchuchinsk"
    ])
async def call_weather_sity_key_en(call: types.CallbackQuery):
    a = "Almaty, KZ"

    call_sity = call.data
    call_index = call_sity[0]

    def_info_weather = InlineKeyboardMarkup()
    def_info_weather.add(InlineKeyboardButton(text=key_sity[0], callback_data=call.data))
    def_info_weather.insert(InlineKeyboardButton(text=key_sity[2], callback_data="deleter1"))
    def_info_weather.add(InlineKeyboardButton(text=key_sity[1], callback_data = call_index))
    if call.data == "Ekibastuz":
        a = "Ekibastuz, KZ"
        area = "Павлодарская область"
    elif call.data == "Emba":
        a = "Emba, KZ"
        area = "Актюбинская область"
    test = a
    if call.data == "Shchuchinsk":
        a = "Shchuchinsk, KZ"
        area = "Акмолинская область"
    if call.data == "Shalkar":
        a = "Shalkar, KZ"
        area = "Актюбинская область"
    elif call.data == "Shardara":
        a = "Shardara, KZ"
        area = "Южно-Казахстанская область"
    elif call.data == "Shardara":
        a = "Shardara, KZ"
        area = "Южно-Казахстанская область"
    elif call.data == "Shakhtinsk":
        a = "Shakhtinsk, KZ"
        area = "Карагандинская область"
    elif call.data == "Shemonaikha":
        a = "Shemonaikha, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Shu":
        a = "Shu, KZ"
        area = "Жамбыльская область"
    elif call.data == "Shymkent":
        a = "Shymkent, KZ"
        area = "Южно-Казахстанская область"
    if call.data == "Khromtau":
        a = "Khromtau, KZ"
        area = "Актюбинская область"
    if call.data == "Uralsk":
        a = "Uralsk, KZ"
        area = "Западно-Казахстанская область"
    elif call.data == "Ust-Kamenogorsk":
        a = "Ust-Kamenogorsk, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Usharal":
        a = "Usharal, KZ"
        area = "Алматинская область"
    elif call.data == "Ushtobe":
        a = "Ushtobe, KZ"
        area = "Алматинская область"
    if call.data == "Taiynsha":
        a = "Taiynsha, KZ"
        area = "Северо-Казахстанская область"
    elif call.data == "Talgar":
        a = "Talgar, KZ"
        area = "Алматинская область"
    elif call.data == "Taldykorgan":
        a = "Taldykorgan, KZ"
        area = "Алматинская область"
    elif call.data == "Taraz":
        a = "Taraz, KZ"
        area = "Жамбыльская область"
    elif call.data == "Tekeli":
        a = "Tekeli, KZ"
        area = "Алматинская область"
    elif call.data == "Temir":
        a = "Temir, KZ"
        area = "Актюбинская область"
    elif call.data == "Temirtau":
        a = "Temirtau, KZ"
        area = "Карагандинская область"
    elif call.data == "Turkestan":
        a = "Turkestan, KZ"
        area = "Южно-Казахстанская область"
    if call.data == "Saran":
        a = "Saran, KZ"
        area = "Карагандинская область"
    elif call.data == "Sarkand":
        a = "Sarkand, KZ"
        area = "Алматинская область"
    elif call.data == "Saryagash":
        a = "Saryagash, KZ"
        area = "	Южно-Казахстанская область"
    elif call.data == "Satpaev":
        a = "Satpaev, KZ"
        area = "Карагандинская область"
    elif call.data == "Semey":
        a = "Semey, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Sergeyevka":
        a = "Sergeyevka, KZ"
        area = "Северо-Казахстанская область"
    elif call.data == "Serebryansk":
        a = "Serebryansk, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Stepnogorsk":
        a = "Stepnogorsk, KZ"
        area = "Акмолинская область"
    elif call.data == "Stepnyak":
        a = "Stepnyak, KZ"
        area = "Акмолинская область"
    if call.data == "Ridder":
        a = "Ridder, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Rudny":
        a = "Rudny, KZ"
        area = "Восточно-Казахстанская область"
    if call.data == "Pavlodar":
        a = "Pavlodar, KZ"
        area = "Павлодарская область"
    elif call.data == "Petropavlovsk":
        a = "Petropavlovsk, KZ"
        area = "Северо-Казахстанская область"
    elif call.data == "Priozersk, KZ":
        a = "Priozersk, KZ"
        area = "Карагандинская область"
    if call.data == "Нур-Султан":
        a = "Nur-Sultan, KZ"
        area = "Акмолинская область"
    if call.data == "Makinsk":
        a = "Makinsk, KZ"
        area = "Акмолинская область"
    elif call.data == "Mamlyutka":
        a = "Mamlyutka, KZ"
        area = "Северо-Казахстанская область"
    if call.data == "Abai":# 1.
        a = "Abai, KZ"
        area = "Карагандинская область"
    elif call.data == "Akkol":# 2.
        a = "Akkol, KZ"
        area = "Акмолинская область"
    elif call.data == "Aksay":# 3.
        a = "Aksay, KZ"
        area = "Западно-Казахстанская область"
    elif call.data == "Aksu":# 4.
        a = "Aksu, KZ"
        area = "Павлодарская область"
    elif call.data == "Aktau":# 5.
        a = "Aktau, KZ"
        area = "Мангистауская область"
    elif call.data == "Aktobe":# 6.
        a = "Aktobe, KZ"
        area = "Актюбинская область"
    elif call.data == "Alga":# 7.
        a = "Alga, KZ"
        area = "Актюбинская область"
    elif call.data == "Almaty":# 8.
        a = "Almaty, KZ"
        area = "Алматинская область"
    elif call.data == "Altaysk":# 9.
        a = "Altaysk, KZ"
        area = "Кызылординская область"
    elif call.data == "Aralsk":# 10.
        a = "Aralsk, KZ"
        area = "Кызылординская область"
    elif call.data == "Arkalyk":# 11.
        a = "Arkalyk, KZ"
        area = "Костанайская область"
    elif call.data == "Arys":# 12.
        a = "Arys, KZ"
        area = "Южно-Казахстанская область"
    elif call.data == "Atbasar":# 13.
        a = "Atbasar, KZ"
        area = "Акмолинская область"
    elif call.data == "Atyrau":# 14.
        a = "Atyrau, KZ"
        area = "Атырауская область"
    elif call.data == "Ayagoz":# 15.
        a = "Ayagoz, KZ"
        area = "Восточно-Казахстанская область"
    if call.data == "Baikonur":
        a = "Baikonur, KZ"
        area = "Арендуется Российской Федерацией"
    elif call.data == "Balkhash":
        a = "Balkhash, KZ"
        area = "Карагандинская область"
    elif call.data == "Bulaevo":
        a = "Bulaevo, KZ"
        area = "Северо-Казахстанская область"
    if call.data == "Derzhavinsk":
        a = "Derzhavinsk, KZ"
        area = "Акмолинская область"
    if call.data == "Ereymentau":
        a = "Ereymentau, KZ"
        area = "Акмолинская область"
    elif call.data == "Esik":
        a = "Esik, KZ"
        area = "Алматинская область"
    elif call.data == "Esil":
        a = "Esil, KZ"
        area = "Акмолинская область"
    if call.data == "Zhanaozen":
        a = "Zhanaozen, KZ"
        area = "Мангистауская область"
    elif call.data == "Janatas":
        a = "Janatas, KZ"
        area = "Жамбыльская область"
    elif call.data == "Zharkent":
        a = "Zharkent, KZ"
        area = "Алматинская область"
    elif call.data == "Zhezkazgan":
        a = "Zhezkazgan , KZ"
        area = "Карагандинская область"
    elif call.data == "Zhem":
        a = "Zhem, KZ"
        area = "Актюбинская область"
    elif call.data == "Zhetisay":
        a = "Zhetisay, KZ"
        area = "Южно-Казахстанская область"
    elif call.data == "Zhetikara":
        a = "Zhetikara, KZ"
        area = "Костанайская область"
    if call.data == "Ereymentau":
        a = "Ereymentau, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Esik":
        a = "Esik, KZ"
        area = "Восточно-Казахстанская область"
    if call.data == "Kandyagash":
        a = "Kandyagash, KZ"
        area = "Актюбинская область"
    elif call.data == "Kapshagai":
        a = "Kapshagai, KZ"
        area = "Алматинская область"
    elif call.data == "Karaganda":
        a = "Karaganda, KZ"
        area = "Карагандинская область"
    elif call.data == "Karazhal":
        a = "Karazhal, KZ"
        area = "Карагандинская область"
    elif call.data == "Karatau":
        a = "Karatau, KZ"
        area = "Жамбыльская область"
    elif call.data == "Karkaralinsk":
        a = "Karkaralinsk, KZ"
        area = "Карагандинская область"
    elif call.data == "Kentau":
        a = "Kentau, KZ"
        area = "Южно-Казахстанская область"
    elif call.data == "Kokshetau":
        a = "Kokshetau, KZ"
        area = "Акмолинская область"
    elif call.data == "Kostanay":
        a = "Kostanay, KZ"
        area = "Костанайская область"
    elif call.data == "Kulsary":
        a = "Kulsary, KZ"
        area = "Атырауская область"
    elif call.data == "Kurchatov":
        a = "Kurchatov, KZ"
        area = "Восточно-Казахстанская область"
    elif call.data == "Kyzylorda":
        a = "Kyzylorda, KZ"
        area = "Кызылординская область"
    if call.data == "Lenger":
        a = "Lenger, KZ"
        area = "Южно-Казахстанская область"
    elif call.data == "Lisakovsk":
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
        tran = "Clouds ⛅ ️️"

    elif weather_main == "Mist":
        tran = "Mist ☁ ️"

    elif weather_main == "Fog":
        tran = "Fog ☁ ️"

    elif weather_main == "Smoke":
        tran = "Smoke ☁ ️"

    elif weather_main == "Clear":
        tran = "Clear ☀️"

    elif weather_main == "Snow":
        tran = "Snow 🥶"

    elif weather_main == "Rain":
        tran = "Rain 🌧"

    else:
        tran = "⁉️⁉️"

    p = "Sity " + call.data + "\n" + area + "\n" + tran + "\n" + str(int(weather_temp)) + " °C" + \
        "\n" + "Feels like " + \
        str(int(weather_feels_like)) + " °C" + "\n" + "Humidity" + str(weather_humidity) + \
        " %" + "\n" + "Visibility " + str(float(weather_visibility / 1000)) + " км." + "\n" + "Wind speed " + \
        str(weather_wind) + " m. s. "

    print(p)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, p, reply_markup=def_info_weather)

def register_message_handler_call_sity_info_key_en(dp: Dispatcher):
    dp.register_message_handler(call_weather_sity_key_en)