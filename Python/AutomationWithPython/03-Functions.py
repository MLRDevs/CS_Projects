# Alex Miller 3-Functions

def hello():
    print('Hello World')
    print('')

hello()

def helloname(name):
    print('Hello ' + name)
    print('')

helloname('Alex')

import random

def getAns(ansnum): # magic 8 ball function
    if ansnum == 1:
        return 'It is certain'
    elif ansnum == 2:
        return 'It is decidedly so'
    elif ansnum == 3:
        return 'Yes'
    elif ansnum == 4:
        return 'Answer hazy, try again'
    elif ansnum == 5:
        return 'Ask later'
    elif ansnum == 6:
        return 'Concentrate and ask again'
    elif ansnum == 7:
        return 'My answer is no'
    elif ansnum == 8:
        return 'Outlook not so good'
    elif ansnum == 9:
        return 'Very Doubtful'

r = random.randint(1,9)
fortune = getAns(r)
print(fortune) # or print(getAns(random.randint(1,9)))
print('')

# print(Hello)
# print(World)

# Hello
# World

print('Hello', end='') # HelloWorld
print('World')

print('Cats', 'Dogs', 'Mice') # Cats Dogs Mice ==> even tho i didnt include spaces, they print the spaces, which is dumb
print('Cats', 'Dogs', 'Mice', sep=',') # Cats,Dogs,Mice ==> sep is the seperation attribute, changed it from a space to a comma
print('')


# Stack calls
def a(): 
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()
print('')

def spam():
    eggs = 10

spam()
# print(eggs) ==> doesn't work, not in local scope

def spams():
    eggs = 99
    bacon()
    print(eggs) # eggs doesnt change even tho its changed in a function that just happened due to it being in a different scope

def bacon():
    hams = 101
    eggs = 0

spams()
print('')

def spamss(): # no parameter so python considers 'eggs' to be a global variable and uses that
    print(eggs) # prints 42
eggs = 42
spamss()
print(eggs) # prints 42
print('')

def thing():
    global shell
    shell = 'spam'

shell = 'global'
thing()
print(shell)

# prints 'spam' 

# global vs local
# if a variable is being used in the global scope (outside of all methods) then it is always a global variable
# if there is a 'global' statement, its global
# variable used inside a function with no global statement, it's a local variable
# if variable is not used in an assignment statement, it is global

def thing1():
    global thin
    thin = 'spam' # global

def baconthing():
    thin = 'bacon' # local

def ham():
    print(thin) # global

thin = 42 # global
thing1()
print(thin) # spam

print('')

def div(divideby): # exception handling, try-catch
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Error: Divide By Zero')

print(div(2))
print(div(12))
print(div(0))
print(div(1))

def div2(divideby):
    return 42 / divideby

try:
    print(div2(2))
    print(div2(12))
    print(div2(0))
    print(div2(1))
except ZeroDivisionError:
    print('Error: Divide By Zero')

print('')

import time, sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # one tenth second pause

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()


