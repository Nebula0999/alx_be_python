# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False  # Insufficient funds or invalid withdrawal amount

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")
