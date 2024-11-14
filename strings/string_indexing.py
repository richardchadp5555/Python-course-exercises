# string_indexing.py
# This program demonstrates string indexing and slicing in Python

# Sample text
sampleText = "Hello Python!"

# Access individual characters
print('First character: ', sampleText[0])
print("Fifth character: ", sampleText[4])
print("Last character: ", sampleText[-1])

# String slicing 
print("First 5 characters: ", sampleText[:5])
print("Character from index 7 to 12: ", sampleText[7:12])
print("Last 3 characters: ", sampleText[-3:])

# Slicing with step
print("Every second character>", sampleText[::2])
print("Characters from index 7 to 12, every second character: ", sampleText[7:12:2])

# Reversing the string
print("Reversed string: ", sampleText[::-1])

# Combining slices: taking first 5 and last 3 characters
combinedSlices = sampleText[:5] + sampleText[-3:]
print("Combined slices (first 5 + last 3 characters): ", combinedSlices)