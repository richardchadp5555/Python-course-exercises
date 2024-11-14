# type_conversions.py
# This program demonstrates type conversions and casting in Python.

# 1. Converting a Float to an Integer
# When converting from float to integer, note that Python truncates (cuts off) the decimal portion.
floatValue = 7.9
intFromFloatValue = int(floatValue)
print("Original float:", floatValue)
print("Converted to integer:", intFromFloatValue)

# 2. Parsing an Integer from a String
# When parsing a number from a string, ensure the string contains only numeric characters.
stringNumber = "123"
intFromString = int(stringNumber)
print("\nOriginal string:", stringNumber)
print("Parsed integer from string:", intFromString)

# Handling invalid conversions with a try-except block
invalidString = "abc123"
try:
    invalidString = int(invalidString)
except ValueError:
    print("\nCannot convert 'abc123' to an integer. Non-numeric characters are present.")

# 3. Converting an Integer to a String
# This is useful for concatenating numbers with other strings.
intergerValue = 456
strinFromInt = str(intergerValue)
print("\nOriginal integer:", intergerValue)
print("Converted to string:", strinFromInt)
print("Concatenated with text:", "Number is " + strinFromInt)

# 4. Converting between String, Integer, and Float
# Demonstrates going from string to float, then float to integer.
stringFloat = "45.67"
floatFromString = float(stringFloat)
intFromFloatString = int(floatFromString)
print("\nOriginal string:", stringFloat)
print("Converted to float:", floatFromString)
print("Converted to integer (from float):", intFromFloatString)

# 5. Converting Boolean to Integer and String
# Booleans are often used in conversions, where True is 1 and False is 0.
booleanValue = True
intFromBoolean = int(booleanValue)
stringFromBoolean = str(booleanValue)
print("\nBoolean value:", booleanValue)
print("Converted to integer:", intFromBoolean)
print("Converted to string:", stringFromBoolean)

