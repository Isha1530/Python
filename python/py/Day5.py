#oops
# to map with real world scenarios , we starting using objects in code
# this is oop
from jupyter_server.auth import passwd

from Day3 import student


# Procedure -> function -> oops

#class & object -> blueprint for object
# class Employee:
#     emp_name = "isha"
#
# e1 = Employee()
# print(e1.emp_name)
# e2 = Employee()
# print(e2.emp_name)

#constructor
# it is __init__ function to initialization
# when object is created it is called
# compiler has default init function

# class Student:
#     #default
#     def __init__(self):
#         print("Default constructor")
#
#     #parameterized
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print("Student init")
#
# s1=Student("isha",19)
# print(s1.name,s1.age)
# s2=Student("akshay",19)
# print(s2.name,s2.age)

#CLass & instance attributes
# 1->class 2->obj

# class Student:
#     #default
#     def __init__(self):
#         print("Default constructor")
#
#     #parameterized
#     def __init__(self,name,age):
#         self.name = name #object attribute
#         self.age = age
#         print("Student init")

      # name = "krisha" #class attribute
#
# s1=Student("isha",19)
# print(s1.name,s1.age)

# object attribute is higher importance

#methods in class

# class Hello:
#     def hello(self):
#         print("Hello World")
#         return 1
#
# h =Hello()
# a=h.hello()
# print(a)

#static method ->it is not use self parameter
# class

#abstaction -> hiding the implementation details of a class and only showing essential feature to the user

#encapsulation ->wrapping daya and method into single unit

# qus
# class Account:
#     def __init__(self, acno, balance):
#         self.acno = acno
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print("Rs. " , amount,"was deposited.")
#         print("total amount: ", self.get_balance())
#
#     def withdraw(self, amount):
#         self.balance -= amount
#         print("Rs. ", amount, "was withdrawn.")
#         print("total amount: ", self.get_balance())
#
#     def get_balance(self):
#         return self.balance
#
# ac1 = Account(123, 5000)
# ac1.deposit(1000)
# ac1.withdraw(2000)

#del keyword
# del obj_name

#private (like) attributes & methods
# not accessible outside the class

# class Account:
#     def __init__(self,acc_no,password):
#         self.acc_no = acc_no
#         self.__password = password
#     def reset_password(self):
#         self.__password = 'isha'
#         return self.__password
#
# ac1 = Account('123456','password')
# print(ac1.acc_no)
# print(ac1.reset_password())

#inheritance ->when onr class derives another class with its properties
# single inheritance
# class Car:
#     def start(self):
#         print("Starting")
#     def stop(self):
#         print("Stopping")
#
# class toyocard(Car):
#     def __init__(self, name):
#         self.name = name
#
# c1 = toyocard("fortuner")
# c1.start()

# 3 types of inheritance
# 1->single 2->multi-level 3->multple

# multi-level inheritance
# class Car:
#     def start(self):
#         print("Starting")
#     def stop(self):
#         print("Stopping")
#
# class Toyota(Car):
#     def __init__(self, brand):
#         self.brand = brand
#
# class Fortune(Toyota):
#     def __init__(self, type):
#         self.type = type
#
# c1 = Fortune("Ford")
# c1.start();

# multiple inheritance
# class A:
#     varA = "wlc A"
# class B:
#     varB = "wlc B"
# class C(A,B):
#     varC = "wlc C"
#
# c1 = C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)

#super method
# access methods of the parent class

# class Car:
#     def __init__(self,type):
#         self.type = type
#     def start(self):
#         print("Starting")
#     def stop(self):
#         print("Stopping")
#
# class Toyota(Car):
#     def __init__(self, name,type):
#         self.name = name
#         super().__init__(type)
#         super().stop()
#
# c1 = Toyota("BMW" , "elc")
# print(c1.type)
# c1.start()

#class method

# class Person:
#     name = "isha"
#     @classmethod
#     def changeName(self, name):
#         self.name = name
#
# p1 = Person()
# p1.changeName("akshay")
# print(p1.name)
# print(Person.name)

# property
# class Student:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     @property
#     def sum(self):
#         return self.a+self.b
#
# s1 = Student(10,20)
# print(s1.sum)
# s1.a = 20
# print(s1.sum)

#Polymorphism : Operator overloading

# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.real = realpart
#         self.imag = imagpart
#     def showno(self):
#         print(self.real,"i ", self.imag,"j ")
#
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)
#     def __sub__(self, other):
#         return Complex(self.real - other.real, self.imag - other.imag)
#
# num1 = Complex(3,4)
# print(num1.showno())
# num2 = Complex(5,6)
# print(num2.showno())
# num3 = num1 + num2
# print(num3.showno())