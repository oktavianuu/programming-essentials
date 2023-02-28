beatles = []
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print('The current members of the beetles are', beatles)

new_beetles_members = input("Add Stu Sutcliffe to the beetels: ")
beatles.append(new_beetles_members)
new_beetles_members = input("Add Pete Best to the beatles: ")
beatles.append(new_beetles_members)
print("The current members of the beatles are: ", beatles)

del beatles[-1]
del beatles[-1]
print("The current members of the beatles are: ", beatles)

beatles.insert(0, 'Ringo Starr')
print("The current members of the beatles are: ", beatles)
