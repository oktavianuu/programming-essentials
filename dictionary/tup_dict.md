### Tuple and dictionary can work together

Let's imagine the following problem:

* you need a program to evaluate the students' average scores;
* the program should ask for the student's name, followed by her/his single score;
* the names may be entered in any order;
* entering an empty name finishes the inputting of the data (note 1: entering an empty score will raise the ValueError exception, but don't worry about that now, you'll see how to handle such cases when we talk about exceptions in the second part of the Python Essentials course series)
* a list of all names, together with the evaluated average score, should be then emitted.