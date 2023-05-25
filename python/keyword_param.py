# function arguments are dictated by its parameters name
def intro(fn, ln):
    print("Hello my name is", fn, ln)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

intro(first_name, last_name)
intro(last_name, first_name)

# in this case, the positions doesn't matter. Each argument's value knows its destination by the parameters' name

