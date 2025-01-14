from models.user_model import User

class UserController:
    @staticmethod
    def __init__(self):
        self.users = []

    def create_user(self, user_id, name, email):
        user = User(user_id, name, email)
        self.users.append(user)
        return user.to_dict()

    def get_users(self):
        return [user.to_dict() for user in self.users]