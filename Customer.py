from numpy import double
from User import User

class customer(User):

    def __init__(self, user:User, name:str, address:str, customerld:int, accountBalance:double):
        self.User = user 
        self.Name = name 
        self.Address = address
        self.Customerld = customerld
        self.AccountBalance = accountBalance