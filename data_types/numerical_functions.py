# numerical_functions.py
# This program demonstrates various built-in numerical functions in Python

import math

# Absolute value
negativeNumber = -10
print("Absolute value:", abs(negativeNumber))

# Rounding
floatNumber = 3.14159
print("Rounded to 2 decimal places: ", round(floatNumber, 2))

# Power calculation
base = 2
exponent = 3
print("Power with pow()", pow(base, exponent))
print("Power with ** operator: ", base ** exponent)

# Minimum and Maximum
numbers = [3, 1, 7, 4, 5]
print("Minimum value: ", min(numbers))
print("Maximum value: ", max(numbers))

# Square Root
number = 16
print(f"Square root of {number}: ", math.sqrt(number))

# Floor and Ceiling
floatValue = 5.7
print("Floor: ", math.floor(floatValue))
print("Ceiling: ", math.ceil(floatValue))