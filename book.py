class Book:
    def __init__(self, title, author, ISBN, is_available : bool):
        self. title = title
        self.author = author
        self.ISBN = ISBN
        self.is_available = is_available

    
    def __str__(self):
        return f"your choice: {self.title} by:{self.author} status: {self.is_available}"
    

    