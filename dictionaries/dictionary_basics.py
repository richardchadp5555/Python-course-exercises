# dictionary_basics.py
# This program demonstrates the basics of Python dictionaries, including creation, modification, and common operations.

# 1. What is a Dictionary?
# A dictionary is a mutable, hash table-based data structure in Python that stores key-value pairs.
# The key must be an immutable type (e.g., string, number, or tuple), while the value can be any data type.

# Example: Creating an empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# Example: Creating a dictionary with fruit prices
prices = {
    "Pear": 1.60,
    "Plum": 1.24,
    "Apple": 1.75
}
print("Fruit prices dictionary:", prices)

# Alternative way to create a dictionary using dict()
prices_alt = dict(Pear=1.60, Plum=1.24, Apple=1.75)
print("Fruit prices dictionary (using dict()):", prices_alt)

# 2. Adding or Modifying Elements
# You can add a new element or update an existing one by using the key in square brackets.
prices["Watermelon"] = 0.99  # Adds a new item
prices["Pear"] = 1.80        # Updates the price of "Pear"
print("Updated prices dictionary:", prices)

# 3. Checking if a Key Exists
# Use the "in" keyword to check if a key exists in a dictionary.
if "Pear" in prices:
    print("Pear is in the dictionary.")

# 4. Accessing Values
# Use square brackets to access a value. An error is raised if the key does not exist.
p_watermelon = prices["Watermelon"]
print("Price of Watermelon:", p_watermelon)

# Using get() to access values safely (avoiding errors)
p_melon = prices.get("Melon", -1)  # Returns -1 if "Melon" is not in the dictionary
print("Price of Melon (default if not found):", p_melon)

# 5. Removing Elements
# Use the "del" keyword to remove an element by its key.
del prices["Watermelon"]
print("Prices dictionary after removing Watermelon:", prices)

# Using pop() to remove an item and return its value
p_pear = prices.pop("Pear")
print("Removed Pear with pop():", p_pear)
print("Prices dictionary after popping Pear:", prices)

# Using pop() with a default value to avoid errors
p_melon = prices.pop("Melon", -1)
print("Tried to pop Melon (returns default if not found):", p_melon)

# 6. Clearing the Dictionary
# Clears all items in the dictionary
prices.clear()
print("Prices dictionary after clearing:", prices)

# 7. Dictionary Length
# Get the number of items in a dictionary using len()
print("Length of empty prices dictionary:", len(prices))

# 8. Dictionary Keys, Values, and Items
# Access the keys, values, or key-value pairs (items) of a dictionary.
# Let's reinitialize the dictionary for demonstration
prices = {
    "Pear": 1.60,
    "Plum": 1.24,
    "Apple": 1.75
}
print("\nDictionary keys:", list(prices.keys()))
print("Dictionary values:", list(prices.values()))
print("Dictionary items:", list(prices.items()))

# Iterating over dictionary keys
print("\nIterating over dictionary keys:")
for key in prices.keys():
    print(key)

# Iterating over dictionary values
print("\nIterating over dictionary values:")
for value in prices.values():
    print(value)

# Iterating over dictionary items (key-value pairs)
print("\nIterating over dictionary items:")
for key, value in prices.items():
    print(f"{key}: {value}")
