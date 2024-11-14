# basic_operations.py
# This program demonstrates basic arithmetics operations and unary operators in Python

# Sample numbers
number1 = 10
number2 = 3

# 1. Basic Arithmetic Operations
addition = number1 + number2
substraction = number1 - number2
multiplication = number1 * number2 
division = number1 / number2            # Regular division
intDivision = number1 // number2        # Integer (floor) division
modulus = number1 % number2
exponentiation = number1 ** number2     # We can also use the function pow() to do this operation
exponentiationPow = pow(number1, number2)

# Printing the results 
print("Basic Arithmetic Operations: ") 
print(f"Addition ({number1} + {number2})", addition)
print(f"Substraction ({number1} - {number2})", substraction)
print(f"Multiplication ({number1} * {number2})", multiplication)
print(f"Division ({number1} / {number2})", division)
print(f"Interger division ({number1} // {number2})", intDivision)
print(f"Modulus ({number1} % {number2})", modulus)
print(f"Exponentiation ({number1} ** {number2})", exponentiation)
print(f"Exponentiation with function pow() (pow({number1},  {number2}))", exponentiationPow)

# 2. Unary Operators
positiveUnary = +number1
negativeUnary = -number1

# Print the results of unary operations
print("\nUnary Operators:")
print(f"Positive Unary (+{number1}):", positiveUnary)
print(f"Negative Unary (-{number1}):", negativeUnary)
