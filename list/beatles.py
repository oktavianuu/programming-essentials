beatles = [] # create an empty list

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("The beatle after append: ")
print(beatles)

for member in range(2):
    new_member = input("Enter a new member: ")
    beatles.append(new_member)
print(beatles)

del beatles[-1]
del beatles[-2]

print("The Beatles after applying del:")
print(beatles)

beatles.insert(0, "Ringo Starr")
print("The Beatles member after applying insert: ")
print(beatles)