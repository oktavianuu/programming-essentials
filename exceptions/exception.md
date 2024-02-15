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
