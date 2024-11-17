# dictionary_exercise_4.py

# This program asks the user for their name, age, address, and phone number and stores the information in a dictionary.
# Then, it displays a message: <name> is <age> years old, lives at <address>, and their phone number is <phone number>.

def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")

    userInfo = {
        "name": name,
        "age": age,
        "address": address,
        "phone": phone
    }

    print(f"{userInfo['name']} is {userInfo['age']} years old, lives at {userInfo['address']}, and their phone number is {userInfo['phone']}.")

# Run the program
main()
