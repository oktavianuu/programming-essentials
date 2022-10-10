from itertools import count
import time
counter = int(input("Enter your favorite number: "))

while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
    time.sleep(0.5)
print("Outside the loop.", counter)

# compact version
print("compact version of the previous code.")
counter = int(input("Enter your favorite number: "))

while counter:
    print("Inside the loop.", counter)
    counter -= 1
    time.sleep(0.5)
print("Outside the loop.", counter)
print("Thanks buddy!")