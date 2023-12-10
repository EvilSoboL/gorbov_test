class User:
    def __init__(self):
        self.id = None
        self.is_authorized = False
        self.is_admin = None

    def authorized(self, user_id, is_admin):
        self.is_authorized = True
        self.id = user_id
        self.is_admin = is_admin


user = User()
