dictionary = {
    "cat": "chat", 
    "dog": "chien", 
    "horse": "cheval"
    }

# checking words in dictionary by check its key
words = ['cat', 'dog', 'horse', 'lion']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "isn't present in dictionary!")