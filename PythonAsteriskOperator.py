# Asterisk (*) in Python
# multiplication and power operations, args and kwargs, kw only params,
# creating lists or tuples with repeated elements
# unpacking lists, tuples, dicts into funct arguments,
# unpacking containers, and merging containers into a list,
# merging two dicts

# multiplication
result = 5*7
print(result)

# Powers
result = 2**4
print(result)

# Creating lists, tuples, strings with repeated elements
zeros = [0]*10      # ten zeros
print(zeros)
zeros = [0,1]*10    # ten zero ones, so 0,1,0,1...
print(zeros)
zeros = (0,1)*10    # tuples work too
print(zeros)
zeros = "AB" * 10   # string with 10x occurences of "AB"
print(zeros)

# function usage (function arguments) check that document
def foo(a,b,*args, **kwargs):
    print(a)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
foo(1,2,3,4,5,six=6,seven=7)
