# boolean_operations.py
# This program demonstrates the basics of Boolean data types, logical operations, and comparison operators in Python.

# 1. Defining Boolean values
trueValue = True
falseValue = False
print("True value:", trueValue)
print("False value:", falseValue)

# 2. Values considered 'falsy' in Python
falsyValues = [False, 0, 0.0, "", [], {}, None]
print("\nFalsy values in Python:")
for value in falsyValues:
    print(f"{value} is considered:", bool(value))

# 3. Comparison Operators
x = 5
y = 10

print("\nComparison Operators:")
print("x == y:", x == y)            # Compares if x and y are equal
print("x != y:", x != y)            # Compares if x and y are not equal
print("x > y:", x > y)              # Checks if x is greater than y
print("x >= y:", x >= y)            # Checks if x is greater than or equal to y
print("x < y:", x < y)              # Checks if x is less than y
print("x <= y:", x <= y)            # Checks if x is less than or equal to y

# 4. Logical Operators
a = True
b = False

print("\nLogical Operators:")

# AND operator: Both conditions need to be True for the result to be True
print("a and b (True and False):", a and b)  # Expected output: False
# Explanation: Since 'a' is True but 'b' is False, 'a and b' results in False.

# OR operator: At least one condition needs to be True for the result to be True
print("a or b (True or False):", a or b)  # Expected output: True
# Explanation: Since 'a' is True, 'a or b' results in True, even though 'b' is False.

# NOT operator: This inverts the value of a Boolean (True becomes False, and vice versa)
print("not a (not True):", not a)  # Expected output: False
# Explanation: 'not a' inverts the value of 'a', so 'not True' becomes False.

# Additional examples with AND and OR operators
print("a and True (True and True):", a and True)  # Expected output: True
# Explanation: Since both conditions are True, 'a and True' results in True.

print("b or False (False or False):", b or False)  # Expected output: False
# Explanation: Since both conditions are False, 'b or False' results in False.
