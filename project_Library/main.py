from librery import Library
from user import User
from book import Book
from convert_JSON import File
l1=Library()
choice = None
while choice != "8":

    print("1. Add Book\n2. Add User\n3. Borrow Book\n4. return book\n5. available books\n6. search book\n7. get your borrowed books \n8. Save & Exit")
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
        isbn_book = input("enter your book id: ")
        l1.borrow_book(user_id, isbn_book)

    elif choice == "4":
        user_id = input("enter your ID: ")
        isbn_book = input("enter your book id: ")
        l1.return_book(user_id, isbn_book)

    elif choice == "5":
        l1.list_available_books()

    elif choice == "6":
        author = input("enter your fevorit author: ")
        if not isinstance(author,str):
            print("its not type of string, enter another name.")
        else:
            l1.search_book(author)

    elif choice == "7":
        get_user_name = input("enter your user name: ")
        l1.get_list_of_user(get_user_name)
        


    elif choice == "8":
        f1=File()
        try:
            json_book_info=f1.read_book()
            json_user_info=f1.read_user()

            list_of_dict_books=f1.data_books_builder(l1.list_of_books)
            merge_lists_book=list_of_dict_books+json_book_info
            f1.store_book(merge_lists_book)

            list_of_dict_users=f1.data_users_builder(l1.list_of_users)
            merge_lists_user=list_of_dict_users+json_user_info
            f1.store_user(merge_lists_user)
        except:
            list_of_dict_books=f1.data_books_builder(l1.list_of_books)
            f1.store_book(list_of_dict_books)

            list_of_dict_users=f1.data_users_builder(l1.list_of_users)
            f1.store_user(list_of_dict_users)

        print("Hope you enjoyed it, see you later.")
        break
    



