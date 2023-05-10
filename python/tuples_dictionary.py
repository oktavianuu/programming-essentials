# here is the example of how tuples and dictionary work together

# SCENARIO:
# you need a program to evaluate the students' average scores;
# the program should ask for the student's name, followed by her/his single score;
# the names may be entered in any order;
# entering an empty name finishes the inputting of the data (note 1: entering an empty score will raise the ValueError exception, but don't worry about that now, you'll see how to handle such cases when we talk about exceptions in the second part of the Python Essentials course series)
# a list of all names, together with the evaluated average score, should be then emitted.
school_class = {} # empty dic to input data, student's name as the key, while the associated value wil be stored in a tuple
                  # tuple can be used as dictionary value, no problem at all.

while True: # enter an infinite loop, it will terminates at the right moment
    name = input("Enter the student's name: ") # read the students' name
    if name == '': # if the name is empty string, leave the loop
        break 

    score = int(input("Enter the student's score (0-10): ")) # ask student score
    if score not in range(0, 11): # if the score is not within the range of 10
        break                     # leave the loop

    if name in school_class: # if the name of the students already in the class, lengthen the associated 
        school_class[name] += (score,) # tuple with new score
    else:
        school_class[name] = (score,) # if the student is new then, the name will be added to the dict with the score as the value

for name in sorted(school_class.keys()): # iterate through the sorted students name
    adding = 0 # initialize the data needed to evaluate the average (sum and counter)
    counter = 0 # initialize the data needed to evaluate the average (sum and counter)
    for score in school_class[name]: # iterate through the tuple, taking all the subsequent scores 
        adding += score              # and updating the sum, together with the counter;
        counter += 1
    print(name, ":", adding/counter) # evaluate and print the student's name and average score.

print(school_class)
