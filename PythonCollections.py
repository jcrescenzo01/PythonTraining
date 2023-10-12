# Collections: Counter, namedTuple, OrderedDict, defaultdict, deque
# gives alternatives to other dattypes, usually lists and such

from collections import Counter
# container that stores elements as dictionary keys
# and their counts as dict values
a = "aaaaabbbbccc"
mycounter = Counter(a) # makes count of each element with its count
print(mycounter) # Counter({'a': 5, 'b': 4, 'c': 3})
print(mycounter.keys()) # only the keys
print(mycounter.values()) # only the values
print(mycounter.most_common(2)) # finds the most common element(s)
                                # the number indicates the top amount
                                # of elements you want to see, 1 in
                                # this case showing just 'a'
                                # returns a list
print(mycounter.most_common(1)[0][0])
    # want to see what is the most common element, and only the element
    # number 1 most common, access index 0 for the tuple that's there,
    # then access the first element of said tuple with another index 0
print(list(mycounter.elements())) # prints all assoc elements, needs to
                                # be made into a list to print right

print()

# named tuples
from collections import namedtuple
Point = namedtuple('Point', 'x,y') # creates class called Point with fields x and y
pt = Point(1, -4)
print(pt)
print(pt.y)

print()
# Ordered Dictionary, normal dict but they remember the order that items were inserted
# less important now due to dictionary class able to remember order anyway
from collections import OrderedDict
ordereddict = OrderedDict()
ordereddict['a'] = 1
ordereddict['b'] = 2
ordereddict['c'] = 3
ordereddict['d'] = 4
print(ordereddict)
# but again, a normal dict works:
ordereddict = {}
ordereddict['a'] = 1
ordereddict['b'] = 2
ordereddict['c'] = 3
ordereddict['d'] = 4
print(ordereddict)

# Default Dictionary, similar to normal dictionary container
# but has a default value if the key hasnt been set yet
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c']) # returns the default value of an int, which is 0
                # works with lists, etc
                # normal dict would return an KeyValue error

# Deque, double ended queue, add or remove elements from both ends
# both are implemented to be efficient
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)     # 3 is added on the left
print(d)            # prints "deque([3, 1, 2])"
d.pop()             # pop rids us of the rightmost value
print(d)            # prints "deque([3, 1])"
d.popleft()         # popleft does the opposite of pop
print(d)            # prints "deque([1])"
d.extend([4,5])     # adds all elements to right side of d
d.extendleft([1,2]) # adds all elements to left side of d
    # adds them left to right, stacking, so becomes:
print(d)            # prints "deque([2, 1, 1, 4, 5])"
d.rotate(1)         # everything rotates 1 to the right like a circle
print(d)            # each value moved to the right, 5 going back to start
                    # prints "deque([5, 2, 1, 1, 4])"
d.rotate(-2)        # rotates to the left twice
print(d)

