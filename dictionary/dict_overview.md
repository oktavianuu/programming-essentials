### Dictionary: overview

1. Dictionaries are unordered*, changeable (mutable), and indexed collections of data. (*In Python 3.6x dictionaries have become ordered by default).
Each dictionary is a set of key: value pairs. You can create it by using the following syntax:
```python
my_dictionary = {
    key1: value1,
    key2: value2,
    key3: value3,
}
```
2. If we want to access a dictionary item, we can do so by making a reference to its key inside a pair of square brackets or by using the ```get()``` method:
```python
pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }

item_1 = pol_eng_dictionary["gleba"]    # ex. 1
print(item_1)    # outputs: soil

item_2 = pol_eng_dictionary.get("woda")
print(item_2)    # outputs: water
```
3. If we want to change the value associated with a specific key, we can we can do so by referring to the item's key name in the following way:
```python
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

pol_eng_dictionary["zamek"] = "lock"
item = pol_eng_dictionary["zamek"]    
print(item)  # outputs: lock
```
4. To add or remove a key (and the associated value), use the following syntax:
```python
phonebook = {} #empty dictionary

phonebook["Adam"] = 3456783958 # create/add a key-value pair
print(phonebook) # outputs: {'Adam': 3456783958}

del phonebook["Adam"]
print(phonebook) # outputs: {}
```
