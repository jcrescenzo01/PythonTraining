import functools
# Class decorators
# do the same thing as funct decorators, but they are typically used
# if you want to maintain and update a state

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0      # we also create a state to track
                                # how many times this has been executed
    # we need to also implement the call method
    def __call__(self, *args, **kwargs):    # allows us to execute an object of this class just like a function
        self.num_calls += 1     # increment
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

"""
# with def __call__ in CountCalls as:
    def __call__(self, *args, **kwargs):    # allows us to execute an object of this class just like a function
        print('Hi there')
cc = CountCalls(None)
cc()                 # runs it like a function, cc print "Hi there"
"""


@CountCalls
def say_hello():
    print('Hello')

say_hello()     # prints: This is executed 1 times\nHello
say_hello()     # prints: This is executed 2 times\nHello
                # with this we can keep track of how many times this has executed

# Conclusion: Use Cases of decorators
    # timer for execution time
    # debug for more information on a function
    # check to check if arguments fullfill certain requirements
    # cacheing, updating state / info, etc etc etc
    # many uses