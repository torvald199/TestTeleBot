import quiz_config
import telebot
from telebot import types
import config
import iterator


bot = telebot.TeleBot(config.TOKEN)


class UserTelegramBot:

    def __init__(self):
        self.users = {}
        self.quiz_dict = quiz_config.quiz_1
        self.true_answer = quiz_config.quiz_1_answer_1
        self.false_answer = quiz_config.quiz_1_answer_2
        self.i = 0

    # quiz_dict = iterator.QuizIterator(quiz_config.quiz_1)
    # true_answer = iterator.QuizIterator(quiz_config.quiz_1_answer_1)
    # false_answer = iterator.QuizIterator(quiz_config.quiz_1_answer_2)

    # add new user
    def add_user(self, user_id):
        if user_id not in self.users:
            self.users[user_id] = 0

    # add 1 point for user
    def add_point(self, user_id):
        points = self.users[user_id]
        self.users[user_id] = points + 1

    # make user point 0
    def zero_point(self, user_id):
        self.users[user_id] = 0

    def zagdka1(self, user_id):
        for i in range(0, len(self.quiz_dict)):

        #     if randint(1, 2) == 1:
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton(f"{self.true_answer[i]}", callback_data="point + 1")
                item2 = types.InlineKeyboardButton(f"{self.false_answer[i]}", callback_data="zero")
                markup.add(item2, item1)
                return bot.send_message(user_id, f'{self.quiz_dict[i]}', reply_markup=markup)
                #yield
