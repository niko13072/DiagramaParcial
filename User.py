from collections import UserDict
from datetime import date
from ssl import _PasswordType


class User():
    
    def __init__(self, userid:int, password:str, registerDate:date ):
       self.Userid = userid 
       self.Password = password 
       self.RegisterDate = registerDate 
