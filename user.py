class UserTelegramBot:

    def __init__(self):
        self.users = {}

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


class Quiz:

    def __init__(self):
        self.quiz_dict = {
            "Сколько будет 2+2?": 2
        }
