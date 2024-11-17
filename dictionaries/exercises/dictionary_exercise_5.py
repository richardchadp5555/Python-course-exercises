# dictionary_exercise_5.py
# We are asked to perform an analysis of daily and monthly sales for a store. 
# To do this, we will use a dictionary containing the sales of each product for each day of the month.
# Our analysis should include the total monthly sales of each product, the best-selling and least-selling product each month,
# the daily sales of the best-selling product, and the day with the highest sales for each product.
# Suppose we have the sales of four products. In this dictionary, the main keys are the products, 
# and each product key has a nested dictionary where the keys are the days and the values are the units sold.

# Menu
def showMenu():
    print("SALES ANALYSIS")
    print("**********************************************************************************")
    print("1) Calculate the total units sold in the month for each product")
    print("2) Identify the best-selling and least-selling product of the month")
    print("3) Show the daily sales of the best-selling product")
    print("4) Find the day with the highest sales for each product")
    print("5) Exit")

# Method to calculate the total units sold in the month for a product
def calculateSales(product, sales):
    totalSales = 0

    for i in range(30):
        totalSales += sales[product][str(i + 1)]
    return totalSales

# Method to get the total units sold in the month for each product, returns a dictionary with the total sales of each product
def totalSales(sales):
    monthlySales = {}

    for product in sales.keys():
        monthlySales[product] = calculateSales(product, sales)
    return monthlySales

# Method to determine the best-selling and least-selling product of the month
def getExtremesSales(monthlySales):
    highestSales = 0
    bestSellingProduct = ""

    # Determine the best-selling product
    for product, total in monthlySales.items():
        if total > highestSales:
            bestSellingProduct = product
            highestSales = total
    
    # Determine the least-selling product
    lowestSales = highestSales  # Initialize with the highest value
    leastSellingProduct = ""

    for product, total in monthlySales.items():
        if total < lowestSales:
            leastSellingProduct = product
            lowestSales = total

    return (bestSellingProduct, highestSales), (leastSellingProduct, lowestSales)

# Method to determine the day with the highest sales of a product
def dayWithHighestSales(product, sales):
    highestSalesDay = 1
    highestSalesAmount = 0

    for day, units in sales[product].items():
        if units > highestSalesAmount:
            highestSalesDay = day
            highestSalesAmount = units
    
    return highestSalesDay, highestSalesAmount

# Main
def main():
    keepRunning = True  # Control variable for the loop

    # Dictionary of sales for four products, each day of the month (30 days)
    sales = {
        "laptop": {
            "1": 5, "2": 7, "3": 10, "4": 8, "5": 12,
            "6": 9, "7": 11, "8": 4, "9": 6, "10": 10,
            "11": 8, "12": 13, "13": 7, "14": 15, "15": 6,
            "16": 9, "17": 12, "18": 10, "19": 8, "20": 7,
            "21": 11, "22": 5, "23": 14, "24": 9, "25": 10,
            "26": 12, "27": 8, "28": 13, "29": 7, "30": 6
        },
        "keyboard": {
            "1": 10, "2": 8, "3": 9, "4": 12, "5": 7,
            "6": 10, "7": 6, "8": 8, "9": 11, "10": 9,
            "11": 13, "12": 14, "13": 12, "14": 8, "15": 7,
            "16": 6, "17": 10, "18": 7, "19": 9, "20": 12,
            "21": 14, "22": 13, "23": 6, "24": 8, "25": 7,
            "26": 9, "27": 10, "28": 11, "29": 6, "30": 8
        },
        "mouse": {
            "1": 15, "2": 18, "3": 20, "4": 12, "5": 14,
            "6": 17, "7": 19, "8": 13, "9": 16, "10": 15,
            "11": 18, "12": 14, "13": 17, "14": 20, "15": 19,
            "16": 15, "17": 16, "18": 14, "19": 13, "20": 17,
            "21": 20, "22": 18, "23": 19, "24": 16, "25": 15,
            "26": 18, "27": 20, "28": 17, "29": 14, "30": 19
        },
        "mousePad": {
            "1": 8, "2": 7, "3": 6, "4": 10, "5": 9,
            "6": 8, "7": 7, "8": 6, "9": 5, "10": 9,
            "11": 8, "12": 7, "13": 10, "14": 6, "15": 9,
            "16": 8, "17": 7, "18": 6, "19": 10, "20": 8,
            "21": 7, "22": 9, "23": 6, "24": 10, "25": 8,
            "26": 9, "27": 7, "28": 6, "29": 8, "30": 10
        }
    }

    # Pre-calculations
    monthlySales = totalSales(sales)
    (bestSellingProduct, highestSales), (leastSellingProduct, lowestSales) = getExtremesSales(monthlySales)

    while keepRunning:
        showMenu()
        menuOption = input("Enter an option (1 - 5): ")
        print("\n")

        match menuOption:
            case "1":
                for product, total in monthlySales.items():
                    print(f"{product}: {total} units\n")
            case "2":
                print(f"The best-selling product of the month is {bestSellingProduct} with {highestSales} units.")
                print(f"The least-selling product of the month is {leastSellingProduct} with {lowestSales} units.\n")
            case "3":
                print(f"The best-selling product this month is {bestSellingProduct}, and its daily sales are:\n")
                for day, salesAmount in sales[bestSellingProduct].items():
                    print(f"Day {day}: {salesAmount} units\n")
            case "4":
                for product in sales.keys():
                    day, amount = dayWithHighestSales(product, sales)
                    print(f"The highest sale for {product} occurred on day {day} with {amount} units sold.\n")
            case "5":
                print("Exiting...")
                keepRunning = False
            case _:
                print("Invalid option. Please try again.\n")

# Run the program
main()
