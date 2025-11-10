
class User:
    def __init__(self,name:str,id:str):
        self.name=name
        self.id=id
        self.borrowed_books=[]

    def return_users_dict(self):
        return {"name": self.name,
                "id":self.id,
                "borrowed_books":self.borrowed_books}

