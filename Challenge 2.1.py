'''Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.'''


class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
    else:
      print("Invalid deposit amount. Please enter a positive value.")

  def withdraw(self, amount):
    if 0 < amount <= self.__account_balance:
      self.__account_balance -= amount
      print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
    else:
      print("Invalid withdrawal amount or insufficient funds.")

  def display_balance(self):
    print(f"Account Holder: {self.__account_holder_name}")
    print(f"Account Number: {self.__account_number}")
    print(f"Account Balance: ${self.__account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
  # Creating an instance of BankAccount
  my_account = BankAccount("123456789", "suresh", 1000.0)

  # Displaying the initial balance
  my_account.display_balance()

  # Making a deposit
  my_account.deposit(500.0)

  # Making a withdrawal
  my_account.withdraw(200.0)

  # Displaying the updated balance
  my_account.display_balance()
