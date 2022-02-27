from aiogram import executor

from data_config import dp
from start import start

start.register_message_handler_command_start1(dp)
from ru import ru1, ru2, ru_and_back3, back1ru, back2ru

ru1.register_message_handler_call_sity(dp)
ru2.register_message_handler_call_ABC_sity(dp)
ru_and_back3.register_message_handler_call_sity_info_key(dp)

back1ru.register_message_handler_call_dark(dp)
back2ru.register_message_handler_call_sity_1(dp)
from language import language_ru, language_en

language_ru.register_chosen_inline_handler_language_ru(dp)
language_en.register_chosen_inline_handler_language_en(dp)
from en import back1en, back2en, en1, en2, en_and_back3

back1en.register_message_handler_call_dark_en(dp)
back2en.register_message_handler_call_sity_3_en(dp)
en1.register_message_handler_call_sity_2en(dp)
en2.register_message_handler_call_ABC_sity_en(dp)
en_and_back3.register_message_handler_call_sity_info_key_en(dp)
from delet import deleter, deletr1

deleter.register_message_handler_call_delet_open(dp)
deletr1.register_message_handler_call_delet_open111(dp)
from Morse_Code_ru import back1_Mru, back2_Mru, ru1_M, ru2_M, ru_and_back3_M

back1_Mru.register_message_handler_call_dark_M(dp)
back2_Mru.register_message_handler_call_sity_1_M(dp)
ru1_M.register_message_handler_call_sity_M(dp)
ru2_M.register_message_handler_call_ABC_sity_m(dp)
ru_and_back3_M.register_message_handler_call_sity_info_key_mm(dp)

if __name__ == '__main__':
    executor.start_polling(dp)
