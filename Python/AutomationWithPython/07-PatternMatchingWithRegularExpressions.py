# Alex Miller 7-Pattern Matching with Regular Expressions

#Finding Patterns of Text Without Regular Expressions

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone Number Found: ' + chunk)
print('Done')

print()

# Creating Regex Objects (regular expressions)

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # \d is a digit character, '\d{3}-\d{3}-\d{4}' is also the same pattern

# Matching Regex Objects

mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())

print()

# Review of Regular Expression Matching
# import the regex module with 'import re'
# creat a regex object wiht the 're.compile()' function (use a raw string)
# pass the string you want to search into the regex objects search() method. this returns a Match object
# call the Match object's group() to return a string of the actual matched text

# Grouping with Parentheses

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())

print()

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

print()

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242')
print(mo.group(1))
print(mo.group(2))

print()

# Escape chars: \. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)

# Matching Multiple Groups with the Pipe

heroRegex = re.compile(r'Batman|Tina Fey') # pipe, use it to match one of many expressions, will match either or, but when both occur, it takes the first one it finds
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

print()

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

print()

# Optional Matching with Question Mark (zero or one)

batRegex = re.compile(r'Bat(wo)?man') # optional part of the pattern (wo)
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

print()

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

print()

# Matching Zero or More with Star (*)

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

print()

# Matching One or More with a Plus (+)

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

print()

# Matching Specific Repetitions with Braces

# (Ha){3} == (Ha)(Ha)(Ha)
# (Ha){3,5} == ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(HA))

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2 == None)

print()

# Greedy and Non-Greedy Matching

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

print()

# the finall() Method

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

# Groups
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# Not Groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')) # prints Tuples

# Not Groups, returns a list of string matches
# Groups, returns a list of tuples of strings, one string for each group

print()

# Character Classes

# \d == any numeric digit 1-9
# \D == any character that is not a numeric digit 1-9
# \w == any letter, numeric digit, or the underscore char (_)
# \W == any character that is not a letter, numeric digit, or underscore char (_)
# \s == any space, tab, or newline char
# \S == any character that is not a space, tab, or newline char

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
# will match text that has one or more numeric digits (\d), followed by a whitespace (\s), followed by one or more letter/digit/underscore character (\w)

print()

# Making Your Own Character Classes

# All vowels
vowelRegex = re.compile(r'[aeiouAEIOU]') # use brackets to make your own character class
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD'))
# character class [a-zA-Z0-9] will match all lowercase and uppercase characters along with digits

# No vowels
conRegex = re.compile(r'[^aeiouAEIOU]') # '^' negates, like not in
print(conRegex.findall('Robocop eats baby food. BABY FOOD'))

print()

# The Caret and Dollar Sign Characters

# '^' at the start indicates that a match much occur at the begining
# '$' at the end indicates that a match much occur at the end 

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello, World!'))
print(beginsWithHello.search('He said Hello') == None)

endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty-two') == None)

print()

WholeStringIsNum = re.compile(r'^\d+$')
print(WholeStringIsNum.search('1234567890'))
print(WholeStringIsNum.search('12345xyz67890') == None)
print(WholeStringIsNum.search('12 34567890') == None)

print()

# The Wildcard Character

# '.' will match any character except a newline

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

print()

# Matching Everything with Dot-Star

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

print()

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

print()

# Matching Newlines with the Dot Character

# doesn't get newlines
nonNewlineRegex = re.compile(r'.*')
print(nonNewlineRegex.search('Serve the puplic trust. \nProtect the innocent.\nUphold the law').group())

print()

# gets newlines
newlineRegex = re.compile(r'.*', re.DOTALL)
print(newlineRegex.search('Serve the puplic trust. \nProtect the innocent.\nUphold the law').group())

print()

# Review

# ? matches 0 or 1 of the preceding group
# * matches 0 or more of the preceding group
# + matches 1 or more of the preceding group
# {n} matches exactly n of the preceding group
# {n, } matches n or more of the preceding group
# { ,m} matches 0 to m of the preceding group
# {n,m} matches at least n and at most m of the preceding group
# {n,m}? or *? or +? performs a non greedy match of the preceding group
# ^spam means the string must begin with spam
# spam$ means the string must end with spam
# the . matches any character except newlines
# \d, \w, and \s match a digit, word, or space character respectively
# \D, \W, and \S match anything except a digit, word, or space character respectively
# [abc] matches any character between the brackets (a, b, or c)
# [^abc] matches any character that is not in the brackets

# Case-Insensitive Matching

robocop = re.compile(r'robocop', re.I) # or re.IGNORECASE
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

print()

# Substituting Strings with the sub() Method, sub(string to replace any matches, a string for the regular expression)

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

print()

# Managing Complex Regexes

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)') #WTF
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                      # area code
    (\s|-|\.)?                              # seperator
    \d{3}                                   # first 3 digits
    (\s|-|\.)                               # seperator
    \d{4}                                   # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?            # extension
)''', re.VERBOSE)

# Combining re.IGNORECASE, re.DOTALL, re.VERBOSE

# re.compile() only takes two arguments, use the pipe to add more kinda
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)






