#What does this mean: *args, **kwargs?
# And why would we use it?

'''
In python, we can pass a avariable number of arguments to 
a function using special symbols. There are two special symbols.

1. *args (Non keyword arguments)
2. **kwargs (keyword argumens)

USE:
We use *args and **kwargs as an argument inside function when
we are not sure about the number of arguments to pass in the functions.
that time we can use this arguments inside a fuction.


PYTHON *args:

Python has *args which allow us to pass the non keyword arguments
inside function.In this function we should use an asterisk * before
the parameter name and it passes variable length of arguments.
The arguments are passed as a tuple and these passed arguments
make tuple inside the function with same name as the parameter
excluding asterisk * .

SYNTAX; func_name(*args) ----> [same as func_name(*args or (1,2,3))]

#EXAMPLE:

def func(*args):
    add = 0
    for x in args: #1,
        add = x + add
    print("sum of all nos:",add)
func(3,4,8)
func(1,2,3,4)

PYTHON **kwargs:

Python has **kwargs which allow us to pass the keyword arguments
inside function.In this function we should use an asterisk ** before
the parameter name and it passes variable length of arguments.
The arguments are passed as a dictionary and these passed arguments
make dictionary inside the function with same name as the parameter
excluding asterisk ** .

SYNTAX; func_name(**kwargs) ----> [same as func_name(*kwargs or [1:"value",2:"value"])]

#EXAMPLE:

def details_of_emp(**kwargs):
    print(type(kwargs))

    for key,value in kwargs.items():
        print(key,value)

details_of_emp(idno = 101,name = 'mohan')
'''