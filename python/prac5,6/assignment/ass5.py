# Superclass demonstrating Polymorphism
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Subclass Circle overriding calculate_area
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.1416 * self.radius * self.radius

# Subclass Rectangle overriding calculate_area
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Class demonstrating Encapsulation
class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

# Main function to test the implementation
def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    print("Circle Area:", circle.calculate_area())
    print("Rectangle Area:", rectangle.calculate_area())

    book = Book("Python Programming", "Guido van Rossum", "1234567890")
    print("Book Title:", book.get_title())
    print("Book Author:", book.get_author())
    print("Book ISBN:", book.get_isbn())

if __name__ == "__main__":
    main()