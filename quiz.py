import quiz_config
import telebot


class Quiz:

    def __init__(self):
        self.quiz_dict = quiz_config.quiz_1
        self.true_answer = quiz_config.quiz_1_answer_1
        self.false_answer = quiz_config.quiz_1_answer_2
        self.i = 0

    def zagdka1(self):
        # for i in range(0, len(self.quiz_dict)):
        #     if randint(1, 2) == 1:

                if self.i <= len(self.quiz_dict):
                    self.i += 1
                    markup = types.InlineKeyboardMarkup(row_width=2)
                    item1 = types.InlineKeyboardButton(f"{self.true_answer[self.i-1]}", callback_data="point + 1")
                    item2 = types.InlineKeyboardButton(f"{self.false_answer[self.i-1]}", callback_data="zero")
                    markup.add(item2, item1)
                    return bot.send_message(357720759, f'{self.quiz_dict[self.i-1]}', reply_markup=markup)

                else:
                    raise StopIteration

