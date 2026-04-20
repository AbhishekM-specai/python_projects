#Bank account system
'''
class BankAccount:
    def __init__(self, name, account_number,balance=0 ):
        self.name = name
        self.account_number = account_number
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print("You deposited", amount,"your remaining balance is:",self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("You withdrawn",amount,"your remaining balance is:",self.balance)
        else:
            print("insufficient balance")


    def check_balance(self):
        print("your remaining balance is:",self.balance)

a=BankAccount(name=input("Enetr your name:"),
              account_number=int(input("Enter your account number:")))
a.deposit(int(input("Enter your deposite amount:")))
a.withdraw(int(input("Enter your withdrawn amount:")))
a.check_balance()
'''''