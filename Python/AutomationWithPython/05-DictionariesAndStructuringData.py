# Alex Miller 5-Dictionaries And Structuring Data

# Dictionary
# the keys for this dictionary is "size" "color" and "disposition"
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'} # assigns the dictionary to 'myCat'
print(myCat['size']) # prints the assigned value in the dictionary "myCat" for the key "size"
print('my cat has ' + myCat['color'] + ' fur') # 'my cat has gray fur'

print('')

spam = {12345: 'Luggage Combination', 42: 'The Answer'} # can also use integers as keys
print(spam[42])

print('')

# lists are ordered while dictionaries are not
# lists in different orders while having the same stuff, are not equal
# dictionaries with different orders, while having the same stuff, are equal
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam==bacon) # False
eggs = {
    'name': 'Zophie',
    'species': 'cat',
    'age': '8'
}
ham = {
    'species': 'cat',
    'age': '8',
    'name': 'Zophie'
}
print(eggs == ham) # True

print('')

# trying to access a key that does not exist gives you a "KeyError"
birthdays = {
    'Alice': 'Apr 1',
    'Bob': 'Jan 6',
    'Carol': 'Mar 4'
}
# asks user for name and prints corrisponding bday, if the name doesn't exist, ask for the name and add it to the dictionary
while True:
    print('Enter a name (Blank to quit): ')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
        print()
    else:
        print('I do not have the information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
        print()

print()

# keys(), values(), and items() methods
spam = {
    'color': 'red',
    'age': 42
}
for v in spam.values(): # prints the values (red, 42)
    print(v)
print()

for k in spam.keys(): # prints the keys (color, age)
    print(k)
print()

for i in spam.items(): # prints both values and keys ('color', 'red') ('age', 42)
    print(i)
print()

print(spam.keys()) # prints "dict_keys([color', 'age])"
print(list(spam.keys())) # prints ['color', 'age']

print()

for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v)) # "Key: color Value: red"

print()

# Checking whether a value or key exists in a dictionary
spam = {
    'name': 'Zophie',
    'age': 7
}
print('name' in spam.keys()) # True
print('Zophie' in spam.values()) # True
print('color' in spam.keys()) # False
print('color' not in spam.keys()) # True
print('color' in spam) # False

print()

# The get() method, get('key', return value if key doesn't exist)
picnicItems = {
    'apples': 5,
    'cups': 2
}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups') # "I am bringing 2 cups"
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs') # "I am bringing 0 eggs"

print()

# The setdefault() method, setdefault('key to chek', 'set the key to this value')
spam = {
    'name': 'Pooka',
    'age': 5
}
spam.setdefault('color', 'black')
print(spam.get('color', 'none')) # prints "black"
print(spam)
spam.setdefault('color', 'white') # doesn't change to white, the default value was already set to 'black'
print(spam.get('color', 'none')) # prints "black"

print()

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}
for character in message: # assigns each letter in the message as a key, and the value the amount of times that letter is in the message
    count.setdefault(character, 0)
    count[character] += 1
print(count)

print()

# pretty printing
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}
for character in message: # assigns each letter in the message as a key, and the value the amount of times that letter is in the message
    count.setdefault(character, 0)
    count[character] += 1
pprint.pprint(count) # prints in a list format instead

print()

# Nested dictionaries and lists
allGuests = {
    'Alice': {
        'apples': 5,
        'pretzels': 12
    },
    'Bob': {
        'ham sandwiches': 3,
        'apples': 2
    },
    'Carol': {
        'cups': 3,
        'apple pies': 1
    }
}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought: ')
print(' - Apples            ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups              ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes             ' + str(totalBrought(allGuests, 'Cakes')))
print(' - Ham Sandwiches    ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies        ' + str(totalBrought(allGuests, 'apple pies')))

# Using data structures to model real world things
Board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}
def printboard(Board):
    print(Board['top-L'] + '|' + Board['top-M'] + '|' + Board['top-R'])
    print('-+-+-')
    print(Board['mid-L'] + '|' + Board['mid-M'] + '|' + Board['mid-R'])
    print('-+-+-')
    print(Board['low-L'] + '|' + Board['low-M'] + '|' + Board['low-R'])

turn = 'X'
for i in range(9):
    printboard(Board)
    print('Turn for ' + turn + ' move on what space?')
    move = input()
    Board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printboard(Board)





