import time

class User:
    book_list=[]

    def __init__(self,user_id):
        self.user_id=user_id

    def get_user_id(self):
        return self.user_id

    def lend_book(self,book):
        self.book_list.append(book)
        print(f"user {self.user_id} borrow the book {book.name}")

    def ret_book(self,book):
        self.book_list.remove(book)
        print(f"user {self.user_id} return the book {book.name}")

    def count_book(self):
        return len(self.book_list)
    
    def expired_book(self):
        for b in self.book_list:
            if b.date_end < time.time():
                print(f"{b.name} is expired. {(time.time()-b.date_end)//86400} days elapsed.")
        
class Book:
    def __init__(self,name,author,publisher,year,page,keyword):
        self.name=name
        self.author=author
        self.publisher=publisher
        self.year=year
        self.page=page
        self.keyword=keyword

    def lend(self,user_id,date):
        self.user_id=user_id
        self.date_start=date-604800
        self.date_end=date-86401

    def ret(self):
        self.user_id=None
        self.date_start=None
        self.date_end=None

hwan=User(1234)
rev=Book("Reversing core principle","Seungwon Lee","Insight",2018,1030,"information security")
rev.lend(hwan.get_user_id(),time.time())
hwan.lend_book(rev)
hwan.expired_book()
rev.ret()
hwan.ret_book(rev)