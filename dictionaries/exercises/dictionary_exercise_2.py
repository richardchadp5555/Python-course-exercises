# dictionary_exercise_2.py

# In this program, we declare a dictionary for the prices of different fruits. 
# The program will ask for the name of the fruit and the quantity sold, and it will display the final price of the fruit based on the data stored in the dictionary.
# If the fruit doesn't exist, it will display an error message.
# After each query, the program will ask if the user wants to perform another query.

# The key will be the name of the fruit, and the value will be its price.

fruitPrices = {"apple": 2, "orange": 1.5, "banana": 4, "pineapple": 3}
keepSelling = True

while keepSelling:
    fruit = input("Enter the fruit you sold: ").lower()
    if fruit not in fruitPrices:
        print("This fruit does not exist in the system.")
    else:
        try:
            quantity = int(input(f"Enter the quantity of {fruit} you sold: "))
            totalPrice = quantity * fruitPrices[fruit]
            print(f"The total price for {quantity} {fruit}(s) is: ", str(totalPrice))
        except ValueError:
            print("Please enter a valid number.")

    # Ask the user if they want to continue with the program
    option = input("Do you want to sell another fruit? (yes / no): ").strip().lower()
    while option != "yes" and option != "no":
        option = input("Do you want to sell another fruit? (yes / no): ").strip().lower()
    if option == "no":
        keepSelling = False
