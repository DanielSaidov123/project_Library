import json
import csv
from librery import Library
from user import User
from book import Book

class File:
    def data_books_builder(self,list_book:list[Book]):
        new_list=[]
        for book in list_book:
            new_list.append(book.return_to_dict())
        return new_list
    
    def data_users_builder(self,list_user:list[User]):
        new_list=[]
        for user in list_user:
            new_list.append(user.return_users_dict())
        return new_list
    

    def store_book(self,list_of_books):
        with open( "list_of_books.json","w") as f:
            json.dump(list_of_books,f,indent=4)

    def read_book(self):
        with open("list_of_books.json","r") as r:
            dict_store=json.load(r)
        return dict_store
    
    def store_user(self,list_of_users):
        with open( "list_of_users.json","w") as f:
            json.dump(list_of_users,f,indent=3)

    def read_user(self):
        with open("list_of_users.json","r") as r:
            dict_store=json.load(r)
        return dict_store
    
    def create_csv_file_of_books(self,list_of_books):
        with open('file_books.csv', 'w', newline='') as csvfile:
            fieldnames = ['title', 'author', 'ISBN', 'is_available']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(list_of_books)

    def create_csv_file_of_users(self,list_of_users):
        with open('file_users.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'id', 'borrowed_books']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(list_of_users)
    

     
# b1=Book("daniel","dsf","312432")
# b2=Book("dani","dsf","2432")
# b3=Book("da","sf","2432")

# u1=User("dd","333")
# l1=Library()
# f1=File()
# l1.add_book(b1)
# l1.add_book(b2)
# l1.add_book(b3)
# l1.add_user(u1)
# d=f1.data_books_builder(l1.list_of_books)
# a=f1.data_users_builder(l1.list_of_users)
# f1.create_csv_file_of_books(d)
# f1.create_csv_file_of_users(a)
# # f1.store_book(d)

# # f1.store_user(a)


# # g=f1.read_book()
# # print(g)
# # o=f1.read_user()
# # print(o)







