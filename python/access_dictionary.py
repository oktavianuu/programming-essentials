dictionary = {
    "cat": "chat", 
    "dog": "chien", 
    "horse": "cheval"
    }

# accessing dictionary with keys()
print("keys() method")
for key in dictionary.keys():
    print(key, "->", dictionary[key])

# because dictionary isn't a seq type, we cannot just use for loop like list
# but instead, we can use for loop with key to access the key and value of a dictionary

# accessing dictionary with items()
print("items() method")
for english, french in dictionary.items():
    print(english, "->", french)

print("values() method")
for french in dictionary.values():
    print(french)

# MODIFYING DICTIONARY
# modifying including adding values is simple since dictionary is fully mutable
print("\ndictionary: replacing value")
print("Here is the the dictionary:")
print(dictionary)
print("replacing 'cat' with 'minou'")
dictionary['cat'] = 'minou'
print("\nThis is the output:")
print(dictionary)

print("\nADDING NEW KEY")
# is simple as changing value, we just need to assign a value to a new previously non-existent key.
print("current dictionary")
print(dictionary)
dictionary['swan'] = 'cygne'
print("This is the new modified dictionary:")
print(dictionary)

# we can also use updates() method to add new value
print("\nusing updates() method")
print("current dictionary")
print(dictionary)
dictionary.update({'duck': 'canard'})

# REMOVE KEY
# remove key will always causing the associated value to be removed from the dictionary
print("\nREMOVING KEY")
print("removing key can be done with del instruction and will always the associated value.")
del dictionary['dog']
print("updated dictionary")
print(dictionary)

# we can use popitem() method to 
print("\ndictionary before popitem()")
dictionary.popitem()
print("dictionary after popitem():")
print(dictionary)
