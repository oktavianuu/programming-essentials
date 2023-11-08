# Why do we need list?

We need list when we're about to write a variable than can store many value; hundred or thousand or even million?

List is unique and different from another scalar variable. In list, we put the value inside suare brackets and use comma to separate the value as the following example:

```python
numbers = [1, 2, 3, 4, 5]
```

In the above example, ``numbers`` is a list variable consisting of five values, all of them are numbers. List may contain different types of data, e.g., integer, character, float or even another list. In short, list is a collection of elements, but each element is a scalar.

### Indexing Lists

Indexing means how do we access a list content. We access list contenet by using square bracket as follow:

```python
numbers[0] # will select the first element of the list.
numbers[3] # will select the fourth element of the list.
```

We can also modify list by using its index and square brackets like so:

```python
numbers[0] = 150 # replace the first element by 150.
numbers[-1] = 200 # replace the last element of the list by 200.
numbers[1] = numbers[3] # copying element at index 3 to elelemnt at index 1 in list "numbers"
```

NOTE: we may use  ``len()`` function to check how many element inside a list.

### Removing Element From a List

We can remove an element from a list using an instruction. The instruction is called ``del`` as follow:

```python
del numbers[2]
```

The expression above remove element at index 2 from the list. It is important to rememeber that we can't access an element that doen't exist. So it is crucial to know that we cannot access element outside a range of the list. Look at the example below:

```python
print(numbers[5])
```

The expression above will cause an error.
Another way to access element from a list is by using negative indices. look at the example below:

```python
numbers[-1] # select the very last element of the list numbers
numbers[-2] # select the one before the last one
```

### Function vs Method

A method is specific kind of function; it behaves like a function and looks like a function, but diffes in the way in which it acts, and in its invocation style.

A **function** does not belong to any data ~ it gets data, it may create data and it (generally) produces a result. A __method__ does all these things, but is also able to change the state of a selected entity.
NOTE: __A methodis owned by the data it works for, while a function is owned by the whole code__.
The following code is a clear example of how to use method and function.
__Function:__

```python
result = function(arg)
```

A function takes an argument, does something, and returns a result.
__Method:__

```python
result = data.method(arg)
```

The method will behave like a function, but can do something more - it can change the internal state of the data from which it has been invoked.

You may ask: why are we talking about methods, not about lists?

This is an essential issue right now, as we're going to show you how to add new elements to an existing list. This can be done with methods owned by all the lists, not by functions.

### Important List Operations Concept

* If we have list ``L1``, then the following assignment: ``L2 = L1`` does not make copy of L1 but makes the variables L1 and L2 point to one and the same list in computer memory. For example:

```python
> vehicles_one = ['car', 'bicycle', 'motor']
> print(vehicles_one) 
> outputs: ['car', 'bicycle', 'motor']

> vehicles_two = vehicles_one
> del vehicles_one[0] # deletes 'car'
> print(vehicles_two)
> outputs: ['bicycle', 'motor']
```

* If we want to copy a list, me can do it by performing slice on that list, for example:

```python
> colors = ['red', 'green', 'orange']

> whole_colors = colors[:] # copying whole colors
> part_colors = colors[:2] #copying two first elements 
```

* We can use negative indices to perform slicing too:

```python
> sample_list = ["A", "B", "C", "D", "E"]
> new_list = sample_list[2:-1] # slice 'C' and 'D' and copied it to new_list
> print(new_list)
> outputs: ['C', 'D']
```

* The general rule for slicing a list as is ``list[start:end]``, with ``start`` and ``end`` are indices. They're optional; if we want to copy all list content, we don't have to specify the indices just use the ``:``.
* We can delete list or content of the list using ``del`` instruction:

```python
> my_list = [1, 2, 3, 4, 5]
> del my_list[0:2]
> print(my_list)  # outputs: [3, 4, 5]

> del my_list[:]
> print(my_list)  # deletes the list content, 
> outputs: []
```

* We can test if some items exist in a list or not using the ``in`` and ``not in`` keywords:

```python
> my_list = ["A", "B", 1, 2]
> "A" in my_list
> outputs: True
> "C" not in my_list
> outputs: True
> 2 not in my_list
> False
```

### Lists in list

Lists can contain variety of data types including scalars and non-scalar value such as string, boolean or even more complex structure such as list itself.
Sometimes, we want to use list as element in our list. We often find such arrays in our daily lives, the simple example is chessboard.
A chessboard composed of rows and columns, there are eight rows and eight columns. Each column is marked with the letters A through H. Each line is marked with a number from one to eight. Each line is marked with a number from 1 to 8.
The location of each filed is identified by letter-digits pairs. Thus we know that the bottom left corner of the board (the one with white rook) is A1, while the opposite corner is H8.

If we assume that we're able to use the selected numbers to represent any chess piece. We can also assume that every row on the cheesboard is a list.
Look at the code below:
```python
> row = []
for i in range(8):
    row.append(WHITE_PAWN)
```
It builds a list containing eight elements representing the second row of the chessboard - the one filled with pawns (assume that WHITE_PAWN is a predefined symbol representing a white pawn).

The same effect may be achieved by means of a list comprehension, the special syntax used by Python in order to fill massive lists.

A list comprehension is actually a list, but created on-the-fly during program execution, and is not described statically.

Take a look at the snippet:
```python
row = [WHITE_PAWN for i in range(8)]
```
The part of the code placed inside the brackets specify:
* the data to be used to fill the list (WHITE_PAWN)
* the clause specifying how many the data occurs inside the list ```(for i in range(8))```

Lets take a closer look to the following example:
```python
sq = [x ** 2 for x in range(1, 11)]
```
The above code will generate a list with 10 elements. Here is how the list generated:
* ```range(1, 11)``` creates an iterable that yields numebers from 1 to 10. It generates the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9,10. 
* The list comprehension is enclosed in square brackets ```[...]``` which indicates that it will produce list.
* ```x``` is the variable that represent each element of the iterable (in this case, the number from 1 to 10) as the list comprehension iterates over them. 
* ```x ** 2``` calculates the square of the current value of ```x```.
* The entire list comprehension is wrapped in aquare brackets ```[...]```, which collects all the square values into a list. 
* it will produce the following elements:
```[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]``` and is assigned to the sq variable. 

### Lists in lists: two-dimensional arrays
We assume that ```EMPTY``` is a predefined symbol designates an empty field on the cheessboard. So, if we want to create a list of lists representing the whole chessboard, it may be done in the following way:
```python
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
```
Explanation:
* the inner part of the loop 
