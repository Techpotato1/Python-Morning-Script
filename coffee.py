#Coffee shop program

menu = "Coffee, Latte, Tea, and Water"
price = 5

print("Hello, Welcome to my coffee shop!")

name = input("What is your name? \n")

print("Welcome to my coffee shop, " + name + "!")
print("We currently serve: " + menu + ".")

itemordered = input("What would you like to order? \n")
if itemordered == "Latte":
    price = 7
elif itemordered == "Tea":
    price = 4
elif itemordered == "Water":
    price = 2   
elif itemordered == "Coffee":
    price = 5
else:
    print("Sorry, we don't serve that here.")
    exit()

numordered = input("How many " + itemordered + "s would you like? \n")
total = price * int(numordered)

print("Ok, " + name + ", your " + itemordered + " will be right up!")

if total >= 50:
    print("That's a lot of " + itemordered + "s, " + name + "!")
    print("For being such a generous customer, we'll give you a 20% discount!")
    print("Your total is: $" + str(total * 0.8) + "!")
else:
    print("Your total is: $" + str(total) + "!")
