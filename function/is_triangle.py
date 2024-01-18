"""
1. Function to check whether three sides of given lengths can build a triangle.
2. We know from school that the sum of two arbitrary sides has to be longer than the third side.
3. The function will have three parameters - one for each side.
4. It will return True if the sides can build a triangle, and False otherwise.
"""

# version 1
print("version A:")
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
print()

# version 2
print("version B:")
def is_a_triangle2(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print("version B:")
print(is_a_triangle2(1, 1, 1))
print(is_a_triangle2(1, 1, 3))
print()

# version 3
print("version C:")
def is_a_triangle3(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle3(1, 1, 1))
print(is_a_triangle3(1, 1, 3))
