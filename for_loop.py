import time
#i = 0 
#while i < 100:
#    i += 1
#    time.sleep(0.01)
#    print(i)
#print("Yeayy!")

# more compact using for loop
#for i in range(101):
#    print(i)
#    time.sleep(0.009)

# for is designed to do more complicated tasks – it can "browse" large collections of data item by item. 
print("range with one argument.")
for i in range(10):
    print("The value of i is currently", i)
# range function may be equiped with two arguments not just one
print("range with two arguments.")
for i in range(2, 8): # start with two, end in 75
    print("The value of i is currently", i)

# range with three arguments
print("range with three arguments.")
for i in range(2, 8, 3): # the third arguments indicates the step
    print("The value of i is currently", i)

print("write some of the first powers of two.")
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2
    