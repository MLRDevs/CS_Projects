# Alex Miller 6-Manipulating Strings

print("That is Alice's cat") # can use single or double quotes, if you use double, you can print a single one

print()
# escape characters

print('Say hi to Bob\'s mother') # allows a single quote
# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (break)
# \\ Backslash
print()
print("Hello there! \nHow are you? \nI\' m doing well!") # space after the escape character, prints the space

print()

# Raw Strings

print(r"That is Carol\'s cat") # ignores escape characters, can help with typing in a file path (C:\Users\Miller\Documents)

print()

# Multiple Strings with Triple Quotes

# anything inside the triple quotes are considered part of the string, indentation is not needed, prints all space and everything
print('''Dear Alice,


Eve's cat has been arrested for catnapping, cat burglary, and extortion


Sincerly,
Bob''') # the single quote in "Eve's" doesn't need to be escaped

print()

# Multiline Comments

"""

this is a comment
yet looks like a string


"""

# Indexing and Slicing Strings

spam = 'Hello, World!'
print(spam[0]) # indexing and slicing like lists also work with strings
print(spam[-1]) # in a slice, the starting index is included and the end index is not
print(spam[0:5]) # 0-4 indexs -> 'Hello'
print(spam[:5]) # start to 4 -> 'Hello'
print(spam[7:]) # 7th index to the end

print()

fizz = spam[0:5] # can set splices to different variables
print(fizz)

print()

# The 'in' and 'not in' Operators with Strings
# tests if the exact string (case sensative) is in the other string

print('Hello' in 'Hello, World!') # True
print('Hello' in 'Hello') # True
print('HELLO' in 'Hello, World!') # False
print('' in spam) # True
print('cats' not in 'cats and dogs') # False

print()

# Putting Strings Inside of Other Strings

name = 'Al'
age = 42
print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old') # noramal way of doing it 

#this new way doesn't use 'str()' and just use '%s' wherever a variable needs to be used and then set what variable in the right order
print('Hello, my name is %s and I am %s years old' %(name, age)) # string interpolation

# this way uses the 'f-strings'
print(f'Hello, my name is {name} and I am {age} years old')

print()

# Useful String Methods, upper(), lower(), isupper(), islower()

# these methods do not change the string but return the new one, thats why it gets assigned back to 'spam'
spam = 'hello'
spam = spam.upper() # makes the string all upper case
print(spam)

spam = 'HELLO'
spam = spam.lower() # makes the string all lower case
print(spam)

print()

# will return true if there is at least one letter, and is all uppercase, otherwise false
spam = 'Hello'
print(spam.islower()) # False
print(spam.isupper()) # False
print('HELLO'.isupper()) # True
print('abc12345'.islower()) # True
print('12345'.isupper()) # False
print('12345'.islower()) # False

print()

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too')
else:
    print('I hope the rest of your day is good')

print()

print('HELLO'.lower().upper().lower().upper().islower()) # you can chain them together, this statement returns False

print()

# The isX() method, these methods also return booleans

# isalpha() returns True if the string consists of only letters and isn't blank
# isalnum() returns True if the string consists of only letters and numbers and isn't blank
# isdecimal() returns True if the string consists of only numberic characters and isn't blank
# isspace() returns True if the string consists of only spaces, tabs, and newlines and isn't blank
# istitle() returns True if the string consists of only words that begin with an uppercase letter followed by only lowercase letters

print('hello'.isalpha()) # True
print('hello123'.isalpha()) # False
print('hello123'.isalnum()) # True
print('hello'.isalnum()) # True
print('123'.isdecimal()) # True
print(' '.isspace()) # True
print('This Is Title Case'.istitle()) # True
print('This Is Title Case 123'.istitle()) # True
print('This Is not Title Case'.istitle()) # False
print('This Is NOT Title Case'.istitle()) # False

print()

while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Enter a number for your age')

while True:
    print('Enter a password (letters and numbers only)')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers')

print()

# the startswith() and endswith() methods

print('Hello, World!'.startswith('Hello')) # True
print('Hello, World!'.endswith('World!')) # True
print('abc123'.startswith('abcdef')) # False
print('Hello, World!'.startswith('Hello, World!')) # True
print('Hello, World!'.endswith('Hello, World!')) # True

print()

# The join() and split() methods
# join() takes a list and makes it into a string
# split() takes a string and makes it into a list

print(', '.join(['cats', 'bats', 'rats'])) # cats, bats, rats
print(' '.join(['My', 'name', 'is', 'Alex'])) # My name is Alex
print('ABC'.join(['My', 'name', 'is', 'Alex'])) # MyABCnameABCisABcAlex

print()

print('My name is Alex'.split()) # ['My', 'name', 'is', 'Alex'] by default, splits wherever there is whitespace
print('MyABCnameABCisABCAlex'.split('ABC')) # ['My', 'name', 'is', 'Alex'] splits at the string thats inside the .split()
print('My name is Alex'.split('m')) # ['My na', 'e is Alex'] splits at the 'm'

print()

spam = ('''
Dear Alice, 

How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment"

please do not drink it.

Sincerly,
Bob ''')
print(spam.split()) # takes every word and puts it into a list
print(spam.split('\n')) # every list item is when a break happens

print()

# Splitting Strings with the partition() method, returns tuple (before, seperator, after)

print('Hello, World!'.partition('W')) # ('Hello, ', 'W', 'orld!')
print('Hello, World!'.partition('World')) # ('Hello, ', 'World', '!')
print('Hello, World!'.partition('o')) # ('Hell', 'o', ', World!') if the string in the partition occurs more than once, it splits only on the first occurance
print('Hello, World!'.partition('XYZ')) # ('Hello, World!', '', '') if the partition cannot be found then it returns the whole string and two empty strings
before, sep, after = 'Hello, World!'.partition(' ') # can use the assignment trick to assign the three returned strings to three variables
print(before)
print(after)

print()

# Justifying Text with the rjust(), ljust(), and center() Methods

print('Hello'.rjust(10)) # making the string a length of 10 and aligning the text to the right
print('Hello'.rjust(20))
print('Hello, World!'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.rjust(20, '*')) # instead of spaces, the rest of the text is '*' 
print('Hello'.center(20, '='))

print()

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {
    'sandwiches': 4,
    'apples': 12,
    'cups': 4,
    'cookies': 9001
}
printPicnic(picnicItems, 12, 5)
print()
printPicnic(picnicItems, 20, 6)

print()

# Removing Whitespace with the strip(), rstrip(), and lstrip() Methods

spam = '        Hello, World!       '
print(spam.strip()) # doesn't change the variable
print(spam.lstrip()) # 'Hello, World!       '
print(spam.rstrip()) # '        Hello, World!'
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS')) # strips whatever is inside the strip(), only on the outside of the string

print()

# Numeric Values of Characters with the ord() and chr() Methods

print(ord('A')) # 65
print(ord('4')) # 52
print(ord('!')) # 33
print(chr(65)) # 'A'
print(ord('B')) # 66
print(ord('A') < ord('B')) # True
print(chr(ord('A'))) # 'A'
print(chr(ord('A') + 1)) # 'B'

print()

# Copying and Pasting Strings with the Pyperclip Module -> has copy() and paste()

import pyperclip
pyperclip.copy('Hello, World!')
print(pyperclip.paste())

print()






