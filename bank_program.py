"""
cd ~/Documents
python3 bank_program.py
"""

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposit {amount} units. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(f"Withdraw {amount} units. New balance: {self.balance}")
        else:
            print("Insufficient funds.")
    
    def transfer(self, other_account, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            other_account.balance = other_account.balance + amount
            print(f"Tranferred {amount} units to {other_account.account_number}. Your new balance: {self.balance}")
        else:
            print("Insufficient funds.")

account1 = BankAccount("123456", 1000)
account2 = BankAccount("789012", 2000)

while True:
    print("Select an action:")
    print("1. Transfer")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter the amount to transfer: "))
        account_number = input("Enter the recipient's account number: ")
        if account_number == account2.account_number:
            account1.transfer(account2, amount)
        else:
            print("Recipient account not found.")
    elif choice == 2:
        amount = float(input("Enter the amount to deposit: "))
        account1.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter the amount to withdraw: "))
        account1.withdraw(amount)
    elif choice == 4:
        print("Existing the program.")
        break
    else:
        print("Invalide choice. Please select a valid option.")