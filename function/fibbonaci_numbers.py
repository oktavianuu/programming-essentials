"""
rules of fibbonaci numbers:
1. the first element of the sequence is equal to one (Fib1 = 1)
2. the second is also equal to 1
3. every subsequent number is the_sum of the two preceding numbers: (Fib(i) = Fib(i-1) + Fib(i-2)) 
"""

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1 
    
    elem_1 = elem_2 = 1
    the_sum = 0

    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2 # the next number is the sum of the two preceding numbers
        elem_1, elem_2 = elem_2, the_sum # move the elem_1 and elem_2 
    return the_sum # variables through the subsequent Fibonacci numbers.

# testing
for n in range(1, 10):
    print(n, "->", fib(n))