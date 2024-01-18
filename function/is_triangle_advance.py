"""
This time, we'll ask the user to input or enter three values and then our function will deal with those values.
"""
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Enter the first side\'s length: "))
b = float(input("Enter the second side\'s length: "))
c = float(input("Enter the third side\'s length: "))

result = is_a_triangle(a, b, c)
print(result)