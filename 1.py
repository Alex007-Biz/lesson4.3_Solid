class UserManager():
    def __init__(self, user):
        self.user = user
    def change_user_name(self, user_name):
        self.user = user_name

    def save_user(self):
        file = open("users.txt", "a")
        file.write(self.user)
        file.close()
        