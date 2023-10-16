import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 27)  # created a User named Max who is 27

# converting to json
#userJSON = json.dumps(user)   # error, object of type user isnt
                                    # json serializable
                                # so we need a custom encoding
                                    # function!

def encode_user(o):
    if isinstance(o, User):     # return whether obj is an instance of a class
        return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
            # making the class name as a key at the end there is a useful
            # trick to
    else:
        raise TypeError('Object of type User is not JSON serializable')

#userJSON = json.dumps(user, default=encode_user)
#print(userJSON) # we get a dict with the name, age, and User class key - that with value true

# second way is to use a custom json encoder
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User): # is instance returns whether an object is a class / subclass of one
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

#userJSON = json.dumps(user, cls=UserEncoder) # then you can run UserEncoder through "cls=" in dumps()
#print(userJSON)

#alternatively:
userJSON = UserEncoder().encode(user)
print(type(userJSON))   # str type
print(userJSON)

print()

#switching to python object
user = json.loads(userJSON)
print(type(user))       # dict type
print(user)
# note that we cant do something like "user.name" because it isnt a User, its a dict now

# if we want to decode it into a user object, we need a custom decoding object
def decode_user(dct):   # takes a dictionary
    if User.__name__ in dct:    #
        return User(name=dct['name'], age=dct['age'])
    return dct
user = json.loads(userJSON, object_hook=decode_user)
print(user.name) # now it successfully prints "Max" using user.name


