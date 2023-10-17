# Decorators: Function and Class Decorators
import functools
"""a function decorator is a function that takes another function
as an argument and extends the behavior of the function without
explicitly modifying it"""
#@mydecorator # syntax for a decorator
#def dosomething():
#    pass

"""
# start_end_decorator for use with print_name
def start_end_decorator(func):
    def wrapper():
        print('Start')      # added to the input function's start
        func()              # runs the input function
        print('End')        # added to the input function's end
    return wrapper
"""
"""
# start_end_decorator for use with add5
def start_end_decorator(func):
    @functools.wraps(func)          # will perserve the information of our used function (Help part)
    def wrapper(*args, **kwargs):   # this syntax lets us use as many arguments and keyword arguments as we want
        print('Start')
        result = func(*args, **kwargs)       # || ABOVE COMMENT (allows application of arguments)
                                    # needed to also change the func to save the result and return it
        print('End')
        return result               # added to actually get result back for add5
    return wrapper

@start_end_decorator        # like "print_name = start_end_decorator(print_name)", this
                            # assigns the decorator to print_name, extending the function
def print_name():
    print('Alex')

#print_name = start_end_decorator(print_name)
    # the deco function can actually do this part with the @ symbol
    # this assigned decorator to function print_name
#print_name()                # prints "Start\nAlex\nEnd" fusing the decorator and the function

# When our function to be decorated has arguments

@start_end_decorator
def add5(x):
    return x+5

print()
#result = add5(10)       # typeerror: start_end_decorator.<locals>.wrapper() takes 0 positional arguments but 1 was given
                        # so wrapper needs a positional argument
#print(result)           # prints "Start\nEnd\nNone" - which we dont want
print(help(add5))       # python got confused about the identity of add5 now
                            # import functools, add under def start_end... and above def wrapper, above
print(add5.__name__)    # without print(help(add5)) prints Start\nEnd\nwrapper


# this file now is a template you can use for decorators:
def smy_decorator(func):
    @functools.wraps(func)              # decorator that takes an argument
    def wrapper(*args, **kwargs):       # inner function
        # Do...
        result = func(*args, **kwargs)  # 2 inner functions  - inner funct within an inner funct
        # Do...
        return result
    return wrapper



# more decorators using the above as template
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):           # args = arguments, kwargs = key arguments
            for _ in range(num_times):          # (underscore meaning the variable doesnt matter from a conventional standpoint)
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)    # I want the repeat decorater to repeat this function 3 times
def greet(name):
    print(f'Hello {name}')

greet('Alex')           # repeated 3 times

"""

# Nested Decorators
def start_end_decorator(func):
    @functools.wraps(func)          # will perserve the information of our used function (Help part)
    def wrapper(*args, **kwargs):   # this syntax lets us use as many arguments and keyword arguments as we want
        print('Start')
        result = func(*args, **kwargs)       # || ABOVE COMMENT (allows application of arguments)
                                    # needed to also change the func to save the result and return it
        print('End')
        return result               # added to actually get result back for add5
    return wrapper

def debug(func):    # extracs name, arguments, and keyw arguments,
    # then prints the info of this function, executes it, prints info about the return value
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]                     # extracting arguments and keyw arguments
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)          # extracting the name
        print(f"Calling {func.__name__}({signature})")          # prints the information of this function
        result = func(*args,**kwargs)                           # executes the function
        print(f"{func.__name__!r} returned {result!r}")         # prints info about the return value
        return result
    return wrapper
@debug                  # applying multiple decorators executes in the order they're listed (debug first)
@start_end_decorator    # executes after debug but before say_hello
def say_hello(name):    # executes last
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello('Alex')
    # Calling say_hello('Alex')
    # Start
    # Hello Alex
    # End
    # 'say_hello' returned 'Hello Alex'


# Continued in PythonDecorators_Class
