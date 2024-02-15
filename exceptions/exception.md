Look at the following code:
```python
try:
    # it's a place where  
    # we can do something
    # without asking for permission
except:
    # it is a spot dedicated to 
    # solemnly begging for forgiveness
```
We can see two branches here:
* ```try``` keyword - this is the place where we put the code we suspect is risky and may be terminated in case of error; note: this kind of error is called an **exception**, while the exception occurence is called **raising** - we can say that the exception is (or was) raised.
* second, ```except``` keyword is designed to handle the exception, it is up to us what we want to do here. We can clean up the mess or we can just sweep the problem under the carpet (first solution is recommended).

As we can see, this approach accepts errors (treats them as a normal part of the program's life) instead of escalating efforts to avoid errors at all.

#### The exceptopn proves the rule
Look at the following code:
```python
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')
```
let us summarize:
* Any part of the code placed between ```try``` and ```except```is executed in a very special way, any error which occurs here won't terminate program execution. Instead, the control will immediately jump to the first line situated after the ```except``` keyword, and no other part of the ```try``` branch is executed.
* the code inside the ```except``` branch is activated only only when exception has been encountered inside the ```try``` block. There is no way to get there by any other means.
* whether either the ```try``` block or the ```except```block is executed successfully, the control returns to the normal path of execution, and any code located beyond in the source file is executed as if nothing happened.

#### How to deal with more than one exception
There is more than one possible way to raise an exception. For example, a user may enter zero as an input. When that happen, it will raise an error. When we divide zero by any numbers, it will cause ```ZeroDivisionError```. 

There are at least two approaches you can implement here:
#### First, two separate ```try``` block
The first approach is simple and complicated at the same time: we can just add two separate try blocks, one including the input() function invocation where the ValueError may be raised, and the second devoted to handling possible issues induced by the division. Both these try blocks would have their own except branches, and in effect you will gain full control over two different errors.

NOTE: this solution is good bit it is a bit lengthy. The code becomes unnecessarily bloated. Moreover, it is not the only danger that awaits you. Note that leaving the first ```try-except``` leaves a lot of uncertainty - we will have to add extra code that ensure that the value is the user has entered is safe to use in division. This is how seemingly simple solution becomes overly complicated. Fortunately, python offers a simpler way to deal with this kind of challenge.

#### Second,two ```exceptions``` after one try
Here is how to handle the problem with two exceptions after one try:
```python
try: 
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:
    print('Division by zero is not allowed in our universe.')
```
As we can see, we've introduced the second except branch. This is not the only difference-note that both exception branches have exception names specified. In this solution, each of the expected exceptions has its own way of handling error, but it must be emphasized that only one of all branches can intercept the control, **if one of the branches is executed, all the other branches remain idle.**

Additionally, the number ```except``` branches is not limited, we can specify as many or as few of them as we need, but we must remember that **none of the exceptions can be specified more than once**

#### The default exceptions and how to use it 
Look at the code below:
```python
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')
```
We've added third except branch, but this time it has no exception name specified - we can say it's anonymous or (what is closer to its actual role) it's the **default**. We can expect that when an exception is raised and there is no ```except``` branch dedicated to this exception, it will be handled by the default branch.
NOTE: the 