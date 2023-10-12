# Lambda function: small one line anonymous funct thats defined without a name
# syntax: lambda argument1: expression1

#normal functions look like this:
def add10_funct(x):
    return x+10

print("FUNCTION: ")
print(add10_funct(5))


print()


# lambdas (lambda functions) look like this
add10_lambda = lambda x: x+10  # creates a funct with one argument and adds 10 to it

print("LAMBDA: ")
print(add10_lambda(5)) # prints 15, as add10_lambda functions the same as the function
                        # add10_funct, which just adds 10 to x
                        # lambdas are nice because they're single-line

# now with 2 arguments
mult = lambda x,y: x*y #create the function with x and y as its arguments, multiplying them together
print(mult(2,7))


# lists
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D) # by default sorts by first argument, but we can also give a rule
points2D_sorted2 = sorted(points2D, key=lambda x: x[1]) # we use lambda to force it to sort by y value
        # ie. the lambda funct should take x, and find whatever is at index x, which is 'y' and return it
print(points2D)
print(points2D_sorted)
print(points2D_sorted2)

#points2D_sorted2 using a funct rather than a lambda
def sort_by_y(x):
    return x[1]
points2D_sorted3 = sorted(points2D, key=sort_by_y)
print(points2D_sorted3)     # all in all using functs for something like this is overcomplicated

# sorting according to the sum of each x and y added together
points2D_sorted4 = sorted(points2D, key=lambda x: x[0]+x[1]) # adding x and y together essentially
print(points2D_sorted4)     # prints [(1, 2), (5, -1), (10, 4), (15, 1)]
                            #           3       4         14       16

# map function:
# map(func, seq): (function, list) transforms each element with a function
a = [1,2,3,4,5]
b = map(lambda x: x*2, a) # multiplying each element in a by 2
print(list(b)) # prints [2, 4, 6, 8, 10]
#list comprehension syntax
c = [x*2 for x in a] # multiply x by 2 for each index content (x) in list a
print(c) # same outcome as map and a lot more comprehensive, but map is still a thing

# filter(funct,seq) function must have a true or false
d = filter(lambda x: x%2==0, a) # we only want evens; shows only elements from a that
                                # dont have a remainder when 2 goes into them
print(list(d))

#listcomp of above
e = [x for x in a if x%2==0] # output x for each x in list a, but only if x%2==0
print(e)    # same outcome, less words, for loops are strong in python

# reduce(funct,seq), repeatedly applies funct to elements and returns a single value
from functools import reduce
a = [1,2,3,4]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)
