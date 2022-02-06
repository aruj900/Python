from abc import ABC,abstractclassmethod
class BillServiceInterface(ABC):
    @abstractclassmethod
    def add_bill(self,id,group_id,amount,contribution,paid_by):
        pass
    
    