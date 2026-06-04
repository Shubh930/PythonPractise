# Restaurant Menu Program

menu = {
    "Pizza": 299,
    "Burger": 89,
    "Sandwich": 79,
    "Dosa": 129,
    "Butterchicken": 259,
    "Pasta": 99,
    "Cold Drink": 50,
    "Coffee": 40,
    "Tea": 25
}

total_bill = 0

# Print Menu
print("------- MENU -------")

for dish, price in menu.items():
    print(dish, ":", "Rs", price)

# Take Orders
while True:

    choice = input("\nEnter your dish name to order: ").title()

   
    if choice in menu:

        total_bill = total_bill + menu[choice]

        print(choice, "added to your bill.")
        # print(f"{choice} added to your bill.")
        
    else:
        print("Dish is not available!")
        print("Please choose a valid dish from the menu.")

    # Ask for more orders
    more = input("Do you want to order more? (yes/no): ").lower()

    # Stop loop if user says no
    if more == "no":
        break

# Final Bill
print("\n------ FINAL BILL ------")
print("Total Amount = Rs", total_bill)
print("Thank you for visiting!")
