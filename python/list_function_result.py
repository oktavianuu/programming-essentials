def strange_list_fun(n):
    list_fun = []

    for i in range(0, n):
        list_fun.insert(0, i)
    
    return list_fun

my_range = int(input("Enter range for your list: "))
print("here is your list: ")
print(strange_list_fun(my_range))