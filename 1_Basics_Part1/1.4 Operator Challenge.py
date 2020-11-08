##Estimated time
##10-15 minutes
##
##Level of difficulty
##Easy
##
##Objectives
##becoming familiar with the concept of numbers, operators and arithmetic operations in Python;
##performing basic calculations.
##Scenario
##Take a look at the code below: it reads a float value, puts it into a variable named x, and prints the value of a variable named y. Your task is to complete the code in order to evaluate the following expression:
##
##
##We expect the result to be assigned to y.
##
##Remember that classical algebraic notation likes to omit the multiplication operator – you need to use it explicitly.
##
##Keep your code clean and readable – surround operators with spaces.
##
##Test your code using the data we've provided – don't be discouraged by any initial failures. Be persistent and inquisitive. Good luck!
##
##Example input
##0
##
##Example output
##y = -1.0
##
##Example input
##1
##
##Example output
##y = 3.0
##
##Example input
##-1
##
##Example output
##y = -9.0



x = float(input("Enter value for x: "))

y = 3*x**3 - 2*x**2 + 3*x - 1

print("y =",y)
