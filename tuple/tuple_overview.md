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
