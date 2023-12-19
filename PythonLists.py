"""
myList = ["word1", "word2", "word3"]    #a list
print(myList)                           #prints the list with brackets

# list()
myList2 = list()                        #premaking a list
print(myList2)                          #nothing in it but prints as brackets
"""

"""
# Lists can contain different value types
myList3 = [5, True, "apple", "Oh yeah! \n lets do it!"] #diff value types
print(myList3)                          #note \n actually prints
print(myList3[3])

item = myList3[2]
print(item)

if 5 != 2:
    myList3[1] = False
print(myList3[1])


# length function works
print(len(myList3))

# appending to a list
myList3.append("lemon")     #
print(myList3)              # lemon added to end

# removing items with pop method
a = myList3.pop()
print(a)                # returns lemon, which was taken out
print(myList3)          # returns list, but lemon has been taken out

# removing a specific element
b = myList3.remove(5)   # removing 5 from myList3
print(myList3)          # 5 is gone

c = myList3.insert(1, "blueberry")  # Insert puts blueberry at whatever index given (1 in this case)
print(myList3)
"""


# sorting a list
myList4 = [45, 2, 16, 3002, 8, 8, 98, 18, 12]
print(myList4)
myList4.sort()                      # sorts the list
print(myList4)                      # printing sorted list
# putting a sorted version of a list in a new list
print("\n")
myList5 = [45, 2, 16, 3002, 8, 8, 98, 18, 12]
print(myList5)
myList5_sorted = sorted(myList5)
print(myList5_sorted)

# create lists with same operator many times
myList6 = [0] * 5       # makes 0 at 5 indices, 0-4
print(myList6)

# mixing two lists together at their ends
myList7 = [1, 2, 3, 4, 5]
print(myList7)

myList_6_7 = myList6 + myList7  # 6 attached to 7 right->left
print(myList_6_7)


"""
# selecting what indexes / a range / skipping indexes
myList8 = [1,2,3,4,5,6,7,8,9]
print(myList8)
a = myList8[1:5]   #if you dont specify the nums it goes to either end
print(a)

print("\nColons with Indexes")
print(myList8[:4]) #start from the starting index to but not at 4
print(myList8[4:]) #start from index 4 to the end

print("\nStepping with list")
print(myList8[::2])     #begin to end skipping every 2 varis
print(myList8[2::4])    #start at 2 to the end, skipping 4 varis
print(myList8[1:8:2])   #start at i1 to i8, skipping every second
print(myList8[0:8:2])   #start at i0 to i8, skipping every second
print(myList8[:8:2])    #start at i0 to i8, skipping every second
print(myList8[2::9])    #start at i3 to end, skipping 9
"""

"""
# making a copy of a list that represents it, almost like a pointer
list_org = ["banana", "cherry", "apple"]    # main list
list_copy = list_org                         # copy of list
print(list_copy)
list_copy.append("lemon")
print(list_copy, "\n", list_org)              # appended to both!
                                        # both lists refer to same list's address
print("\n")
# Making a non-original-effecting, actual copy of a list
list_copy2 = list_org.copy()            # use copy method
list_copy2.append("watermelon")
print(list_copy2, "\n", list_org)       # watermelon only appended to list_copy2

# another copy option that doesnt effect the original:
list_copy3 = list_org[:]
list_copy3.append("peach")
print(list_copy3, "\n", list_org)       # peach only in copy3
"""

"""
# List Comprehension - elegent way to create new list from existing list
numList = [1,2,3,4,5,6]
numList2 = [i*i for i in numList] #list to square each element of numList
    # copied using a for loop
print(numList, "\n", numList2)
"""

