# read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = number1 # assume that number 1 is the largest nunber

# check and update for number 2
if number2 > number1:
    largest_number = number2

# check and update for number 3
if number3 > number2:
    largest_number = number3

print("The largest nunmber is:", largest_number)