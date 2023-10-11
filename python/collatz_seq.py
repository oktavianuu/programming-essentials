c0 = int(input("Enter a natural number: "))

steps = 0 # steps counter

#while loops to perform collatz seq
while c0 != 0:
    # print the current value of c0
    print(c0)

    # check if c0 is even
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1

    # increment the step counter
    steps += 1

print(c0)
print("steps:", steps)
