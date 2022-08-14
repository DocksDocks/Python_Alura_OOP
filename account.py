from customer import Customer
customer = Customer("Paulo")


class Account:
    def __init__(self, number, owner, balance, limit):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit
        self.__bank_code = "001"

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def statement(self):
        print("Account balance is: {}".format(self.__balance))
        
    def __can_withdraw(self, value):
        return value <= (self.__balance + self.__limit)
        
    def transfer(self, value, destination):
        if(self.__can_withdraw(value)):
            self.withdraw(value)
            destination.deposit(value)
            print("Your transaction was successful! The value of {} was sent to {}".format(value, destination.__owner))
        else:
            print("Sorry, the transaction could not be completed! Make sure you have the limit to do this transfer.")
            
    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit
        
    @staticmethod
    def bank_code():
        return "001"