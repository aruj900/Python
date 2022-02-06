from splitwise.services.bill_service_interface import BillServiceInterface
from splitwise.models.bill import Bill

class BillService(BillServiceInterface):
    bill_details = {}
    def add_bill(self, id, group_id, amount, contribution, paid_by):
        bill = Bill(id,group_id,amount,contribution,paid_by)
        BillService.bill_details[id] = bill
        return bill
        
        