# Dictionaries: Key-Value pairs, unordered, mutable
# Creation
# default method, need quotes for keys
"""
mydict = {"name": "Max", "age" : "28", "city" : "New York"}
print(mydict)
# using a function, dont need key quotes
mydict2 = dict(name="Mary",age="27",city="Boston")
print(mydict2)
print()

#accessing values
value = mydict["name"]
print(value) # prints max
value = mydict["age"]
print(value)
value = mydict["city"]
print(value)
print()

#adding key value pairs
mydict["email"] = "max@xyz.com"
print(mydict)
mydict["email"] = "coolmax@xyz.com" # overwrites max@xyz.com
print(mydict)
print()

#deletion of value pairs
del mydict["name"] # normal style
print(mydict) # name is now gone, as well as Max
mydict.pop("age") # built in method style
print(mydict)
mydict.popitem() # removes last inserted item
print(mydict) # removed the email key value pair

# wanting to check if a key is in the dictionary
if "city" in mydict: #if/in, prints the New York since its in city
    print(mydict["city"])
else:
    print("Error")

try:    #try/except, prints error since name isnt in the dict
    print(mydict["name"])
except:
    print("Error")
"""

"""
# reestablishing the dictionary by re running it
mydict = {"name": "Max", "age" : "28", "city" : "New York"}
    #reestablishing my dict because of past exercises
print(mydict)

#looping through the dictionary
for key in mydict:          # prints the keys
    print(key)
print()

for key in mydict.keys():   # prints the keys;
                            # keys method returns a list with
                            # the keys inside it
    print(key)
print()

for value in mydict.values():   # prints the values
    print(value)
print()

for key,value in mydict.items(): # prints keys and values
    print(key,value)

# Copying dictionaries________________________________________________

# "copy" that points to the same place in memory, so more of a pointer
mydict_copy = mydict    # both dicts are the same dict in memory
print(mydict_copy)
mydict_copy["email"] = "max@xyz.com"
print(mydict_copy)  # same as mydict
print(mydict)       # same as mydict_copy

print()

# true copy:
mydict_copy = mydict.copy()    # copy() makes an actual copy
print(mydict_copy)
mydict_copy["email2"] = "max@xyz.com"
print(mydict_copy)  # has email2
print(mydict)       # no email2

print()

# another true copy
mydict_copy = dict(mydict)    # dict() function
print(mydict_copy)
mydict_copy["email2"] = "max@xyz.com"
print(mydict_copy)  # has email2
print(mydict)       # no email2

print()

# Merging Dictionaries
my_dict_1 = {"name": "Max", "age" : "28", "email" : "max@xyz.com"}  # only dict with email
my_dict_2 = dict(name="Mary",age="27",city="Boston")    # only dict with city
# they're different
my_dict_1.update(my_dict_2) # existing key/value pairs overwritten, new ones added as they are
print(my_dict_1) # Mary, 27, max@xyz.com, Boston
print(my_dict_2) # Mary, 27, Boston

print()

# You can use most things as a key
my_dict_3 = {3: 9, 6: 36, 9: 81}
print(my_dict_3)

#value = my_dict_3[47]      # nothing prints because 0 isnt a key,
                            # possibly should be an error but idc
#print(value)
value = my_dict_3[6]
print(value)
"""
# tuple as a key
mytuple = (8,7)
tupledict = {mytuple:15}    #since they're immutable, they can work
print(tupledict)
#mylist = {4,12}        #lists dont work for this b/c mutable
#listdict = {mylist:15}
#print(listdict)

