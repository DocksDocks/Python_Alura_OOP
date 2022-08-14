class Account:
    def __init__(self, number, owner, balance, limit):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def statement(self):
        print("Account balance is: {}".format(self.__balance))
        
    def transfer(self, value, destination):
        if(self.__balance - value > -(self.__limit) ):
            self.withdraw(value)
            destination.deposit(value)
            print("Your transaction was successful! The value of {} was sent to {}".format(value, destination.__owner))
        else:
            print("Sorry, the transaction could not be completed! Make sure you have the limit to do this transfer.")