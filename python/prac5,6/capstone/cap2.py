import itertools

# Menu stored as a dictionary (item_name: (price, category))
menu = {
    "Burger": (5.99, "Fast Food"),
    "Pizza": (8.99, "Fast Food"),
    "Pasta": (7.49, "Italian"),
    "Salad": (4.99, "Healthy"),
    "Soda": (1.99, "Beverage"),
}

# List of orders stored as tuples (Order ID, Customer Name, Item List, Total Bill)
orders = []

# Set of unique customer names
customers = set()

# Order ID generator
generate_order_id = itertools.count(1)

def display_menu():
    print("\nMenu:")
    for item, (price, category) in menu.items():
        print(f"{item}: ${price:.2f} ({category})")

def place_order():
    customer_name = input("Enter your name: ")
    customers.add(customer_name)
    
    item_list = []
    total_bill = 0
    
    while True:
        display_menu()
        item = input("Enter item name to order (or type 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        if item in menu:
            item_list.append(item)
            total_bill += menu[item][0]
        else:
            print("Item not found. Please select from the menu.")
    
    if item_list:
        order_id = next(generate_order_id)
        orders.append((order_id, customer_name, item_list, total_bill))
        print(f"\nOrder placed successfully! Order ID: {order_id}, Total Bill: ${total_bill:.2f}")
    else:
        print("No items selected. Order cancelled.")

def display_revenue():
    total_revenue = sum(order[3] for order in orders)
    print(f"\nTotal Revenue: ${total_revenue:.2f}")

def display_unique_customers():
    print("\nUnique Customers:")
    for customer in customers:
        print(customer)

# Main program loop
while True:
    print("\n1. Place an Order")
    print("2. Display Total Revenue")
    print("3. Display Unique Customers")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        place_order()
    elif choice == '2':
        display_revenue()
    elif choice == '3':
        display_unique_customers()
    elif choice == '4':
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")