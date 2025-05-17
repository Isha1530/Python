class CustomError(Exception):
    """Custom exception for specific scenarios"""
    pass

def check_value(value):
    if value < 0:
        raise CustomError("Negative value is not allowed!")

def custom_exception_handling():
    try:
        num = int(input("Enter a number: "))
        check_value(num)
        print("Valid input:", num)
    except CustomError as e:
        print("Custom Exception:", e)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def index_error_handling():
    my_list = [10, 20, 30, 40, 50]
    while True:
        try:
            index = int(input(f"Enter an index (0 to {len(my_list)-1}): "))
            print("Element at index", index, "is", my_list[index])
            break
        except IndexError:
            print("Error: Index out of range! Please enter a valid index.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

def value_error_handling():
    while True:
        try:
            user_input = input("Enter a number: ")
            number = int(user_input)
            print("Valid number entered:", number)
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    print("\n--- Custom Exception Handling ---")
    custom_exception_handling()
    
    print("\n--- Index Error Handling ---")
    index_error_handling()
    
    print("\n--- Value Error Handling ---")
    value_error_handling()
