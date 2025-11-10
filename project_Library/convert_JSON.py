import json
from librery import Library
from user import User
from book import Book

class File(Library):
    def data_books_nuilder(self,list_book:list[Book]):
        new_list=[]
        for book in list_book:
            new_list.append(book.return_to_dict())
        return new_list
    
    def data_users_nuilder(self,list_user:list[User]):
        new_list=[]
        for user in list_user:
            new_list.append(user.return_users_dict())
        return new_list
    

    def store(self,list_of_books):
        with open( "list_of_books.json","a") as f:
            json.dump(list_of_books,f,indent=4)

    # def store(self,list_of_users):
    #     with open( "list_of_users.json","w") as f:
    #         json.dump(list_of_users,f,indent=3)






