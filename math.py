
numentered = input("Addition or Subtraction? \n")
if numentered == "Addition" or numentered == "addition" or numentered == "Add" or numentered == "add":
    firstnum = input("What is the first number? \n")
    secondnum = input("What is the second number? \n")
    print("The sum of " + firstnum + " and " + secondnum + " is " + str(int(firstnum) + int(secondnum)) + ".")
elif numentered == "Subtraction" or numentered == "subtraction" or numentered == "Sub" or numentered == "sub":
    firstnum = input("What is the first number? \n")
    secondnum = input("What is the second number? \n")
    print("The difference of " + firstnum + " and " + secondnum + " is " + str(int(firstnum) - int(secondnum)) + ".")
