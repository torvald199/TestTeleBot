import config
import telebot
from telebot import types
from user import UserTelegramBot
import logging
from info_button import INFO
import quiz_config
from random import randint
import iterator
import requests


bot = telebot.TeleBot(config.TOKEN)

logging.basicConfig(filename='app_log.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

# message for me when bot starting work
logging.info("Start program")
requests.post(f'https://api.telegram.org/bot{config.TOKEN}/sendMessage?chat_id={config.MY_ID}&text=Online')

my_users = UserTelegramBot()


@bot.message_handler(commands=['start'])
def welcome(message):
    """
    'Welcome' function. Create 'Welcome message', create keyboard button.
    :return: 'welcome message'
    """
    my_users.add_user(message.chat.id)

    logging.info(f"New user:{message.chat.id};{message.chat.username};"
                 f"{message.chat.first_name};{message.chat.last_name}")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("Твой счет")
    item2 = types.KeyboardButton("Как дела?")
    item3 = types.KeyboardButton("Начать тест")

    # Перед релизом удалить "item4"
    item4 = types.KeyboardButton("/start")

    # Перед релизом удалить "item4"
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,
                     "Добро пожаловать {0.first_name}!\n".format(message.from_user, bot.get_me()), reply_markup=markup)
    bot.send_message(message.chat.id, f'{INFO}')



@bot.message_handler(commands=['info'])
def get_info(message):
    bot.send_message(message.chat.id, INFO)


@bot.message_handler(commands=['make_points_0'])
def point_zero(message):
    """
    Make score users equal zero
    :return: zero points
    """
    my_users.zero_point(message.chat.id)
    bot.send_message(message.chat.id, f"Твой счет = {my_users.users[message.chat.id]}")
            # else:
            #     markup = types.InlineKeyboardMarkup(row_width=2)
            #     item1 = types.InlineKeyboardButton(f"{self.true_answer[i]}", callback_data="point + 1")
            #     item2 = types.InlineKeyboardButton(f"{self.false_answer[i]}", callback_data="zero")
            #     markup.add(item1, item2)
            #     bot.send_message(357720759, f'{self.quiz_dict[i]}', reply_markup=markup)

@bot.message_handler(commands=['quiz'])
def quiz3(message):
    bot.send_message(message.chat.id, "1")
    bot.register_next_step_handler(message.chat.id, UserTelegramBot.zagdka1(self=message.chat.id))
# def quiz_start2(message):
#    for item in quiz_config.quiz_1:
#        markup = types.InlineKeyboardMarkup(row_width=2)
#       for ans1 in quiz_config.quiz_1_answer_1:
#            item1 = types.InlineKeyboardButton(f"{ans1}", callback_data="point + 1")
#        for ans2 in quiz_config.quiz_1_answer_2:
#            item2 = types.InlineKeyboardButton(f"{ans2}", callback_data="zero")
#        markup.add(item2, item1)
#        bot.send_message(message.chat.id, f'{item}', reply_markup=markup)

# def quiz_start1(message):
#     #if randint(1, 2) == 1:
#     for item in quiz_config.quiz_1:
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         item1 = types.InlineKeyboardButton(f"{quiz_config.quiz_1_answer_1}", callback_data="point + 1")
#         item2 = types.InlineKeyboardButton(f"{quiz_config.quiz_1_answer_2}", callback_data="zero")
#         markup.add(item2, item1)
#         bot.send_message(message.chat.id, f'{item}', reply_markup=markup)

    # else:
    #     markup = types.InlineKeyboardMarkup(row_width=2)
    #     item1 = types.InlineKeyboardButton(f"{quiz_config.quiz_2_answer_1}", callback_data="point + 1")
    #     item2 = types.InlineKeyboardButton(f"{quiz_config.quiz_2_answer_2}", callback_data="zero")
    #     markup.add(item1, item2)
    #     bot.send_message(message.chat.id, f'{quiz_config.quiz_2}', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def start(message):
    try:
        if message.chat.type == "private":
            if message.text == "Твой счет":

                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Обнулить счет", callback_data="make point zero")

                markup.add(item1)
                bot.send_message(message.chat.id, f"Твой счет = {my_users.users[message.chat.id]}", reply_markup=markup)

            elif message.text == "Как дела?":

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Хорошо", callback_data="good")
                item2 = types.InlineKeyboardButton("Плохо(", callback_data="bad")

                markup.add(item1, item2)

                bot.send_message(message.chat.id, "Отлично, а твои?", reply_markup=markup)

            elif message.text == "Начать тест":
                bot.send_message(message.chat.id, f'ДОЛЖЕН НАЧАТЬСЯ ТЕСТ')
                vopros = UserTelegramBot.zagdka1(user_id=message.chat.id)
                next(vopros)
            else:
                bot.send_message(message.chat.id, 'я даже и не знаю что ответить')
                logging.info(f'пользователь {message.chat.username} написал {message.text}')

    except Exception as ex:
        print(ex)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "good":
                bot.send_message(call.message.chat.id, "Вот и итлично))")
            elif call.data == "bad":
                bot.send_message(call.message.chat.id, "Почему?")
            elif call.data == "make point zero":
                my_users.zero_point(call.message.chat.id)
                bot.send_message(call.message.chat.id, f"Твой счет = {my_users.users[call.message.chat.id]}")
            elif call.data == "point + 1":
                my_users.add_point(call.message.chat.id)
                # next(my_users.zagdka1(call.message.chat.id))
            elif call.data == "zero:":
                # next(my_users.zagdka1(call.message.chat.id))

                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="😝)", reply_markup=None)

    except Exception as ex:
        print(repr(ex))


# RUN
bot.polling(none_stop=True)
