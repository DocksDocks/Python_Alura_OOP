def create_account(number, owner, balance, limit):
    account = {"number" : number, "owner" : owner, "balance" : balance, "limit" : limit}
    return account

def deposit(account, amount):
    account['balance'] += amount

def withdraw(account, amount):
    account['balance'] -= amount

def statement(account):
    print("Account balance is: {}".format(account['balance']))