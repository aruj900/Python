from enum import Enum
from abc import ABC
class BookFormat(Enum):
    HARDCOVER, PAPERBACK, AUDIOBOOK, EBOOK, NEWSPAPER, MAGAZINE, JOURNAL = 1,2,3,4,5,6,7

class BookStatus(Enum):
    AVAILABLE, RESERVED, LOANED, LOST = 1,2,3,4

class ReservationStatus(Enum):
    WAITING, PENDING, CANCELED, NONE = 1,2,3,4

class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1,2,3,4,5

class Address:
    def __init__(self,street,city,state,zip_code,country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipCode = zip_code
        self.__country = country

class Person(ABC):
    def __init__(self,name,address,email,phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone

class Constants:
    MAX_BOOKS_ISSUED_TO_USER = 5
    MAX_LENDING_DAYS = 10



