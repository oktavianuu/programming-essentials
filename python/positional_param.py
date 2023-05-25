# function arguments are dictated by its positions

def intro(first_name, llast_name):
    print("hello my name is", first_name, llast_name + "!")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
intro(first_name, last_name)