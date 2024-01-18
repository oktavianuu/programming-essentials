"""
This time, we'll ask the user to input or enter three values and then our function will deal with those values.
"""
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Enter the first side\'s length: "))
b = float(input("Enter the second side\'s length: "))
c = float(input("Enter the third side\'s length: "))

result = is_a_triangle(a, b, c)
if result:
    print("Yes, it can be a triangle.")
else:
    print('No, it can be a triangle.')

# The hypotenuse is the longest side
def is_a_right_triangle(a, b, c):
    if not is_a_triangle:
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    
