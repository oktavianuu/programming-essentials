# dictionary is are unordered*, changeable (mutable), and indexed collections of data. (*In Python 3.6x dictionaries 
# have become ordered by default.

# STRUCTURE
my_dictionary = {
    "key1": 1,
    "key2": 2.0,
    "key3": "yes",
}

# ACCESSING DICTIONARY
# we can access dictionary by making reference to the key inside dictionary or by using get() method.
item_1 = my_dictionary["key1"]
print(item_1)
item_2 = my_dictionary.get("key2")
print(item_2, "\n")

# CHANGE VALUE
# If you want to change the value associated with a specific key, you can do so by referring to the item's key name in 
# the following way:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

pol_eng_dictionary["zamek"] = "lock"
updated_item = pol_eng_dictionary["zamek"]
print(updated_item, "\n")

# ADDING AND REMOVING KEY
# To add or remove a key (and the associated value), use the following syntax:
phonebook = {} # empty dictionary
phonebook["Okta"] = 3456783958    # create/add a key-value pair
print("phonebook after adding key-value:")
print(phonebook)
del phonebook["Okta"]
print("phonebook after deleting item using del")
print(phonebook)

# INSERT AND REMOVE THE LAST ELEMENT
pol_eng_dictionary = {"kwiat": "flower"}
print("initial dictionary:")
print(pol_eng_dictionary)
pol_eng_dictionary.update({"gleba":"soil"}) # insert one key-value pair 
print("updated dictionary")
print(pol_eng_dictionary, "\n")
pol_eng_dictionary.popitem()
print("udpated dictionary after removing the last item using popitem() method")
print(pol_eng_dictionary)

# LOOPING
# looping key
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
for item in pol_eng_dictionary:
    print(item) 

# looping key value using item() method
for key, value in pol_eng_dictionary.items():
    print("pol/eng ->", key, ":", value)

# check if a given key exists
if "zamek" in pol_eng_dictionary:
    print("Yes")
else:
    print("No")

# REMOVE SPECIFIC ITEM 
print("\nThe initial length of dictionary:")
print(len(pol_eng_dictionary))
del pol_eng_dictionary['zamek'] # delete
print("The dictionary length after deleting one item:")
print(pol_eng_dictionary)

# clear item using clear() method
print("remove all items using clear() method")
pol_eng_dictionary.clear()
print("the length of dictionary after applying clear method to it:")
print(len(pol_eng_dictionary))

# remove dictionary
# we can remove the dictionary by using del and put the dictionary's name right after del
# del pol_eng_dictionary

# COPY
# to copy dictionary, we can use copy() method
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
copied_dictionary = pol_eng_dictionary.copy()

# glue two dictionary together
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)
print(d3)

# convert tuple to dictionary
colors = (("green", "#008000"), ("blue", "#0000FF"))
dic = dict(colors)
