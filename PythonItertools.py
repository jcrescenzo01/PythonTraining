# Itertools module is collection of tools for handling iterators
# iterators are used in for loops, the most common being the list
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b) # prod is an iterator
print(list(prod)) # product will combi8ne 1,3 1,4 2,3 2,4 3 dimensionally

# repeat
b = [3] # so it isnt too big
prod = product(a,b, repeat=2) # repeat will define a number of repetitions
    # basically iterates it deeper, now organizing more possible unique iterations based on
    # combinations of 2 copies of the iterator rather than 1, now (1,3,1,3)(1,3,2,3)(2,3,1,3)(2,3,2,3)
print(list(prod))

# Permutations
from itertools import permutations
a = [1,2,3]
perm = permutations(a) # differnt orderings of the numbers in a / every permutation of them
print(list(perm))

# Combinations
from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2) # every combination of the 4 numbers, meaning no repetitions
print(list(comb))
comb = combinations_with_replacement(a,2) # allows for repetitions
print(list(comb))

# Accumulations, for accumulating things together as they go up a list
from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a) # acc is an accumulation of list a
print(a)            # 1, 2, 3, 4
print(list(acc))    # 1, 1+2=3, 3+3=6, 6+4=10
# Accumulation: Multiplying the elements
import operator
a = [1,2,3,4]
acc = accumulate(a, func=operator.mul) # acc is an accumulation of list a
print(a)            # 1, 2, 3, 4
print(list(acc))    # 1, 1*2=2, 2*3=6, 6*4=24
# Accumulation: Max
a = [1,2,5,3,4]
acc = accumulate(a, func=max) # acc is an accumulation of list a
print(a)            # 1, 2, 3, 4
print(list(acc))    # 1, 2 b/c max, 3 b/c max, 3 isnt max so still 5, 4 isnt so still 5
                    # prints "1,2,5,5,5" with 5 overtaking 3 and 4

# Group By: makes an iterator that returns keys and groups from an iterable
from itertools import groupby
def smallerthan3(x):   # function to test whether x is less than 3 or not
    return x < 3
a = [1,2,3,4] # list to be grouped
groupobj = groupby(a, key=smallerthan3) # group a by whether the numbers are less than 3
                                        # so [1,2] and [3,4]
print(groupobj)
for key, value in groupobj:
    print(key, list(value))

# Group By a lambda rather than a function
a = [1,2,3,4]
groupobj = groupby(a, key=lambda x: x<3) # lambda type functions are more concise for this
print(groupobj)
for key, value in groupobj:
    print(key, list(value)) # same output as earlier


# Another example of Group By
persons = [{'name': 'Tim', 'age': 25},{'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27},{'name': 'Clair', 'age': 28}]
                # persons is a list of dictionaries containing name and age
groupobj = groupby(persons, key=lambda x: x['age']) # group persons by the age key and similarities thereof
for key, value in groupobj:
    print(key, list(value)) # organized into 3 lines, tim and dan together b/c they're the same age

print()

# Infinite Iterators
# count funct
from itertools import count, cycle, repeat
for i in count(10):
    print(i)        # an infinite loop starting at 10 and incrementing by 1 for each repetition
    if i == 15:     # now it goes to 15 and breaks
        break
# cycle funct
a = [1,2,3]
for i in cycle(a): #continually loops back to the start, meaning 123123123123123 with a \n betw e/ number
    print(i)
    if i==3:    # just to stop it, # out if needed
        break   # just to stop it, # out if needed

# repeat
print()
for i in repeat(1, 4): # repeat 1, do it 4 times
    print(i) # prints 1, 4 times on a new line each time



