# escape character for apostrophes
mystring1 = "I\'m a Programmer" # escape character "\" to write the "'" char
print(mystring1)

# triple quote manipulation
mystring2 = """Hello \
World"""                        # the escape character makes the triple quote stay as one line
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
