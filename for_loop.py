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
for i in range(10):
    print("The value of i is currently", i)
    time.sleep(0.3)

time.sleep(0.5)
print("Done!")

# range function may be equiped with two arguments not just one
for i in range(2, 8): # start with two, end in 7
    print("The value of i is currently", i)