class Bill:
    def __init__(self,id,group_id,amount,contribution,paid_by):
        self.__id = id
        self.__group_id = group_id
        self.__amount = amount
        self.__contribution = contribution
        self.__paid_by = paid_by
    
    
    def set_id(self,id):
        self.__id = id
    
    def get_id(self):
        return self.__id
    
    def set_group_id(self,group_id):
        self.__group_id = group_id
    
    def get_group_id(self):
        return self.__group_id
    
    def set_amount(self,amount):
        self.__amount = amount
    
    def get_amount(self):
        return self.__amount
    
    def set_contribution(self,contribution):
        self.__contribution = contribution
    
    def get_contribution(self):
        return self.__contribution
    
    def set_paid_by(self,paid_by):
        self.__paid_by = paid_by
    
    def get_paid_by(self):
        return self.__paid_by
    
    