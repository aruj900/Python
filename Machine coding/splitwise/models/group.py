class Group:
    def __init__(self,id,name,members=[]):
        self.__id = id
        self.__name = name
        self.__members = members
    
    
    def set_id(self,id):
        self.__id = id
    
    def get_id(self):
        return self.__id
    
    def set_name(self,name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_members(self,members):
        self.__members = members
    
    def get_members(self):
        return self.__members
    
    