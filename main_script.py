import config
import telebot
from telebot import types
from user import UserTelegramBot

bot = telebot.TeleBot(config.TOKEN)

my_users = UserTelegramBot()


@bot.message_handler(commands=['start'])
def welcome(message):
    """
    'Welcome' function. Create 'Welcome message', create keyboard button.
    :return: 'welcome message'
    """
    my_users.add_user(message.chat.id)
    my_users.add_point(message.chat.id)

    print(message.chat.id, message.chat.first_name, message.chat.last_name, message.chat.username)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Твой счет")
    item2 = types.KeyboardButton("Как дела?")

    markup.add(item1, item2)
    bot.send_message(message.chat.id,
                     "Добро пожаловать {0.first_name}!\n".format(message.from_user, bot.get_me()), reply_markup=markup)


@bot.message_handler(commands=['make_points_0'])
def point_zero(message):
    """
    Make score users equal zero
    :return: zero points
    """
    my_users.zero_point(message.chat.id)
    bot.send_message(message.chat.id, f"Твой счет = {my_users.users[message.chat.id]}")


@bot.message_handler(content_types=['text'])
def start(message):
    # Повторение присланого сообщения
    # bot.send_message(message.chat.id, message.text)

    try:
        if message.chat.type == "private":
            if message.text == "Твой счет":

                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Обнулить счет", callback_data="make point zero")

                markup.add(item1)
                bot.send_message(message.chat.id, f"Твой счет = {my_users.users[message.chat.id]}", reply_markup=markup)

                my_users.add_user(message.chat.id)
                my_users.add_point(message.chat.id)

            elif message.text == "Как дела?":

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Хорошо", callback_data="good")
                item2 = types.InlineKeyboardButton("Плохо(", callback_data="bad")

                markup.add(item1, item2)

                bot.send_message(message.chat.id, "Отлично, а твои?", reply_markup=markup)
            else:
                bot.send_message(message.chat.id, 'я даже и не знаю что ответить')
            #else:
                #bot.send_message((958924219(кесин)), message.text)
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

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😝)",
                                  reply_markup=None)

    except Exception as ex:
        print(repr(ex))


# RUN
bot.polling(none_stop=True)
