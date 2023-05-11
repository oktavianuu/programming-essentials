# Errors – the developer's daily bread

# 1 Errors in data
# this happen when the data provided by the user cannot be processed by our program
# using a try and except
# structure
# main code:
    # try:
        # this is the place where you put the code you suspect is risky and may be terminated in case of error; 
        # note: this kind of error is called an exception, while the exception occurrence is called raising – 
        # we can say that an exception is (or was) raised;
    # except:
        # designed to handle the exception; it's up to you what you want to do here: you can clean up the mess or 
        # you can just sweep the problem under the carpet (although we would prefer the first solution).
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except:
    print("I don't know what to do.")

# deal with more than one exception:
try:    
    value = int(input('Enter a natural number: '))    
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:    
    print('I do not know what to do.')   
except ZeroDivisionError:    
    print('Division by zero is not allowed in our Universe.')
except:
    print('Something strange has happened here... Sorry!')

# some useful exceptions
# 1 ZeroDivisionError
    # This appears when you try to force Python to perform any operation which provokes division in which the divider is 
    # zero, or is indistinguishable from zero. Note that there is more than one Python operator which may cause this 
    # exception to raise

# 2 ValueError
    # Expect this exception when you're dealing with values which may be inappropriately used in some context. In general, 
    # this exception is raised when a function (like int() or float()) receives an argument of a proper type, but its value 
    # is unacceptable.

# 3 TypeError
# This exception shows up when you try to apply a data whose type cannot be accepted in the current context. 
# Look at the example:
short_list = [1]
one_value = short_list[0.5]
# You're not allowed to use a float value as a list index (the same rule applies to tuples, too). TypeError is an 
# adequate name to describe the problem, and an adequate exception to raise.

# 4 AttributeError
# This exception arrives – among other occasions – when you try to activate a method which doesn't exist in an item 
# you're dealing with. For example:
short_list = [1]
short_list.append(2)
short_list.depend(2)
# The third line of our example attempts to make use of a method which isn’t contained in the lists. This is the place 
# where AttributeError is raised.

# 5 SyntaxError
# This exception is raised when the control reaches a line of code which violates Python's grammar. It may sound strange, 
# but some errors of this kind cannot be identified without first running the code. This kind of behavior is typical of 
# interpreted languages – the interpreter always works in a hurry and has no time to scan the whole source code. It is 
# content with checking the code which is currently being run.
# t's a bad idea to handle this exception in your programs. You should produce code that is free of syntax errors, 
# instead of masking the faults you’ve caused.

# 2 Errors in code