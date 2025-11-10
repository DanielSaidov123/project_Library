from librery import Library
from user import User
from book import Book
from convert_JSON import File
l1=Library()
choice = None
while choice != "7":

    print("1. Add Book\n2. Add User\n3. Borrow Book\n4. return book\n5. available books\n6. search book\n7. Save & Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("enter the name of the book you want to add: ")
        author = input("enter the name of the author you want to add: ")
        isbn = input("enter the ID of the book you want to add: ")

        if not isinstance(title,str) or not isinstance(author,str):
            print("its not type of string, enter another info.")
        else:
            b1 = Book(title, author,isbn)
            l1.add_book(b1)            
            print("your book added!")

    elif choice == "2":
        name = input("enter your name: ")
        id = input("enter your ID: ")
        if not isinstance(name,str) or not isinstance(id,str):
            print("its not type of string, enter another name.")
        else:
            u1 = User(name, id)
            l1.add_user(u1)
            print("your name added!")  

    elif choice == "3":
        user_id = input("enter your ID: ")
        name_book = input("enter your book title: ")
        if not isinstance(user_id,str) or not isinstance(name_book,str):
            print("its not type of string, enter another name\id.")
        else:
            l1.borrow_book(user_id, name_book)
            print("the book is borrow, enjoy ")

    elif choice == "4":
        user_id = input("enter your ID: ")
        name_book = input("enter your book title: ")
        if not isinstance(user_id,str) or not isinstance(name_book,str):
            print("its not type of string, enter another name\id.")
            
        else:
            l1.return_book(user_id, name_book)
            print("the book is return, thank you") 

    elif choice == "5":
        print(l1.list_available_books())

    elif choice == "6":
        author = input("enter your fevorit author: ")
        if not isinstance(author,str):
            print("its not type of string, enter another name.")
        else:
            l1.search_book(author)

    elif choice == "7":
        f1=File()
        list_of_dict=f1.data_books_nuilder(l1.return_list())
        f1.store(list_of_dict)
        print("Hope you enjoyed it, see you later.")
        break
    



            





    elif choice == "7":
    # save data and exit
        break
    else:
        print("Invalid choice, try again.")