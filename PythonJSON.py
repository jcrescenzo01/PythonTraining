# import JSON module
import json

# converting python dict to JSON format
# called Serializtion / Encoding
person = {"name": "John", "age": 30, "city": "New York", "hasChildren":False,
          "titles":["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
    # dumps will serialize objects to a JSON formatted string
    # indent 4 gives it a nicer format, the indent is in accord with {}s and []s rather than just in general
    # separators=('; ', '= ') would change the ": " and "," in the print, unsure what denotes which they replace though
        # use defaults instead
    # sort_keys sorts the keys of the dictionary by descending alphebetical order by default

#print(personJSON)
    # prints it in json format, seen by False becoming lowercase, which is JSON format

# you can also convert it / dump it into a file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4) # not dumps (dump-s) b/c not string

# deserialization, converting JSON back to an object in python
person2 = json.loads(personJSON) # loads=load from a stirng
print(person2) # gives us a python dict (false is uppercase now)

with open('person.json', 'r') as file: # opens the json file as read-only
    person3 = json.load(file) # loads person.json to person3
    print(person3) # comes out in python format successfully