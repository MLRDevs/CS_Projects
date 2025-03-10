# Alex Miller 4-Lists

animals = ['cat', 'bat', 'elephant', 'rat']
print(animals) # prints the whole list with the brackets and everything
print('The ' + animals[0] + ' ate the ' + animals[1])

print('')

animalsnums = [['cat', 'bat'], [10, 20, 30, 40, 50]] # [0][1] ==> [[0,1], [0, 1, 2, 3, 4]]
print(animalsnums[0][1]) # bat
print(animalsnums[1][4]) # 50

print('')
print(animals[-1]) # -1 means the last index, -2 means the second to last index etc.. this is dumb asf

print('')

# slice, print multiple parts of an array
print(animals[0:2]) # 0 -> starting index, 2 -> end index - 1, prints 0 and 1
print(animals[0:-1]) # prints ['cat', 'bat', 'elephant']
print(animals[:]) # prints the whole list
print(animals[1:]) # prints from first index to the end of the list
print(len(animals)) # get the length of the list

print('')

#animals[4] = 'dog'  ==> doesn't work, out of bounds
animals[2] = 'dog' # can change the specific index
print(animals) 

print('')

alph = ['A', 'B', 'C', 'D']
alphanimals = alph + animals # can add arrays together, pretty neat
print(alphanimals)

print('')

del alphanimals[0] # can easily delete indexs, also pretty neat
print(alphanimals)

print('')

catnames = []
while True:
    print('Enter the name of cat ' + str(len(catnames) + 1) + ' or nothing to stop')
    name = input()
    if name == '':
        break
    catnames = catnames + [name]
print('The cats names are:')
for name in catnames: # for loops can also be used in lists (arrays)
    print(' ' + name)

print('')

supplies = ['pens', 'staplers', 'flamthrowers', 'binders']
for i in range(len(supplies)):
    print('Index: ' + str(i) + ' in supplies is: ' + supplies[i])

for index, item in enumerate(supplies): # same thing as 'for i in range(len(supplies))'
    print('Index: ' + str(index) + ' in supplies list: ' + item)

print('')

greetings = 'howdy' in ['hello', 'howdy', 'heyas']
print(greetings) # prints True
greetings = 'cat' not in ['hello', 'howdy', 'heyas']
print(greetings) # prints True

print('')

mypets = ['Zophie', 'Pooka', 'Fatty']
print('Enter a pet name')
name = input()
if name not in mypets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet')

print('')

cat = ['fat', 'gray', 'loud']
size, color, diposition = cat
# size = fat
# color = gray
# diposition = loud
print(size) # prints fat

print('')

import random
pets = ['dog', 'cat', 'fish']
print(random.choice(pets)) # prints a random one from the list
# also could be 'print(pets[random.randint(0, len(pets) - 1)])'

print('')

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people) # shuffles the values in the list
print(people)

print('')

bacon = ['bacon']
bacon *= 3 # multiples the amount of indexs by 3 
print(bacon) # prints "['bacon', 'bacon', 'bacon']"

print('')

print(people.index('Alice')) # prints the index where 'Alice' is in the list
people.append('Alex') # adds to the end of the list
print(people)
people.insert(0, 'Jordan') # insert at a specific index
print(people)
people.remove('Jordan') # removes an item from the list
print(people)

print('')

nums = [5, 10, 26, 2, 99]
nums.sort() # sorts the list from low to hight
people.sort() # sorts the list from A-Z
print(nums)
print(people)
nums.sort(reverse=True) # sorts in reverse order (high to low)
people.sort(reverse=True) # sorts in reverse order (Z-A)
print(nums)
print(people)
# cannot sort a list that has both strings and integers, has to be same data type

print('')

chars = ['a', 'Z', 'A', 'z']
chars.sort(key=str.lower) # treats all the strings as if they were all lowercase
print(chars)

print('')

nums = [1, 90, 26, 15, 78]
nums.reverse() # easily reverses the order of the list
print(nums)

print('Four score and seven ' + \
    'years ago') # splitting up an instruction to multiple lines, doesn't work the usual java / C++ way

print('')

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely'
    'Answer hazy, try later'
    'Ask again later'
    'Concentrate and ask again'
    'No'
    'Outlook not so good'
    'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)]) # random number from 0 to list length - 1, then prints the string at that index

print('')

name = 'Alex'
print(name[0]) # prints 'A'
for i in name:
    print('***' + i + '***')

print('')

phrase = 'Zophie a cat'
newphrase = phrase[0:7] + 'the' + phrase[8:12] # replacing a specific part in a string
print(phrase)
print(newphrase)

eggs = ('hello', 42, 0.5) # this is a tuple, tuples cannot be appended, modified, or removed
print(eggs[0])
print(eggs[1:3]) # print specific things in a tuple even with different data types
print(eggs[0:2]) # prints "('hello', 42)"

print('')

print(type(('hello',))) # type() gives the type that the data is, in this case its a tuple
print(type('hello')) # str type
print(tuple(['cat', 'dog', 5])) # can change the type from one thing to another, list to tuple
print(list(('cat', 'dog', 5))) # tuple to list
print(list('hello')) # prints "['h', 'e', 'l', 'l', 'o']" string to list

print('')

spam = [0, 1, 2, 3, 4, 5]
cheese = spam # create a reference
cheese[1] = 'Hello' # changing the reference also changes the original
print(spam)
print(cheese)

print('')

print(id('howdy')) # specific id to the machine, address in memory

print('')

bacon = 'hello'
print(id(bacon))
bacon += ' world'
print(id(bacon)) # id slightly changes due to the change of the string

print('')

eggs = ['cat', 'dog']
print(id(eggs))
eggs.append('moose') # appending doesn't change the memory location
print(id(eggs))
eggs = ['bat', 'cat', 'mat'] # new list so new memory location
print(id(eggs))

# append, remove, extend, sort, reverse methods all modify the lists without changing the memory location

print('')

def eggs(somepar):
    somepar.append('hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) # prints "[1, 2, 3, 'hello']"

print('')

import copy
spam = ['A', 'B', 'C', 'D']
print(id(spam))
cheese = copy.copy(spam)
print(id(cheese)) # different id of spam
cheese[1] = 42
print(spam)
print(cheese) # cheese is a different list so only one list is changed

print('')

# Conway's Game of Life

import time
width = 60
height = 20

nextCells = []
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)
while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    for y in range(height):
        for x in range(width):
            print(currentCells[x][y], end='')
        print()
    
    for x in range(width):
        for y in range(height):
            leftCoord = (x - 1) % width
            rightCoord = (x + 1) % width
            aboveCoord = (y - 1) % height
            belowCoord = (y + 1) % height
            
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1
            
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '
    time.sleep(1)




