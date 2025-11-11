from user import User
from book import Book

class Library:
    def __init__(self):
        self.list_of_books:list[Book]=[]
        self.list_of_users:list[User]=[]
    def return_list(self):
        return self.list_of_books
        
    def add_book(self,book:Book):
        for bk in self.list_of_books:
            if book.ISBN == bk.ISBN:
                print(f"the ID {book.ISBN} already exists\n chose another name.")
                return 
        self.list_of_books.append(book)
        print("your book added!")

    def add_user(self,user:User):
        for ur in self.list_of_users:
            if user.id == ur.id:
                print(f"the ID {user.id} already exists\n chose another ID.")
                return 
        self.list_of_users.append(user)
        print("your name added!")  


    def borrow_book(self,user_id, book_isbn):
        book= None
        for b in self.list_of_books:
            if b.ISBN==book_isbn:
                book=b
        if book is None:
            print("book is not defind")
            return

        user= None
        for u in self.list_of_users:
            if u.id==user_id:
                user=u
        if user is None:
            print("user is not defind")
            return

        if book in user.borrowed_books:
            print("the book alerdy  in your books")
            return
        
        user.borrowed_books.append(book)
        book.is_available=False
        print("the book is borrow, enjoy ")

    def return_book(self,user_id, book_isbn):
        book= None
        for b in self.list_of_books:
            if b.ISBN==book_isbn:
                book=b
        if book is None:
            print("book is not defind")
            return

        user= None
        for u in self.list_of_users:
            if u.id==user_id:
                user=u
        if user is None:
            print("user is not defind")
            return

        if not book in user.borrowed_books:
            print("the book is not in user")
            return
        
        user.borrowed_books.remove(book)
        book.is_available=True
        print("the book is return, thank you") 
    
 
    def list_available_books(self):
        new_books_available=[]
        for book in self.list_of_books:
            if book.is_available:
                new_books_available.append(book)
        print(f"{[i.title for i in new_books_available]}")

    def search_book(self,author):
        for book in self.list_of_books:
            if book.author==author:
                print(f"book name-{book.title} writer-{book.author}")

    def get_list_of_user(self,user_name):
        for user in self.list_of_users:
            if user.name==user_name:
                print(f"the list book: {[i.title for i in user.borrowed_books]}")
                return



   