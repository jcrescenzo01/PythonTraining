# Sets: unordered, mutable, no duplicates
"""
myset1 = {1,2,3}
print(myset1)

# No duplicates allowed
myset2 = {1,2,3,1,2}    # the 1 and 2 at the end are ignored due to
                        # only 1 of each thing being allowed
print(myset2)

# Sets are unordered, arbitrary - it ignores your petty order
myset3 = set("Hello")
print(myset3)       # prints {'l', 'e', 'o', 'H'}
                    # got rid of an l and through it into dissaray

print()

# set() function
myset4 = set()      # empty set
myset4.add(1)       # adds 1 to the set
myset4.add(2)
myset4.add(3)
myset4.add(4)
myset4.discard(4)   # gets rid of 4 in the set
print(myset4)       # {1, 2, 3}

myset4.clear()      # clears the set entirely
myset4.add(8)
myset4.add(9)
print(myset4)       # now {8, 9}

print(myset4.pop())  # pop returns the thin its getting rid of, then does so
print(myset4)

print()
myset4.clear()
myset4.add(1)
myset4.add(2)
myset4.add(3)
for i in myset4:    # can loop through the set with for loop
    print(i)

print()
if 1 in myset4:
    print("yes")
"""

# Union and Intesection in Sets
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

#union
u = odds.union(evens)
print(u)    # both sets combined without duplication
            # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#intersection
i = odds.intersection(evens)
print(i)    # no print because no similarities
i = odds.intersection(primes)
print(i)    # {3, 5, 7} printed, as the 3 numbers are in both sets

#difference
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
#method1
diff = setA.difference(setB)    # take the numbers that are different
                                # in setA compared to setB
print(diff) # {4, 5, 6, 7, 8, 9}
diff = setB.difference(setA)    # take the numbers that are different
                                # in setB compared to setA
print(diff) # {4, 5, 6, 7, 8, 9}

#method2
diff = setB.symmetric_difference(setA)  # symetric difference will
                                        # show all differences between
                                        # both sets
print(diff) # {4, 5, 6, 7, 8, 9, 10, 11, 12}
diff = setA.symmetric_difference(setB)  # same as above
print(diff) # {4, 5, 6, 7, 8, 9, 10, 11, 12}

print()

#Modification via update
#setA.update(setB) # adds the different elements found in the other set
print(setA)
#Intersection Update
#setA.intersection_update(setB) # keeps only the elements found in both sets
print(setA)
#Difference Update
#setA.difference_update(setB) # keeps only the differences
print(setA)
#Symetric Difference Update
setA.symmetric_difference_update(setB)  # keeps only the elements in setA or setB
                                        # but not that are in both
print(setA)

#boolean functions
setC = {1,2,3,4,5,6}
setD = {1,2,3}
setE = {7,8}
print(setC.issubset(setD))  # returns false, as a subset is all the elements
                            # of setC are also in setD, which they are not
print(setD.issuperset(setC))    # returns true if first set contains all numbers from second set
                                # returns false since 4,5,6 arent in setD
print(setC.isdisjoint(setD))    # returns false because they have similar elements
print(setC.isdisjoint(setE))    # returns true because 7 and 8 are not in setC, ie it is disjointed

# Copying
#setC=setD #will copy but send to the same address, so not a copy but a pointer in theory
#print(setC)
#print(setD)
# Actually Copying
setD=setC.copy()
setD.add(7)
print(setC)
print(setD) #only has the 7 because we didnt do just setD=setC, the .copy() method saved it, as usual
# Actually Copying other method
setD = set(setC)
setD.add(7)
print(setC)
print(setD) #works the same, different methodology

# Frozen Sets
a = frozenset({1,2,3,4}) # cant change after creation
#a.remove(1) #causes error
#print(a)

