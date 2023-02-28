my_list = [8, 10, 6, 2, 4] # the list to be sorted
print("The list to be sorted", my_list)
'''
for i in range(len(my_list) - 1): # we need 5 -1 comparisons
    if my_list[i] > my_list[i + 1]: # compare adjacent element
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    print(my_list)
'''
print("'We'll sort the list")
'''
swapped = True
while True:
    swapped = False # no swap so far
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
'''
swapped = True
while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)