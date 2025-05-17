# mymodule.py

def arithmetic_operations(a, b, operation):
    """Perform basic arithmetic operations."""
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

def is_even_or_odd(num):
    """Check if a number is even or odd."""
    return "Even" if num % 2 == 0 else "Odd"
