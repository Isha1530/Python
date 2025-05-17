# geometry.py

import math

def calculate_area(shape, *dimensions):
    """Calculate area of circle, rectangle, or triangle."""
    if shape == 'circle' and len(dimensions) == 1:
        return math.pi * dimensions[0] ** 2
    elif shape == 'rectangle' and len(dimensions) == 2:
        return dimensions[0] * dimensions[1]
    elif shape == 'triangle' and len(dimensions) == 2:
        return 0.5 * dimensions[0] * dimensions[1]
    else:
        return "Invalid shape or parameters"

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
