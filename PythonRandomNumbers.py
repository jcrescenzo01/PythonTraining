# Random Numbers: Built in modules - random() secrets() nonpy
import random

a = random.random()     # random float in the range of 0 to 1
print(a)

b = random.uniform(1, 10)       # specific range using a start and stop, so from 1 to 10, float
print(b)

c = random.randint(1,10)        # integer randomized equal to / between the 2 numbers
print(c)

d = random.randrange(1,10)      # upper boundry (10) is NOT included, so its 1-9, never prints 10
print(d)

e = random.normalvariate(0,1)   # random value from a normal distribution with a mean of 0
                                # and standard deviation of 1
print(e)

# random comes with different functions to work with sequences
# random choice from a list of things
mylist = list("ABCDEFGH")
print(mylist)
f = random.choice(mylist)       # random.choice() chooses randomly from the input list
print(f)

# randomly selecting more elements, uniquely
g = random.sample(mylist, 3)    # picks unique elements, wont pick A twice, for example

# randomly selecting more elements, not uniquely
h = random.choices(mylist, k=3) #choice-->s<-- with the s at the end, this can pick the same thing many times

# Mixing up the elements in a list directly
random.shuffle(mylist)
print(mylist)


# using seed(), which makes the numbers the same each time by referencing a seed value
# seeds are REPRODUCABLE so on another computer 1 would do the same, so not for infosec
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))

print()
# because seeds are reproducable:
# secrets module: for security tokens, account authentication, etc
    # disadvantage is that secrets algorithms take more time
import secrets
i = secrets.randbelow(10)   # produces a random int from 0 to 10
print(i)

j = secrets.randbelow(4)    # returns an integer with k (4) random bits, ie 4
                                # different random binary values
print(j)                    # the highest possible number here is binary 1111, meaning 15
                                # binary work: (2^3=8)+(2^2=4)+(2^1=2)+(1)=8+4+2+1=15
                                # binary calculations like this are good to know
                            # in that regard, randbelow(4) is a random integer between
                                #  0 and 15

mylist = list("ABCDEFGH")
k = secrets.choice(mylist)  # choice picks a random choice that isn't reproducable
#1111
print(k)

#numpy module
import numpy as np


