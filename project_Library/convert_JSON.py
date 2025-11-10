import json
from librery import Library
from user import User
from book import Book

class File(Library):
    def fank(self,list_book):
        new_list=[]
        for book in list_book:
            new_list.append(book.return_to_dict())
        return new_list
    

    def store(self,list_of_books):
        with open( "list_of_books.json","w") as f:
            json.dump(list_of_books,f)




b1=Book("daniel","ddddddd","1",True)
b2=Book("sa","ssssssss","2",True)
b3=Book("lev","gggggggg","3",True)


u=User("daniel","1")
l=Library()
l.add_book(b1)
l.add_book(b2)
l.add_book(b3)

l.add_user(u)
l.borrow_book("1","123")
f=File()
# l.return_book("1","123")
print(l.search_book("ddddddd"))
x=l.return_list()
y=f.fank(x)
print(f.store(y))

# print(l.__str__())

