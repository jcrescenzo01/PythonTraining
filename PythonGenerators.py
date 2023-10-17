# Generators
# functions that return an object that can be iterated over
# generates items in object lazily, so one at a time and only when you ask
# very memory efficient
# use the "yield" keyword instead of "return"

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
#for i in g:
#    print(i)        # prints 1\n2\n3\n

"""
value = next(g)
print(value)        # 1
value = next(g)
print(value)        # 2
value = next(g)
print(value)        # 3
#value = next(g)
#print(value)       # mygenerator() g raises a stop iteration
                    # because it didnt reach another yield statement
"""
#print(sum(g))       # calculates the current place of yields going forward
                    # 1 + 2 + 3
                    # if the above value=next(g) up to 3 are there, it will
                    # add nothing together, making 0

def mygenerator1():
    yield 3
    yield 1
    yield 2
g1 = mygenerator1()
print(sorted(g))            # list with all the objects in a sorted
                            # order, printed "[1, 2, 3]"

print()
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4) # doesnt print starting even
value = next(cd)
print(value)        # 4
print(next(cd))     # 3
print(next(cd))     # 2
print(next(cd))     # 1
#print(next(cd))    # stopiteration error

print()
# Memory saving with large data

# this func will be inefficient using the method you'd normally use for its purpose:
def firstn(n):      # returns numbers in a sequence from 0 to n
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num+=1
    return nums
                    # all of the associated numbers are stored in the
                    # list, which is taxing on memory
# heres the generator version; more efficient:
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

import sys
myList = firstn(1000)
print(myList)
print(sum(myList))
print(sys.getsizeof(myList))        #8856 for sizeof

print()
myList_gen = firstn_generator(1000)
print(myList_gen)
print(sum(myList_gen))
print(sys.getsizeof(myList_gen))    #104 for sizeof - way smaller and more efficient


# fibonacci sequence generator
def fibonacci(limit):
    # 0 1 1 2 3 5 8 13... - thats the fibonacci sequence
    a, b = 0, 1
    while a < limit:
        yield a         # 
        a, b = b, a+b   # a is b, b is a+b as increment in the fibseq

fib = fibonacci(30)
for i in fib:
    print(i)

print()

# Implementing a Generator Expression
mygenerator2 = (i for i in range(1000) if i % 2 == 0)
    # puts all even elements from 0-9 in our generator
"""
# iterating through mygenerator2
for i in mygenerator2:
    print(i)
"""
print()

# List Comprehension
# normally
mylist1 = [i for i in range(1000) if i % 2 == 0]
print(mylist1)
print(sys.getsizeof(mylist1))   # very big

# using a generator working off mygenerator2
print(list(mygenerator2))   # also does the trick using mygenerator2 above
                            # took mygenerator2 and turned it into a list
print(sys.getsizeof(mygenerator2)) # small