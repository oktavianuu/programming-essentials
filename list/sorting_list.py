# We solve this issue in the following way: we introduce another variable; its task is to observe if any swap has been done during 
# the pass or not; if there is no swap, then the list is already sorted, and nothing more has to be done. We create a variable 
# named swapped, and we assign a value of False to it, to indicate that there are no swaps. Otherwise, it will be assigned True.
my_list = [8, 10, 6, 2, 4] # list to be sorted
print(my_list)

# for i in range(len(my_list) - 1): # we need (5-1) comparison
#    if my_list[i] > my_list[i + 1]: # compare adjacent
#        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] # if we end up here, we have to swap the elements
#
# print(my_list)

swapped = True
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("The list before")
print(my_list)