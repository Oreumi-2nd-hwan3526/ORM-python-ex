class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
    
    def get_balance(self):
        return self.balance

account=BankAccount("123456789", 1000000)
print(account.account_number)
print(account.get_balance())