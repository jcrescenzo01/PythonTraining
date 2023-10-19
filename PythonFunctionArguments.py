"""
    difference between arguments and parameters
    positional and keyword arguments
    default arguments
    variable-length arguments (*args and **kwargs)
    container unpacking into function arguments
    Local vs. global arguments
    parameter passing (by value or by reference?)
"""


# Arguments Vs. Parameters
# Parameters are the variables used and defined inside parenthesis while
    # defining a function
# Arguments are the values passed for said parameters while calling a
    # function
"""
def print_name(name):       # name is the parameter
    print(name) 
    
print_name('Alex')          # 'Alex' is te argument
"""

"""
def foo(a,b,c):
    print(a,b,c)

foo(1,2,3)
foo(a=1,b=2,c=3)
print()
foo(c=1,b=2,a=3)        # prints "3 2 1" as foo(a,b,c) means a will be first
                        # using keyword arguments, only the keywords matter
                        # not the position
print()

foo(1,b=2,c=3)          #positional argument can come before keyword args
#foo(1,b=2,3)            # cant after keywords though, error
                        # keywords are good because they make it more clear
"""

"""
def foo(a,b,c,d=4):         # d defaults to 4
    print(a,b,c,d)

foo(1,2,3)                  # prints d as 4 because thats its default
foo(1,2,3,7)                # 7 replaces 4 as its just a default value
"""

"""
#default arguments MUST be at the end, or else error
def foo(a,b=2,c,d=4):         # b=2 causes the error because a non-default comes after it
    print(a,b,c,d)
"""

"""
# *paramName     any number of positional arguments can be passed to your function
    # typically called *args, but doesn't need to be
# **paramName    any number of keyword arguments can be passed to your function
    # typically called **kwargs, but doesn't need to be
# see below:
def foo(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
foo(1,2,3,4,5,six=6,seven=7)
"""
"""
foo prints this:
1 2         # print(a,b)
3           # for arg in args: print(arg)
4
5
six 6       # for key in kwargs:  print(key, kwargs[key])
seven 7

you could also just use keywords or positionals if wanted here
"""

# Forced Keyword Arguments
"""
def foo(a,b,*,c,d):     # every param after the star must be a keyword argument
    print(a,b,c,d)

#foo(1,2,3,4)       # raises an error because c and d must be keyword arguments
foo(1,2,c=3,d=4)    # functions correctly

print()
def foo1(*args, last):
    for arg in args:
        print(arg)
    print(last)
#foo1(1,2,3)                # last parameter is missing so error
foo1(1,2,3, last=100)       # functions because last is there at the end
"""


# Unpacking Arguments
"""
def foo(a,b,c):
    print(a,b,c)

mylist = [0,1,2]
mytuple = (0,1,2)
#foo(mylist)         # fails since it sees mylist as one argument
foo(*mylist)        # the asterisk causes it to account for the index contents as arguments
                    # note that container length must be equivelent to the the arguments for the
                    # funct, meaning 3 arguments long in this case

foo(*mytuple)       # works on tuples too

mydict = {'a': 12,'b': 3,'c': 90,}
foo(**mydict)       # unpack dictionary with 2 asterisks (**)
                    # length of dict and key names of the dict must match
"""

# Local vs Global variables
"""
def foo():
    x = number                              # global variable
    #number = 3                             # raises error b/c created local variable
                                            # that is now different than the global variable
    print('number inside function:', x)

number = 0
foo()
"""
"""
def foo():
    global number
    x = number
    number = 3
    print('number inside function:', x)

number = 0
foo()
print(number)       # 3, so it works correctly

# if we dont assign global to number, it prints 0 instead despite the funct call b/c
# number=3 creates a new local variable, only existing in the funct - doesnt modify the global
# variable.
"""


# Parameter Passing
#   call by object / call by object reference
#   parameter parsed is a reference to an object, but the ref is passe by value
#   there is a difference between mutable and immutable data types
#       mutable:     mutable objects like lists and dicts can be changed in a method but if you
#           rebind the refere3nce in the method then the outer ref will still point to the
#           original object and it isnt changed
#       immutable:   m objects like ints and strings cant be changed in a method, but immutable
#           objects contained in a mutable object can be reassigned within the method
"""
def foo(x):
    x = 5

var = 10
foo(var)
print(var)      # still prints 10 despite trying to change it, since var is an integer and is
                # immutable / can be changed, instead makes a local variable called x that has
                # nothing to do with var: immuties cant be changed
"""
def foo(alist):
    #alist = [200,300,400]       # gets overwritten and prints 123 below since we rebound the
                                    # reference, alist with these new numbers is a Local Variable
                                    # and doesnt effect the global
    #alist += [200, 300, 400]     # appends 200, 300, and 400 between 3 and 4, global list was effected
    alist = alist + [200,300,400] # doesnt change the mylist b/c it creates a local variable
    alist.append(4)
    alist[0] = -100

mylist = [1,2,3]
foo(mylist)
print(mylist)       # since lists are mutable, the 4 remains appended to it
