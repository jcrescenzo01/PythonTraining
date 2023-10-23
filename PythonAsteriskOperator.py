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

print()

#with lists
def foo(a,b,c):
    print(a,b,c)
mylist = [0,1,2]
foo(*mylist) # prints the list / tuple after unpacking elements into a b c
mydict = {'a':1,'b':2,'c':3}
foo(**mydict)

print()

#unpacking multiple items into a list
numbers = [1,2,3,4,5,6]
*begining, last = numbers   # all elements except the last one go into a list
                            # always unpacks elements into a list
print(begining)
print(last)

print()

begining, *last = numbers   # all elements packed into last except first element
print(begining)
print(last)

print()

begining, *middle, last = numbers   # all elements packed into middle except first and last elements
print(begining)
print(middle)
print(last)
print()

mytuple1 = (1,2,3)
mylist1 = [4,5,6]
newlist1 = [*mytuple1, *mylist1]     # new merged list [1,2,3,4,5,6]
print(newlist1)
print()

#binding dicts together
dicta = {'a': 1,'b': 2}
dictb = {'c': 3,'d': 4}
dict_ab = {**dicta, **dictb}
print(dict_ab)
