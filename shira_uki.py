from aiogram import executor

from config import dp
from functions.комманда_стар_1 import start

start.register_message_handler_command_start(dp)
from functions.call_выбор_города_по_Б_2 import call_sity_ABC

call_sity_ABC.register_message_handler_call_sity(dp)
from functions.call_выбор_города_по_Б_2.back import back

back.register_message_handler_call_dark(dp)
from functions.call_выбор_города_3 import call_sity_A

call_sity_A.register_message_handler_call_ABC_sity(dp)
from functions.call_выбор_города_3.bark import call_sity_ABC_1

call_sity_ABC_1.register_message_handler_call_sity_1(dp)
from functions.call_sity_4 import sity

sity.register_message_handler_call_sity_info_key(dp)
from functions.delet import delet

delet.register_message_handler_call_delet_open(dp)
from functions.язык.язык_ru import язык1

язык1.register_message_handler_call_lang1(dp)
from functions.язык.комманда_стар_1_en import en_start

en_start.register_message_handler_en_start(dp)
from functions.язык.call_выбор_города_по_Б_2_en import call_sity_ABC

call_sity_ABC.register_message_handler_call_sity_en(dp)
from functions.язык.call_выбор_города_по_Б_2_en.back import back

back.register_message_handler_call_dark_en(dp)
from functions.язык.ru.язык_en import язык

язык.register_message_handler_call_lang_en(dp)
from functions.язык.ru import start1

start1.register_message_handler_command_start1(dp)
from functions.язык.call_sity_en import sity_1

sity_1.register_message_handler_call_sity_info_key_en(dp)
from functions.язык.call_выбор_города_по_Б_2_en import call_sity_ABC

call_sity_ABC.register_message_handler_call_sity_en(dp)
from functions.язык.call_выбор_города import call_sity_A

call_sity_A.register_message_handler_call_ABC_sity_en(dp)
from functions.язык.call_выбор_города.bark import call_sity_ABC_1

call_sity_ABC_1.register_message_handler_call_sity_en(dp)
from functions.язык.Morse_Code import Morse

Morse.register_message_handler_morze_ABC(dp)
from functions.язык.Morse_Code import sity_m

sity_m.register_message_handler_call_ABC_sity_m(dp)
from functions.язык.Morse_Code import SITY_MM

SITY_MM.register_message_handler_call_sity_info_key_mm(dp)
if __name__ == '__main__':
    executor.start_polling(dp)
