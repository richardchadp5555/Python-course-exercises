# dictionary_exercise_1.py
# Write a program that reads a string and returns a dictionary with the number of occurrences of each character in the string.

# Initialize an empty dictionary
characterCount = {}

# Ask for the string
inputString = input("Enter a text string: ")
for character in inputString:
    if character in characterCount:
        characterCount[character] += 1  # If it's in the dictionary, increment the count by 1
    else:
        characterCount[character] = 1  # If it's not in the dictionary, add it and set the count to 1

# Display the result
for key, value in characterCount.items():
    print(key, " - ", value)
