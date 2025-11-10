import json
from librery import Library

class File(Library):
    def store(self,list_of_books, list_of_users):
        with open( "list_of_books.json","w") as f:
            f.write()

