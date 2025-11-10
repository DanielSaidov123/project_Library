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
        print(book.ISBN)
    def add_user(self,user:User):
        self.list_of_users.append(user)

    def borrow_book(self,user_id, book_name):
        for book in self.list_of_books:
            if book.title==book_name:
                if book.is_available:
                    for user in self.list_of_users:
                        if user.id==user_id:
                            user.borrowed_books.append(book)
                            book.is_available=False
                        else:
                            print("user is not fuond")
                else:
                    print("is not available")

    def return_book(self,user_id, book_name):
        for book in self.list_of_books:
            if book.title==book_name:
                for user in self.list_of_users:
                    if user.id==user_id:
                        user.borrowed_books.remove(book)
                        book.is_available=True
            else:
                print("book is not fuond, check book name")
    
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
                print(f"book name-{book.title} writer-{book.author}")




# b1=Book("daniel","ddddddd" )
# b2=Book("123","ssssssss" )
# b3=Book("lev","gggggggg")


# u=User("1","1")
# l=Library()
# l.add_book(b1)
# l.add_book(b2)
# l.add_book(b3)

# l.add_user(u)
# l.borrow_book("1","123")
# # f=File()
# l.return_book("1","123")
# # print(l.search_book("ddddddd"))
# # x=l.return_list()
# # y=f.fank(x)
# # print(f.store(y))

# # print(l.__str__())  