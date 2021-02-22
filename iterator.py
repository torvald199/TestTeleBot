import quiz_config


class QuizIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index = self.index + 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


class QuizListAsk:
    def __init__(self):
        self.quiz_list_ask = quiz_config.quiz_1

    def __iter__(self):
        return QuizIterator(self.quiz_list_ask)


class QuizListAns1:
    quiz_list_ans1 = quiz_config.quiz_1_answer_1

    def __iter__(self):
        return QuizIterator(self.quiz_list_ans1)


class QuizListAns2:
    quiz_list_ans2 = quiz_config.quiz_1_answer_2

    def __iter__(self):
        return QuizIterator(self.quiz_list_ans2)


quiz = QuizIterator(quiz_config.quiz_1)
ans1 = QuizIterator(quiz_config.quiz_1_answer_1)
ans2 = QuizIterator(quiz_config.quiz_1_answer_2)

