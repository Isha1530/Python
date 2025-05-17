# Online Book Rental System

# Store book information as a dictionary
books = {
    "The Great Gatsby": ("F. Scott Fitzgerald", "Fiction", 5.0),
    "To Kill a Mockingbird": ("Harper Lee", "Fiction", 4.5),
    "1984": ("George Orwell", "Dystopian", 6.0),
    "The Catcher in the Rye": ("J.D. Salinger", "Fiction", 5.5),
    "Pride and Prejudice": ("Jane Austen", "Romance", 4.0)
}

# List of rentals (each rental is a tuple)
rentals = []

# Set to store unique customers
unique_customers = set()

# Function to display available books
def display_books():
    print("\nAvailable Books:")
    for i, (title, details) in enumerate(books.items(), 1):
        print(f"{i}. {title} by {details[0]} (Genre: {details[1]}, Rental Price: ${details[2]:.2f})")

# Function to rent books
def rent_books():
    customer_name = input("\nEnter your name: ").strip()
    unique_customers.add(customer_name)

    display_books()
    selected_books = input("\nEnter the book numbers you want to rent (comma-separated): ").split(",")

    rental_id = len(rentals) + 1
    rented_books = []
    total_cost = 0

    for book_num in selected_books:
        try:
            book_index = int(book_num.strip()) - 1
            book_title = list(books.keys())[book_index]
            rented_books.append(book_title)
            total_cost += books[book_title][2]
        except (IndexError, ValueError):
            print(f"Invalid book number: {book_num.strip()}")

    if rented_books:
        rentals.append((rental_id, customer_name, rented_books, total_cost))
        print("\nRental Receipt:")
        print(f"Rental ID: {rental_id}")
        print(f"Customer Name: {customer_name}")
        print("Rented Books:")
        for book in rented_books:
            print(f"- {book}")
        print(f"Total Rental Cost: ${total_cost:.2f}")
    else:
        print("No valid books selected for rental.")

# Function to display total revenue
def display_revenue():
    total_revenue = sum(rental[3] for rental in rentals)
    print(f"\nTotal Revenue Generated: ${total_revenue:.2f}")

# Function to display unique customers
def display_unique_customers():
    print("\nUnique Customers:")
    for customer in unique_customers:
        print(f"- {customer}")

# Main menu
def main():
    while True:
        print("\n=== Online Book Rental System ===")
        print("1. Rent Books")
        print("2. Display Total Revenue")
        print("3. Display Unique Customers")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            rent_books()
        elif choice == "2":
            display_revenue()
        elif choice == "3":
            display_unique_customers()
        elif choice == "4":
            print("\nThank you for using the Online Book Rental System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
