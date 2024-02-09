### Tuple Overview
1. Tuples are ordered and unchangeable (immutable) collections of data. They can be thought of as immutable lists. They are written in round brackets:
```python
my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
my_list = [1, 2, True, "s string", (3, 4), [5,6], None]
```
Each tuple element maybe of a different type (i.e., integers, strings, booleans, etc.) What is more, tuples can contain other tuples or lists (and the other way round).
2. we can create empty list:
```python
empty_tuple = ()
```
3. A one-element tuple:
```python
one_elem_tuple_1 = ("one", )    # Brackets and a comma.
one_elem_tuple_2 = "one",       # No brackets, just a comma.
# NOTE: if we remove comma ",", we'll create variable instead of tuple.
```
4. we can access tuple by indexing them:
```python
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(my_tuple[3])    # outputs: [3, 4]
```
5. Tuples are immutable, which means we cannot change their elements (we cannot append tuples, or modify, or remove tuple elements). The following snippet will cause an exception:
```python
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
my_tuple[2] = "guitar" # The TypeError exception will be raised.
```
NOTE: however, we can delete tuple as a whole:
```python
my_tuple = 1, 2, 3, 
del my_tuple
print(my_tuple) #nameError: name 'my_tuple' is not defined
```

Loop through a tuple element:
```python
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)
```
Check of specific element not present in a tuple:
```python
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)
```
check how many elements in a tuple using ```len()```:
```python
tuple_3 = (1, 2, 3, 4, 5)
print(len(tuple_3))
```
join/multipy multiple tuples:
```python
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2

print(tuple_4)
print(tuple_5)
```

#### EXTRA
We can create a tuple using a python built-in function called tuple(). This is particularly useful when we want to convert a certain iterable (e.g., a list, range, string, etc.) to a tuple:
```python
my_tup = tuple((1, 2, "string"))

my_list = [1, 2, 4]
print(type(my_list)) # output <class 'list'>

tup = tuple(my_list)
print(type(tup)) # output <class 'tuple'>
```
By the same fashion, we may convert any iterable to a list using ```list()``` function:
```python 
tup = 1, 2, 3
my_list = list(tup)
print(type(my_list))
```