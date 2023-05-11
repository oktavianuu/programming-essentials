# initialize tuple
tuple_1 = (1, 2, 3)
print(tuple_1[2]) # accessing tuple by its index

# unzip tuple
a, b, c = tuple_1
print(a * b * c) # applying multiplication --> 6

# count method
tup_2 = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup_2.count(2)
print(duplicates) # --> 4

# converst list to tuple
my_list = ["car", "Ford", "flower", "Tulip"]
t = tuple(my_list)