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

