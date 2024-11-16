# phone_directory.py
# This program uses a dictionary to create a phone directory. The dictionary consists of name-phone pairs.

import re  # Module for regular expressions

# Method to display the menu
def showMenu():
    print("\nPHONE DIRECTORY")
    print("**************************************************************")
    print("a) List all contacts in default order")
    print("b) List all contacts in alphabetical order")
    print("c) Add a new contact")
    print("d) Update a contact's phone number")
    print("e) Search for a contact's phone number")
    print("f) Delete a contact")
    print("g) Clear the phone directory")
    print("h) Exit\n")

# Method to validate phone numbers
def isPhoneValid(phone):
    pattern = r"^\d{9}$"
    return bool(re.fullmatch(pattern, phone))

# Method to update a contact's phone number
def updatePhoneNumber(name, phoneDirectory):
    while True:
        newPhone = input("Enter the new phone number: ").strip()
        if isPhoneValid(newPhone):
            phoneDirectory[name] = newPhone
            print(f"{name.capitalize()}'s phone number has been successfully updated.\n")
            break
        else:
            print("Invalid phone number. It must be a 9-digit number.\n")

# Method to add a new contact
def addContact(name, phoneDirectory):
    if name in phoneDirectory:
        print(f"A contact named '{name.capitalize()}' already exists.")
        updatePhone = input("Do you want to update their phone number? (yes / no): ").strip().lower()
        if updatePhone == "yes":
            updatePhoneNumber(name, phoneDirectory)
    else:
        phone = input("Enter the phone number: ").strip()
        if isPhoneValid(phone):
            phoneDirectory[name] = phone
            print(f"Contact {name.capitalize()} has been successfully added.\n")
        else:
            print("Invalid phone number. It must be a 9-digit number.\n")

# Main function
def main():
    # Preloaded phone directory
    phoneDirectory = {
        "john": "123456789",
        "mary": "987654321",
        "peter": "456789123",
        "anna": "789123456",
        "charles": "321654987"
    }

    # Variable to manage the loop
    keepRunning = True

    # Main loop
    while keepRunning:
        showMenu()
        menuOption = input("Choose an option (a - h): ").strip().lower()

        match menuOption:
            case "a":  # List all contacts in default order
                print("\nContact list:")
                for name, phone in phoneDirectory.items():
                    print(f"{name.capitalize()} - {phone}")
                print()
            case "b":  # List all contacts in alphabetical order
                print("\nContact list (alphabetical order):")
                for name, phone in sorted(phoneDirectory.items()):
                    print(f"{name.capitalize()} - {phone}")
                print()
            case "c":  # Add a new contact
                name = input("Enter the name of the new contact: ").strip().lower()
                addContact(name, phoneDirectory)
            case "d":  # Update a contact's phone number
                name = input("Enter the name of the contact: ").strip().lower()
                if name not in phoneDirectory:
                    response = input("This contact is not in the system. Do you want to add them? (yes / no): ").strip().lower()
                    if response == "yes":
                        addContact(name, phoneDirectory)
                else:
                    updatePhoneNumber(name, phoneDirectory)
            case "e":  # Search for a contact's phone number
                name = input("Enter the name of the contact whose phone number you want to find: ").strip().lower()
                if name in phoneDirectory:
                    print(f"\n{name.capitalize()}'s phone number is {phoneDirectory[name]}\n")
                else:
                    print("\nThis contact is not in the system.\n")
            case "f":  # Delete a contact
                name = input("Enter the name of the contact you want to delete: ").strip().lower()
                if name in phoneDirectory:
                    del phoneDirectory[name]
                    print(f"\nContact {name.capitalize()} has been deleted.\n")
                else:
                    print("\nThis contact is not in the system.\n")
            case "g":  # Clear the phone directory
                confirmation = input("Are you sure you want to clear the phone directory? (yes / no): ").strip().lower()
                if confirmation == "yes":
                    phoneDirectory.clear()
                    print("\nThe phone directory has been cleared.\n")
            case "h":  # Exit
                print("\nExiting...\n")
                keepRunning = False
            case _:
                print("\nInvalid option.\n")

# Run the program
main()
