import random
from datetime import datetime
class Book:
    __number=100

    def __init__(self,title:str,author:str,number:int) -> None:
        self.title=title
        self.author=author
        self.reference_number=Book.generate_ref_number()
        self.number=number
    
    def availability(self):
        return self.number>0
    
    @staticmethod
    def generate_ref_number():
        res= ''.join(random.choice(['a','b','c','d'])for i in range(5))
        return f'LIB_ID_{res}'
class human:
    def __init__(self,name:str,age:int) -> None:
        self.name=name
        self.age=age
    def borrow_book(self,book:Book):
        if isinstance(book,Book) and book.availability():
            self.borrowed_books.append(book)
        else:
            print("I couldn't recognize that book! ")
class patron(human):
    def __init__(self, name: str, age: int) -> None:
        
        super().__init__(name, age)

class Transaction:
    def __init__(self,book,patron,library) -> None:
        self.book=book
        self.patron=patron
        self.library=library
        self.ledger={}
        
    def record_book_borrow(self,book,patron):
        self.ledger[f'{self.patron}-{str(datetime.today())}']=f'{self.book},{self.patron},{str(datetime.today())}'

    def record_book_return(self,book,patron):
        self.ledger.pop(f'{self.patron}-{str(datetime.today())}')

class Library:
    def __init__(self) -> None:
        self.books={}
    def add_book_toshel