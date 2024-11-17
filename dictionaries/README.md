# Dictionaries in Python

This folder provides an in-depth look at dictionaries in Python, a versatile data structure used to store key-value pairs. Below, you’ll find explanations of core dictionary concepts, operations, and example code snippets.

## Exercises
The **exercises** subdirectory contains several practical tasks to deepen your understanding of Python dictionaries:

- **Exercise 1**: Count character occurrences in a string.
  - Reads a string input from the user and creates a dictionary that counts the occurrences of each character in the string.
  - **Objective**: Practice creating and manipulating dictionaries, as well as iterating through their keys and values.

- **Exercise 2**: Manage a fruit inventory and calculate prices.
  - Asks the user for a fruit name and quantity sold.
  - Calculates the total price based on the stored prices in the dictionary.
  - Includes error handling for invalid fruit names and non-numeric inputs.
  - Allows the user to make multiple queries.
  - **Objective**: Learn to validate user input and calculate values using dictionaries.

- **Exercise 3**: Build an interactive phone directory.
  - Implements a phone directory with features like adding, updating, searching, and deleting contacts.
  - Displays the phone directory in default and alphabetical orders.
  - Validates phone numbers (must be 9 digits).
  - Includes an interactive menu for seamless navigation.
  - **Objective**: Work with dictionary operations and build an interactive application.

- **Exercise 4**: Store and display user information.
  - Asks the user for their name, age, address, and phone number, then stores this data in a dictionary.
  - Displays the following message:
    ```
    <name> is <age> years old, lives at <address>, and their phone number is <phone number>.
    ```
  - **Objective**: Practice basic input/output operations and storing user data in a dictionary.

- **Exercise 5**: Analyze daily and monthly sales of a store.
  - Analyzes sales data stored in a nested dictionary for four products over 30 days.
  - Features include:
    - Calculating total units sold for each product.
    - Identifying the best-selling and least-selling product of the month.
    - Displaying daily sales of the best-selling product.
    - Finding the day with the highest sales for each product.
  - **Objective**: Explore advanced use cases with nested dictionaries and perform calculations based on stored data.

For more details about the exercises, check the `exercises/README.md`.

## What is a Dictionary?

A **dictionary** in Python is a mutable data structure that stores data in **key-value pairs**. Dictionaries are highly efficient for lookups, adding, and deleting items by their keys.

- **Keys**: Must be immutable (strings, numbers, or tuples).
- **Values**: Can be any data type and may include other dictionaries.
- **Ordering**: Dictionaries are ordered (preserve insertion order) starting from Python 3.7.

```python
# Creating a dictionary to store fruit prices
fruit_prices = {
    "Apple": 1.50,
    "Banana": 0.75,
    "Cherry": 2.00
}
print(fruit_prices)
```

## Creating a dictionary
Dictionaries can be created using curly braces {} with coma-separated key-value pairs, or with the dict() function
**Syntax:**
dictionary_name = {
    key1: value1,
    key2: value2,
    ...
}

For example:
```python
# Using curly braces
sample_dict = {
    "name": "Alice",
    "age": 25
}

# Using dict() constructor
another_dict = dict(name="Bob", age=30)

```

## Accesing Dictionary Values
Dictionary Values can be accessed by referencing their keys. If the key does not exists, a **KeyError** will be raised. To avoid this, use the get() method, wich allows setting a **default return value**

```python
# Accessing using square brackets
print(sample_dict["name"])  # Outputs: Alice

# Using get() to avoid KeyError
print(sample_dict.get("address", "Not Found"))  # Outputs: Not Found

```


## Adding or Modifying Elements
To add a new key-value or modify an exixting key, use square brackets with the key and asing a value.
### Example:

```python
sample_dict["address"] = "123 Maple St"  # Adds a new key-value pair
sample_dict["age"] = 26  # Modifies the existing "age" key
print(sample_dict)

```
## Checking for Key Existence
To check if a key exists **in** a dictionary, use the in keyword.
```python
if "name" in sample_dict:
    print("Name exists in the dictionary.")

```

## Removing elements
Dictionaries support several methods for removing elements:
- **del:** Removes an item by key
- **pop():** Removes an item by key and return its value
- **popitem():** Removes and return the last inserted key-value pair.
- **clear():** Removes all items from the dictionary.

```python
# Using del
del sample_dict["age"]

# Using pop()
removed_value = sample_dict.pop("address", "Not Found")
print("Removed address:", removed_value)

# Using popitem()
last_item = sample_dict.popitem()
print("Last item removed:", last_item)

# Using clear()
sample_dict.clear()
print("Dictionary after clearing:", sample_dict)

```
## Dictionary Methods and Functions

Here are some useful dictionary methods and functions:

| Method                  | Description                                                      |
|-------------------------|------------------------------------------------------------------|
| `dict.get(key, default)`| Returns the value for a key if it exists, else returns `default`.|
| `dict.keys()`           | Returns a view object with all dictionary keys.                 |
| `dict.values()`         | Returns a view object with all dictionary values.               |
| `dict.items()`          | Returns a view object with all dictionary key-value pairs as tuples. |
| `dict.update(other_dict)` | Updates the dictionary with key-value pairs from `other_dict`. |
