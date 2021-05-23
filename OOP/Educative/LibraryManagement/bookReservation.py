class BookReservation:
    def __init__(self, creation_date,status,book_item_barcode,member_id):
        self.__ceration_date = creation_date
        self.__status = status
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id
    
    def fetch_reservattion_details(self, barcode):
        None

class BookLending:
    def __init__(self, creation_details, due_date, book_item_barcode, member_id):
        self.__creation_details = creation_details
        self.__due_date = due_date
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id
        self.__return_date = None
    
    def lend_book(self,barcode,member_id):
        None
    
    def fetch_lending_details(self,barcode):
        None

class Fine:
    def __init__(self,creation_date,book_item_barcode,member_id):
        self.__creation_date = creation_date
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id
    
    def collect_fine(self,member_id,days):
        None
        


