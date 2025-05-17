class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades  # List of grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Average Grade: {self.average_grade():.2f}")


class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")
    
    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}, Account Type: {self.account_type}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


# Taking user input
name = input("Enter student name: ")
age = int(input("Enter student age: "))
grades = list(map(int, input("Enter grades separated by space: ").split()))
student1 = Student(name, age, grades)
student1.display_info()

account_number = input("Enter account number: ")
balance = float(input("Enter initial balance: "))
account_type = input("Enter account type: ")
account1 = BankAccount(account_number, balance, account_type)
account1.display_info()

amount = float(input("Enter amount to deposit: "))
account1.deposit(amount)
amount = float(input("Enter amount to withdraw: "))
account1.withdraw(amount)

person_name = input("Enter person name: ")
person_age = int(input("Enter person age: "))
person1 = Person(person_name, person_age)
person1.display_info()

student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_id = input("Enter student ID: ")
student2 = Student(student_name, student_age, student_id)
student2.display_info()