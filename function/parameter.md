### FUNTION

Function is a special piece of code we can use to to certain task. One of the most important feature is that once a function has been created, it can be used anywhere within our code.

#### Parameter

Parameters are similar to variable but only live inside functions. To use parameter in a function, we use the following convention:

```python
function_name(parameter):
    funtion_body
```

We may apply multiple parameters as many as we wish:

```python
function_name(parameter1, paramater2, parameter3):
    function_body
```

#### What is the use of parameters?

In order to make use of parameters, we call the function with argument. Argument is the variable we use to access parameters. Here is the syntax:

```python
funtion_name(argument) # function call with argument 

function_name(argument1, argument2, argument3) # function call with more than one argument.
```

After we call the function, the value we enter in the argument will be transferefed to the parameters and will be executed based on the rule of function's body.

#### positional parameter passing

positional parameter passing is a technique we can use to asssign the i^th argument to i^th function parameter. The arguments passed in this way is called positional arguments. Study the following example:

```python
def intro(firs_name, last_name):
    print("Hello, I am", first_name, last_name)

# function call
intro("Luke", "Rockhold") # here we use positional argument and refer to the first and last name in the parameter.  
```

#### Keyword argument passing

Another way to pass argument aside from using its position is using its name. In this case, we use the parameter's name when calling the function. 
Study the following example:
```python
def intro(first_name, last_name):
    print("Hello, I am", first_name, last_name)

intro(first_name="Dmitry", last_name="Bivol") # function call
```
In the above example, we use the name exactly the same with parameter functions.

#### Mixing positional and keyword arguments
We can mix both positional and keyword argument. But one important thing to remember is that the positional argumnets must come first. We need to place the positional argument before keyword argument. Study the following example:
```python
def adding(a, b, c):
    print(a + b + c)

adding(4, 10, c=12) # mix positional and keyword argument
# The following function call is not correct:
adding(4, a=5, c=10) # thic call will generate error
```

#### Default (predefined) parameters' value
When a value is used more often than the other, we might consider to make such value default. Let's consider the followings scenario. Let's say that "Smith" is a very popular last name in a country so that a programmer write the following function:
```python
def intro(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
```
The above function has "Smith" as its default value for last_name parameter. This value stays as it is unless we change it. The following function calls are legal:
```python
intro("Henry") # positional argument, assign "Henry" to first_name. last_name will stays "Smith"
intro(first_name="Henry") # keyword argument, assign "Henry" to first_name and leave last_name to use its default value.
intro(first_name="Henry", last_name="Golding") # keyword argument, we change the default value here.

# all functions call above are legal :)
```

