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
We can also insert an item to a dictionary by using the ```update()``` method, and remove the last element by using the ```popitem()``` method, e.g.:
```python
pol_eng_dictionary = {"kwiat": "flower"}

pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary) # outputs: {'kwiat': 'flower', 'gleba': 'soil'}

pop_eng_dictionary.popitem()
print(pol_eng_dictionary) # outputs: {'kwiat': 'flower'}
```
5. We can use ```for``` loop through a dictionary:
```python
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
}
for item in pol_eng_dictionary:
    print(item)

# outputs: zamek
#          woda
#          gleba
```
6. If we want to loop through a dictionary's keys and values, we can use the ```items()``` method, e.g.:
```python
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value)
```
7. To check if a given key exists in a dictionary, we can use in keyword:
```python
pol_eng_dict = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
}

if "zamek" in pol_eng_dictionary:
    print("Yes")
else:
    print("No")
```
8. We can use ```del``` keyword to remove a specific item, or delete a dictionary. To remove all dictionary's items, we need to use ```clear()``` method:
```python
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

print(len(pol_eng_dictionary)) # outputs: 3
del pol_eng_dictionary["zamek"] # removes an item
print(len(pol_eng_dictionary)) # outputs: 2

pol_eng_dictionary.clear() # removes all the itmes
print(len(pol_eng_dictionary)) # outputs: 0

del pol_eng_dictionary # removes the dictionary
```
9. Use ```copy()``` method to copy a dictionary:
```python
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

copy_dictionary = pol_eng_dictionary.copy()
```
    