counter = int(input("Enter your favorite number: "))

while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)