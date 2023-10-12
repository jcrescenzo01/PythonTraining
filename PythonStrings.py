"""
# escape character for apostrophes
mystring1 = "I\'m a Programmer" # escape character "\" to write the "'" char
print(mystring1)

# triple quote manipulation
mystring2 = """ """Hello \
World""" """                       # the escape character makes the triple quote stay as one line
print(mystring2)

# access characters / substrings
mystring3 = "Hello World"
char0 = mystring3[0]
print(char0) # prints the 'H' in "Hello World"
#mystring3[0] = 'h' #changing H to h, but strings are immutable so error
substring = mystring3[1:5] # takes a range from mystring3, i1 to but not at i5
print(substring)    # we get ello
# yadayadayada we can step and all that good stuff:
substring2 = mystring3[::2]
print(substring2)   # prints HloWrd
# new thing with that though: -1 will reverse the string
substring3 = mystring3[::-1]
print(substring3)   # prints "dlroW olleH"

# variables in strings
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

# iterate through string with for loop
for i in greeting:
    print(i)        # vertically prints hello, each char induvidually

# check for character or substring! so that e could be ell and would work
if 'e' in greeting:
    print('yes')
else:
    print('no')

# strip to remove whitespace
mystring4 = "     Hello World       "
print(mystring4)    # prints the white space
mystring4 = mystring4.strip()   # tells mystring4 to not have white sspace at ends
print(mystring4)    # prints without white space other than space in middle

# this method doesnt change our string though, since its immutable
mystring5 = "     wow oh boy       "
print("\n"+mystring5)   # changed nothing yet
mystring5.strip()
print(mystring5)        # no change to mystring5 since its immutable
mystring5 = mystring5.strip()
print(mystring5)        # reassignment does work since that effects even the immutable

# string functions
mystring6 = "Hello World"
print(mystring6.upper())                    # make all uppercase
print(mystring6.lower())                    # make all lowercase
    # I see these 2 being used to make sure user input comes out right
print(mystring6.startswith("Hello"))        # does mystring6 start with Hello?
print(mystring6.find('o'))                  # what index is 'o' at?
print(mystring6.count('o'))                 # how many 'o's in mystring6
print(mystring6.replace('World', 'Bud'))    # replaces "World" with "Bud"

# string and lists, functs continued
mystring7 = 'how are you doing?'
mylist7 = mystring7.split() # splits string by reading spaces as delimiter
print(mylist7) # ['how', 'are', 'you', 'doing?']

mystring7 = 'how,are,you,doing?'
mylist7 = mystring7.split(",") # splits string by reading commas as delimiter
print(mylist7) # ['how', 'are', 'you', 'doing?']
newstring7 = ''.join(mylist7)
    # joins together elements of mylist7 into a string, using the string as the space between
print(newstring7) # back to being a string: howareyoudoing? due to there being no entry for string
newstring7 = ' '.join(mylist7) # added a space
print(newstring7)
    # .join is really useful for joining elements of a string back together from a list

mylist8 = ['a'] * 6 # mylist8 will have 6 'a's at its indices
print(mylist8)

#time module to track the below two attempts:
from timeit import default_timer as timer
# now we want to join them, this is the bad version:
start = timer()     # TIMER - BAD
mystring8 = ''
for i in mylist8:
    mystring8 += i # bad because, since strings are immutable, this operation will
                    # create a new string here and assign it
                    # back to our original string, which is "costly"
print(mystring8)
stop = timer()      # TIMER - BAD
print(stop-start)   # TIMER - BAD 2ms

#good version
start2 = timer()     # TIMER - GOOD
mystring8 = ''.join(mylist8) # faster and cleaner
print(mystring8)
stop2 = timer()      # TIMER - GOOD
print(stop2-start2)   # TIMER - GOOD
# theyre basically interchangeble in timing, but if we up the list amount:

print()

# SECOND TIME TEST
# no printing because 1m elements would be a lot
mylist8 = ['a'] * 1000000 # mylist8 will have 6 'a's at its indices
from timeit import default_timer as timer

# BAD
start = timer()     # TIMER - BAD
mystring8 = ''
for i in mylist8:
    mystring8 += i
stop = timer()      # TIMER - BAD
print(stop-start)   # TIMER - BAD 2ms

# GOOD
start2 = timer()     # TIMER - GOOD
mystring8 = ''.join(mylist8)
stop2 = timer()      # TIMER - GOOD
print(stop2-start2)   # TIMER - GOOD
# now you can see that its no longer close - joining is generally better
# .join() is better for fusing lists into strings!

"""

# String Formatting
# a few ways:
# % operator
# .format() method
# f-Strings

# %____________________________________________________________________
var = "Tom"
mystring9 = "the variable is %s" % var
    # %s = placeholder for a string, that string being var due to "% var"
print(mystring9) # prints: the variable is Tom

var = 10
mystring9 = "the variable is %d" % var
    # %d = placeholder for a decimal
print(mystring9) # prints: the variable is 10

var = 10.893
mystring9 = "the variable is %f" % var
    # %f = placeholder for a float
print(mystring9) # prints: the variable is 10.893000, as floats are 6 digits as default

# float %, but with chosen decimal length
var = 10.893
mystring9 = "the variable is %.2f" % var
    # %f = placeholder for a float, but the .2 makes it 2 points after
print(mystring9) # prints: the variable is 10.89 due to %.2f rather than just %f

# .format()______________________________________________________________
# NEW FORMATING STYLE: float %, but with chosen decimal length
var = 10.893812417
mystring9 = "the variable is {}".format(var) # {} rather than %dataType
    # also, float doesnt default to 6 decimal spaces(?)
print(mystring9)
# decimal place manipulation in NEW FORMAT
var = 10.893812417
mystring9 = "the variable is {:.2f}".format(var) # :.2f = %.2f basically
    # also, float doesnt default to 6 decimal spaces(?)
print(mystring9)

var = 10.893812417
var2 = 47.8933
mystring9 = "the variable is {:.2f} and {}".format(var, var2)
    # added anoter variable to be formated, in the same function call
print(mystring9)

# NEW-EST FORMAT METHOD
var = 10.893812417
var2 = 47.8933
mystring9 = f"the variable is {var*2} and {var2}"
    # the f goes before the string, then you put the variables
    # into it directly, wayyyyy easier
print(mystring9)