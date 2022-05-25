import email
from User import User

class Administrador(User):
    def __init__(self, user:User, name:str, email:str):
        self.User = user 
        self.Name = name
        self.Email = email
    