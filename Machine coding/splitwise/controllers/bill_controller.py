class BillController:
    
    def __init__(self,bill_service):
        self.bill_service = bill_service
    
    def add_bill(self,id,group_id,amount,contribution,paid_by):
        return self.bill_service.add_bill(id,group_id,amount,contribution,paid_by)
    
    def get_user_balance(self,user_id):
        balance = 0
        for bill_id in self.bill_service.bill_details:
            bill = self.bill_service.bill_details.get(bill_id)
            if user_id in bill.get_contribution():
                balance = balance - bill.get_contribution()[user_id]
            if user_id in bill.get_paid_by():
                balance = balance + bill.get_paid_by()[user_id]
        return balance
        