from abc import ABC,abstractclassmethod
class UserServiceInterface(ABC):
    @abstractclassmethod
    def add_user(self,id,name):
        pass
    