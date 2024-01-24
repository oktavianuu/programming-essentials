# recursive implementation of factorial function

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter your favorite number: "))
print(factorial(n))