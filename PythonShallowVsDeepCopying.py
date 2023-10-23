# Copying - copying mutable elements with Build and Copy,
# shallow vs deep, copies of custom objects

org1 = 5
cpy1 = org1   # cpy isnt a real copy, its a new variable with the same reference
            # both variables point to the same number
cpy1 = 6
print(cpy1)
print(org1)
print()


# when we deal with mutable types, we have to be careful with this:
org2 = [0,1,2,3,4]
cpy2 = org2     # this assignement (=) operator doesnt make a real
                # copy, it references the same address org2 does and
                # so it will change the same information: see below!
cpy2[0] = -10
print(org2)     # note that org2[0] changed when cpy2[0] did! see above!
print(cpy2)
print()


# Shallow and Deep Copies
#   Shallow - one level deep, only references of nested child objects
#   Deep - full independent copy

import copy

# Shallow copy
# Method 1
org3 = [0,1,2,3,4]
cpy3 = copy.copy(org3)
cpy3[0] = -10
print(org3)     # org3 isnt effected by the change to cpy3[0]
print(cpy3)
print()
# Method 2
org4 = [0,1,2,3,4]
cpy4 = org4.copy()  # .copy() method
cpy4[0] = -7
print(org4)     # org3 isnt effected by the change to cpy3[0]
print(cpy4)
print()
# Method 3
org5 = [0,1,2,3,4]
cpy5 = list(org5)   # using list function
cpy5[0] = -33
print(org5)     # org3 isnt effected by the change to cpy3[0]
print(cpy5)
print()
# Method 4
org6 = [0,1,2,3,4]
cpy6 = org6[:]  # using list slicing
cpy6[0] = -70
print(org6)
print(cpy6)
print()

# Shallow Copy with Nested List - doesnt work!
org7 = [[0,1,2,3,4], [5,6,7,8,9]]
cpy7 = copy.copy(org7)
cpy7[0][1] = -9     # changing second element of first list
print(org7)     # org7 changed! Thats because Shadllow Copies are
                # only one level deep!
print(cpy7)
print()

# Deep Copying to work with Nested List
org7 = [[0,1,2,3,4], [5,6,7,8,9]]
cpy7 = copy.deepcopy(org7)  # deep copy done with deepcopy()
cpy7[0][1] = -9
print(org7)
print(cpy7)
print()

