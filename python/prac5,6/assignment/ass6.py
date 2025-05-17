# main.py

import my_module6
import geometry6
import datetime

# Using mymodule functions
print("Arithmetic Operations:")
print("Addition (5 + 3):", my_module6.arithmetic_operations(5, 3, 'add'))
print("Multiplication (4 * 2):", my_module6.arithmetic_operations(4, 2, 'multiply'))
print("Check Even/Odd (7):", my_module6.is_even_or_odd(7))

# Using geometry module
print("\nArea Calculations:")
print("Circle with radius 3:", geometry6.calculate_area('circle', 3))
print("Rectangle with length 4 and width 5:", geometry6.calculate_area('rectangle', 4, 5))
print("Triangle with base 6 and height 7:", geometry6.calculate_area('triangle', 6, 7))

print("\nPrime Number Check:")
print("Is 11 prime?", geometry6.is_prime(11))
print("Is 12 prime?", geometry6.is_prime(12))

# Using datetime module
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("\nCurrent Date and Time:", formatted_time)
