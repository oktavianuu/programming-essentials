print("The initial list: ")
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(my_list)

unique_list = []
for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
my_list = unique_list

print(" ")
print("The list containing unique elements: ")
print(my_list)
