# : Build a Bank Account system with:
# Base Account class with deposit/withdraw methods
# SavingsAccount and CheckingAccount subclasses
# Property decorators for balance validation
# Custom exceptions for insufficient funds
class InsufficientFund(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance += amount
        print(f"Deposited {amount} New balance: {self._balance}")

    def withdraw(self, amount):
        
        if self._balance < amount:
            raise InsufficientFund("Insufficient Balance")
        
        self._balance -= amount
        print(f"Withdrawn {amount} New Balance {self._balance}")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

class SavingsAccount(BankAccount):
    def __init__(self, balance, interest = 0.1):
        super().__init__(balance)
        self.interest = interest

    def interest_add(self):
        self.interest_amount = self.balance * self.interest
        self._balance += self.interest_amount
        print(f"Interest({self.interest_amount}) added to balance new balance {self._balance}")

class CheckingAccount(BankAccount):
    def __init__(self, balance, overdraft_limit = 500):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    # Overriding withdraw for overdraft
    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            raise InsufficientFund("Exceeded overdraft limit")
        self._balance -= amount
        print(f"Withdrawn {amount}. New balance: {self._balance}")


    
