# Variables in Python

This document covers the concept of variables in Python, including how they are created, updated, and assigned new values. Understanding variables is fundamental to Python programming, as they store the data that is manipulated within a program.

## What is a Variable?

A variable in Python is an identifier that references a value. Unlike some other languages, Python does not require you to declare a variable before using it, nor do you need to specify its type. A variable's type is determined by the value it currently holds.

- **Dynamic Typing**: Python is dynamically typed, meaning a variable’s type can change as the program runs.
- **Automatic Memory Management**: Variables in Python are managed by Python’s built-in garbage collector, which automatically allocates and frees memory.

## Deleting variables
- **Variables can be deleted using the del keyword**. After deleting a variable, trying to access it will result in a NameError.

## Variable Assignment
- **Basic Assignment**. You can assign a value to a variable simply by using the = operator. This operator assigns the value on the right to the variable on the left.
- **Multiple Assignment**. Python allows you to assign values to multiple variables in a single line. For example: x, y, z = 5, 10, 15
- **Swapping Variables**. Swapping the values of variables in Python can be done easily without using a temporary variable. For example: x, y = y, x

## Best Practices for Variables
- **Use meaningful names:** Choose variable names that clearly describe the data they hold.
- **Follow naming conventions:** In Python, it’s common to use snake_case for variable names or capitalize each word after the first (e.g., variableName).
- **Avoid using reserved keywords:** Python has reserved words like class, for, and if. Avoid using these as variable names.
- **Keep scope in mind:**  Avoid defining variables in a broader scope than necessary.