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