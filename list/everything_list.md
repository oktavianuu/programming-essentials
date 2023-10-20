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
numbers[1] = numbers[3] #
```
