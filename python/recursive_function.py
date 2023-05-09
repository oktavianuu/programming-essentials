# recursive implementation of the factorial function

def factorial(n):
    if n == 1:      # the base case, termination condition
        return 1
    else:
        return n * factorial(n - 1) # call the fucntion factorial itself

print(factorial(4))
