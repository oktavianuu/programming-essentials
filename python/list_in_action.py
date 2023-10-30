my_list = [10, 1, 8, 3, 5]
print("Our list before swapping: ")
print(my_list)

# imagine if we want to swap the element. Traditionally, we will do the following:
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print("Our list after swapping: ")
print(my_list)

# Imagine if we have 100 element in a list, then we want to swap the element, what will we do? It will be hard for us to swap it.
# We can use for loops to do it.
my_list = [10, 1, 8, 3, 5]
print("We use for loop to swap the element:")
length = len(my_list)
for i in range(length//2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[1]

print("Modification after foor loop:")
print(my_list)