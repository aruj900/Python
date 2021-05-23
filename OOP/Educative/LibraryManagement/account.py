from Educative.LibraryManagement.EnumsAndConstants import AccountStatus
from abc import ABC
import datetime

class Account(ABC):
    def __init__(self,id,password,person,status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__person = person
        self.__status = status

    def resetPassword(self):
        None

class Librarian(Account):
    def __init__(self, id, password, person, status):
        super().__init__(id, password, person, status=status)
    
    def addBookItem(self,bookItem):
        None
    
    def blockMember(self, member):
        None
    
class Member(Account):
    def __init__(self, id, password, person, status):
        super().__init__(id, password, person, status=status)
        self.__date_of_membership = datetime.date.today()
        self.__total_books_checkout = 0

    def get_total_books_checkout(self):
        return self.__total_books_checkout
    
    def reserve_book_item(self,book_item):
        None
    
    def increment_total_books_checkout(self):
        None
    
    