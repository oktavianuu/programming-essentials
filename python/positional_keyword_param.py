# we can mix both positional and keyword parameters
# but there is one rule we must obeyed, the positional param must be placed before keyword paaram

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

number_a = int(input("Enter number a: "))
number_b = int(input("Enter number b: "))
number_c = int(input("Enter number c: "))

adding(number_a, number_b, number_c)

# mix
adding(5, c = 2, b = 3) # this is legal and okay
adding(5, a = 4, c = 3) # this will causes TypeError since we assign multple value for one argument.
