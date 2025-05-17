class Book:
    def __init__(self, title, author, genre, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
    
    def get_details(self):
        return f"{self.title} by {self.author} - {self.genre}: ${self.price}"

class EBook(Book):
    def __init__(self, title, author, genre, price, file_size):
        super().__init__(title, author, genre, price)
        self.file_size = file_size
    
    def get_details(self):
        return f"E-Book: {super().get_details()} (File size: {self.file_size}MB)"

class PrintedBook(Book):
    def __init__(self, title, author, genre, price, weight):
        super().__init__(title, author, genre, price)
        self.weight = weight
    
    def get_details(self):
        return f"Printed Book: {super().get_details()} (Weight: {self.weight}kg)"

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.books = []
        self.total_price = 0
    
    def add_book(self, book):
        self.books.append(book)
        self.total_price += book.price
    
    def get_order_summary(self):
        order_details = f"Order for {self.customer_name}:\n"
        order_details += "\n".join([book.get_details() for book in self.books])
        order_details += f"\nTotal Price: ${self.total_price}"
        return order_details

# Example Usage
book1 = EBook("Python Basics", "John Doe", "Programming", 10, 2)
book2 = PrintedBook("OOP in Python", "Jane Smith", "Programming", 20, 0.5)

order = Order("Alice")
order.add_book(book1)
order.add_book(book2)

print(order.get_order_summary())
