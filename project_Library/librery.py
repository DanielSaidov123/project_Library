from user import User
from book import Book

class Library:
    def __init__(self):
        self.list_of_books:list[Book]=[]
        self.list_of_users:list[User]=[]
    def return_list(self):
        return self.list_of_books
        
    def add_book(self,book:Book):
        self.list_of_books.append(book)

    def add_user(self,user:User):
        self.list_of_users.append(user)

    def borrow_book(self,user_id, book_isbn):
        for book in self.list_of_books:
            if book.ISBN==book_isbn:
                if book.is_available:
                    for user in self.list_of_users:
                        if user.id==user_id:
                            user.borrowed_books.append(book)
                            book.is_available=False
                        else:
                            print("user is not fuond")
                else:
                    print("is not available")

    def return_book(self,user_id, book_isbn):
        for book in self.list_of_books:
            if book.ISBN==book_isbn:
                book.is_available=True
                for user in self.list_of_users:
                    if user.id==user_id:
                        user.borrowed_books.remove(book)
            else:
                print("book is not fuond, check the book_isbn")
    
    def __str__(self):
        for user in self.list_of_users:
            print(f"{user.borrowed_books}")

    
    def list_available_books(self):
        new_books_available=[]
        for book in self.list_of_books:
            if book.is_available:
                new_books_available.append(book)
        return new_books_available

    def search_book(self,author):
        for book in self.list_of_books:
            if book.author==author:
                return f"book name-{book.title} writer-{book.author}"




   