### Dictionary
Dictionary is another python data structure. Not a sequence type but can be proccessed just like sequence and last but not least, it is mutable. 

Dictionary works exactly like dictionary. It has the word we need and the 'meaning' we want. In python's dictionary, the word we're looking for is called ```key```, and the 'meaning' of that worrd is called ```value```. This means that dictionary is a key-value pair.

Importance things to remember about dictionary:
* each key must be unique - it is not possible to have more than one key of the same value.
* a key may be any immutable type of object; it can be number (integer or float), or even a string but not a list;
* a dictionary is not a list, a list contains a set of  numbered values, while a dictionary holds pair of values.
* the ```len()``` function works for dictionary too, it returns the number of key-value pairs in dictionary.
* a dictionary is one-way tool, if you have an English-French dictionary, you can look for French equivalents of English terms, but not vice versa.

#### How to make dictionary?
```python
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
```
NOTE: the order of dictionary isn't in our control, so when we print something to the console, the order will be different from the actual assignment. 

#### How to use dictionary?
if we want to get any of the values in the dictionary, we need to deliver a valid key value:
```python
print(dictionary['cat'])
print(phone_numbers['Suzy'])
```
NOTE: key is case sensitive, ```suzy``` and ```Suzy``` are different. Trying to access a key that is not in the dictionary will cause runtime error. ```in``` and ```not in``` can be used to solve this issue:
```python
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = {'cat', 'lion', 'horse'}

for word in words:
    if word in dictionary:
        print(word, '->', dictionary[word])
    else:
        print(word, "is not in dictionary.")
```
NOTE: it is important to remember that when we write a big or lengthy expression, it might be a good idea to keep it verticlly aligned:
```python
# example 1:
dictionary = {
                "cat": "chat",
                "dog": "chien",
                "horse": "cheval"
            }

# example 2
phone_numbers = {'boss': 5551234567
                 'Suzy': 22657854310
                }
```
The kind of formatting above is called hanging indent.

#### Modifying and adding new ```key```
##### Modifying ```key```
dictionary is fully mutable so there will be no obstacle to modifying them.
```python
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)
```
In the code above, we will replace "chat" with "minou".
Output:
```
{'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}
```
##### Adding new ```key```
Adding a new key-value pair to a dictionary is as simple as changing a value - we only have to assign a value to a new, previously non-existent key.

Note: this is very different behavior compared to lists, which don't allow you to assign values to non-existing indices.
```python
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)
```
output:
```
{'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'}
```
EXTRA:
we can also insert an item to a dictionary by using the update() method, e.g.:
```python
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"})
print(dictionary)
```

#### Removing ```key```
Note: removing a key will always cause the removal of the associated value. Values cannot exist without their keys. This is done with the del instruction.
```python
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)
```
output:
```
{'cat': 'chat', 'horse': 'cheval'}
```
EXTRA:
To remove the last item in a dictionary, you can use the popitem() method:
```python
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem()
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}
```

#### How to use a dictionary: The ```keys()```
Can dictionaries be browsed using for loop, like lists or tuples?
No and Yes
