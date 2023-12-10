class User:
    def __init__(self):
        self.id = None
        self.is_authorized = False

    def authorized(self, user_id):
        self.is_authorized = True
        self.id = user_id


user = User()
