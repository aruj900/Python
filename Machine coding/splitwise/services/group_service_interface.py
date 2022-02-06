from abc import ABC,abstractclassmethod
class GroupServiceInterface(ABC):
    @abstractclassmethod
    def add_group(self,id,name,members):
        pass
    