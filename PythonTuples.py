

# Tuples are collection data types that are ordered and
# IMMUTABLE,meaning it cant be changed

# Creation: with either parenthesis or blank
# Parenthesis Style
myTuple = ("Max", 28, "Boston") #created with parenthesis
print(myTuple)
print(type(myTuple))
# Blank Style
myTuple = "Max", 28, "Boston" #created with blank
print(myTuple)
print(type(myTuple))

myTuple2 = ("Jon")  # apparently a string, the parenthesis dont stop this
print(myTuple2)
print(type(myTuple2))
myTuple2 = ("Jon",) # comma makes it tuple rather than string
print(myTuple2)
print(type(myTuple2))

# accessing elements of a tuple
item = myTuple[0]
print("\nMyTuple index 0 is: \n" + item + "\n")
# changing elements isnt possible
# myTuple[0] = "Tim" # fails because TUPLES ARE IMMUTABLE

# Iteration over a tuple
for i in myTuple:
    print(i)

print("\n")

# finding something in a tuple
if "Max" in myTuple:
    print("Yes")
else:
    print("No")

# useful tupple methods
my_tuple = ("a", "p", "p", "l", "e")
print(len(my_tuple))        # 5 letters in apple
print(my_tuple.count('p'))  # returns 2 becuase there are 2 letter p
print(my_tuple.index('l'))  # returns the first index of one of the tuple's values
my_list = list(my_tuple)    # makes a list out of the tuple
print(my_list)
my_tuple2 = tuple(my_list)  # makes a tuple out of a list
print(my_tuple2)

# slicing with a tuple
a = (1,2,3,4,5,6,7,8,9,10)
print(a)
b=a[2:5]    # works as these ratios / steps normally do
print(b)
c=a[1::2]
print(c)    # prints every other number from i1, which is 2, so 2,4,6,8,10

# Unpacking - puting tuples into singular elements
name, age, city = myTuple   # assigns tuple values to each vari, but
                            # must be the same amount of variables
print("\n" + name)
print(age)
print(city + "\n")

# unpack multiple elements with one vari using *
my_num_tuple = (0,1,2,3,4)
i1,*i2, i3 = my_num_tuple   # the asterisk placed everything between 0 and 4 into it
print(i1)
print(i3)
print(i2)   # a list containing 1,2,3 due to asterisk
print()

# Efficiency: since tuples are immutable, python has things
# that can make them more efficient
import sys
my_list_1 = [0,1,2,"hello",True]
my_tuple_1 = (0,1,2,"hello",True)
print(sys.getsizeof(my_list_1), "bytes")    # 120 Bytes
print(sys.getsizeof(my_tuple_1), "bytes")   # 80 Bytes
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))  # 0.22s
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))  # 0.04s
