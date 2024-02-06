school_class = {} # initialize empty dict to store the data

while True: # infinite loop as long as the condition is true
    name = input("Enter the student's name: ") # read the student's name
    if name == "": #if the name is empty
        break       # leave the loop

    score = int(input("Enter the student's score (0-10): ")) # ask for one of the student's score (integer range 0-10)
    if score not in range(0, 11): # if the score is not in range 0-10
        break # leave the loop

    if name in school_class: # if the name of the student is already in the dictionary
        school_class[name] += (score, ) # lengthen the associated tuple with the new score (the "+=" operator)
    else:                   # if this is a new student (unknown to the dict),
        school_class[name] = (score, ) # create a new entry, its value is a one-element tuple containing the entered score
    
for name in sorted(school_class.keys()): # iterate through the 
    adding = 0 # initialize the data needed to evaluate the average sum 
    counter = 0 # nitialize the data needed to evaluate the average counter

    # iterate through the tuple, taking all the subsequent scores and updating the sum, together with the counter;
    for score in school_class[name]:
        adding += score
        counter += 1
    # evaluate and print the student's name and average score.
    print(name, ":", adding/counter)
                