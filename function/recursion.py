# recursion is a technique where a function invokes itself.

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n-1)

for n in range(1, 5):
    print(n, "->", factorial_function(n))