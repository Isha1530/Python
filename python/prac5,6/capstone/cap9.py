import sqlite3
import csv

# Database setup
def initialize_db():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        author TEXT,
                        price REAL,
                        stock INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        book_id INTEGER,
                        quantity INTEGER,
                        total_price REAL,
                        FOREIGN KEY(book_id) REFERENCES books(id))''')
    conn.commit()
    conn.close()

# Add book to inventory
def add_book(title, author, price, stock):
    try:
        conn = sqlite3.connect("bookstore.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, price, stock) VALUES (?, ?, ?, ?)", 
                       (title, author, price, stock))
        conn.commit()
        conn.close()
        print("Book added successfully!")
    except Exception as e:
        print("Error adding book:", e)

# View all books
def view_books():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    for book in books:
        print(book)

# Place an order
def place_order(book_id, quantity):
    try:
        conn = sqlite3.connect("bookstore.db")
        cursor = conn.cursor()
        cursor.execute("SELECT price, stock FROM books WHERE id=?", (book_id,))
        book = cursor.fetchone()
        if book and book[1] >= quantity:
            total_price = book[0] * quantity
            cursor.execute("INSERT INTO orders (book_id, quantity, total_price) VALUES (?, ?, ?)", 
                           (book_id, quantity, total_price))
            cursor.execute("UPDATE books SET stock = stock - ? WHERE id=?", (quantity, book_id))
            conn.commit()
            print("Order placed successfully!")
        else:
            print("Insufficient stock or book not found!")
        conn.close()
    except Exception as e:
        print("Error placing order:", e)

# Export books to CSV
def export_books():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    with open("books.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Author", "Price", "Stock"])
        writer.writerows(books)
    print("Books exported to books.csv")

# Menu-driven interface
def menu():
    initialize_db()
    while True:
        print("\n1. Add Book\n2. View Books\n3. Place Order\n4. Export Books\n5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter stock quantity: "))
            add_book(title, author, price, stock)
        elif choice == '2':
            view_books()
        elif choice == '3':
            book_id = int(input("Enter book ID: "))
            quantity = int(input("Enter quantity: "))
            place_order(book_id, quantity)
        elif choice == '4':
            export_books()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
