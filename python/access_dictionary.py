dictionary = {
    "cat": "chat", 
    "dog": "chien", 
    "horse": "cheval"
    }

for key in dictionary.keys():
    print(key, "->", dictionary[key])

# because dictionary isn't a seq type, we cannot just use for loop like list
# but instead, we can use for loop with key to access the key and value of a dictionary
