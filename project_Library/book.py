class Book:
    def __init__(self, title, author,ISBN):
        self. title = title
        self.author = author
        self.ISBN =ISBN
        self.is_available = True

    
    def __str__(self):
        return f"your choice: {self.title} by:{self.author} status: {self.is_available}"
    
    def return_to_dict(self):
        return{"title":self.title,
               "author":self.author,
               "ISBN":self.ISBN,
               "is_available":self.is_available}

    