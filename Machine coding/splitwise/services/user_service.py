from splitwise.services.user_service_interface import UserServiceInterface
from splitwise.models.user import User

class UserService(UserServiceInterface):
    user_details = {}
    def add_user(self, id, name):
        user = User(id,name)
        UserService.user_details[id] = user
        return user