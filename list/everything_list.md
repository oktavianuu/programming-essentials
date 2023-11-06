# Why do we need list?

We need list when we're about to write a variable than can store many value; hundred or thousand or even million?

List is unique and different from another scalar variable. In list, we put the value inside suare brackets and use comma to separate the value as the following example:

```python
numbers = [1, 2, 3, 4, 5]
```

In the above example, ```numbers``` is a list variable consisting of five values, all of them are numbers. List may contain different types of data, e.g., integer, character, float or even another list. In short, list is a collection of elements, but each element is a scalar. 

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
NOTE: we may use  ```len()``` function to check how many element inside a list. 

### Removing Element From a List
We can remove an element from a list using an instruction. The instruction is called ```del``` as follow:
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
