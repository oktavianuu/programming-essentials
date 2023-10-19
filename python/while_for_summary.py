# the while loop executes a statement or a set of statements as long as specified statement is true
# example 1
while True:
    print("Stuck in this while loop!")

# example 2
counter = 5
while counter > 2:
    print(counter)
    counter -=1

# the for loop executes a set of statements many times; it's used to iterate over a sequence, or other objects that are iterable (e.g., strings). You can use the for loop to iterate over a sequence of numbers using the built-in range function.
# Example 1:
word = "python"
for w in word:
    print(w, end="*")

# example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

# we can use the break and continue statements to change the flow of a loop:
# use break to exit a loop
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

# use continue to skip the current iteration, and continue with the next iteration
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter)

# The range() function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of range() looks as follows: range(start, stop, step), where:
        # start is an optional parameter specifying the starting number of the sequence (0 by default)
        # stop is an optional parameter specifying the end of the sequence generated (it is not included),
        # and step is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)
# example:
for i in range(2, 10, 3):
    print(i)

