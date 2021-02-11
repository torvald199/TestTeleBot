import quiz_config
import telebot


class Quiz:

    def __init__(self):
        self.quiz_dict = [quiz_config.quiz_1]
        self.true_answer = [quiz_config.quiz_1_answer_1]
        self.false_answer = [quiz_config.quiz_1_answer_2]

    def zagdka1(self):
        for i in range(0, len(self.quiz_dict)):
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton(f"{quiz_config.quiz_1_answer_1}", callback_data="point + 1")
            item2 = telebot.types.InlineKeyboardButton(f"{quiz_config.quiz_1_answer_2}", callback_data="zero")
            markup.add(item2, item1)
            telebot.bot.send_message(self.message.chat.id, f'{self.quiz_dict[i]}', reply_markup=markup)

