
# Errors and Exceptions
#a = 5 print(a) # gives us a syntax error because print should be on a \n
#a=5
#print(a)) # syntax error extra parenthesis
#a=5+'10' # type error cant add int to str
#import thisModule # module error since it doesnt exist
#a=5
#b=c # name error since c doesnt exist
#f=open('somefile.txt')  # file not found error

#a = [1,2,3]
#a.remove(4) # value error since 4 isnt in a
#a[4] # index error since 4 is out of range
#print(a)

#mydict = {'name': 'Max'}
#mydict['age'] # key error since 'age' isnt in mydict as a key

# raise Exception is used to force an Exception to occur when a
# condition is met
"""
x = -5
if x < 0:
    raise Exception('x should be positive') # prints in red
"""

# AssertionError takes away the if statement
"""
x = -5
assert(x>=0), 'x is not positive' # prints error and
            # "AssertionError: x is not positiveAssertionError: x is not positive"
"""

"""
# try and try-except blocks
try:
    a=5/0
except:
    print('an error has occurred') # program continues instead of stopping like with raising exceptions

try:
    a=5/0
except Exception as e: # exception is the base class for all exceptions
    print(e) # prints the division by zero message from the ZeroDivisionError class
             # essentially, we specified the exception for the compiler to put out
try:
    a=5/0
except ZeroDivisionError as e: # specifically checking for ZDE rather than general exceptions
    print(e) # prints the same as the above, but we knew the error to put in and check for

print()

# Catching multiple exceptions
try:
    a=5/1
    #b=a+'10' #TypeError catches this
    b=a+4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("everything is fine!")
finally: # runs always regardless of an exception for cleanup operations
    print('cleaning up...')
"""

# Defining our own exceptions / defining our own error classes by taking from base Exception clss
class ValueTooHighError(Exception): # error classes should have "Error" as their title-end
                                    # Exception in the class title is the "Base Class" for ValueTooHighError
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x>100:
        raise ValueTooHighError('value is too high') # raises as an error
    if x<5:
        raise ValueTooSmallError('value is too small:', x)
try:
    test_value(3)
except ValueTooHighError as e:
    print(e) # prints instead of raising the error so code can continue
except ValueTooSmallError as e:
    print(e.message, e.value) # better than ValueTooHighError since now we get the value sent to inform the user

