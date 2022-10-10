# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number
number = int(input("Enter a number or type 0 to stop: "))

# terminates excection 
while number != 0:
    # check if number is odd
    if number % 2 == 1:
        # increase the odd number counter
        odd_numbers += 1
    else:
        # increase the even number counter
        even_numbers += 1
    # Read the next number 
    number = int(input("Enter a number or type 0 to stop: "))

# print results
print("Odd number count:", odd_numbers)
print("Even number count:", even_numbers)