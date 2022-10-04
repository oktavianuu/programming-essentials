# The program reads a float value, puts it into a variable named x, and prints the value of a variable named y. Your task is to complete the code in order to 
# evaluate the following expression: 3X^3 - 2X^2 + 3X - 1

# input             # output
# X = 0             # y = -1.0
# X = 1             # y = 3.0

x = float(input("enter any number:"))
y = (3 * x ** 2) - (2 * x ** 2) + (3 * x) -1

print("y =", y)