#1.Bank Account Class
#Question: Create a class with methods deposit(), withdraw(), and display_balance().

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance: ₹", self.balance)


account = BankAccount("Annu", 5000)

account.display_balance()
account.deposit(2000)
account.withdraw(1000)
account.display_balance()

#2.Library Management System (OOP)
#Question: Create a program to add/remove books and issue/return books.

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append({"name": book, "issued": False})
            print(book, "added successfully.")
        else:
            print("Book already exists.")

    def remove_book(self, book):
        for item in self.books:
            if item["name"] == book:
                if item["issued"]:
                    print("Cannot remove an issued book.")
                    return
                self.books.remove(item)
                print(book, "removed successfully.")
                return
        print("Book not found.")

    def issue_book(self, book):
        for item in self.books:
            if item["name"] == book:
                if not item["issued"]:
                    item["issued"] = True
                    print(book, "issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, book):
        for item in self.books:
            if item["name"] == book:
                if item["issued"]:
                    item["issued"] = False
                    print(book, "returned successfully.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")

    def display_books(self):
        print("\nLibrary Books:")
        for item in self.books:
            status = "Issued" if item["issued"] else "Available"
            print(item["name"], "-", status)


library = Library()

library.add_book("Python Programming")
library.add_book("Java Programming")
library.add_book("C Programming")

library.display_books()

library.issue_book("Python Programming")
library.display_books()

library.return_book("Python Programming")
library.remove_book("Java Programming")

library.display_books()

#3.Calculator Class with Exception Handling
#Question: Create a calculator class that performs arithmetic operations and handles exceptions.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."


try:
    calc = Calculator()

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Addition:", calc.add(a, b))
    print("Subtraction:", calc.subtract(a, b))
    print("Multiplication:", calc.multiply(a, b))
    print("Division:", calc.divide(a, b))

except ValueError:
    print("Error: Please enter valid numbers.")