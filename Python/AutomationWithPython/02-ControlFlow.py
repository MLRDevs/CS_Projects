#Alex Miller 2-Control Flow

# 42 != '42'
# 42 == 42.0
# 42 == 0042.00

# true and true == true
# true and false == false
# false and true == false
# false and false == false

# true or true == true
# true or false == true
# false or true == true
# false or false == false

# not true == false
# not false == true
# not not not not true == true

# (4 < 5) and (5 < 6) == true
# (4 < 5) and (9 < 6) == false
# (1 == 2) or (2 == 2) == true

# 2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2 --> true

# 'else if' in python is 'elif'
# ':' is used to show start of block code
# indentation shows what's in the block codes

name = 'Alex'
age = 22
if name == 'Bob':
	print('Hi Bob')
elif age < 12:
	print('you a kid')
else:
	print("you're not Bob and you're old")
	
# print('you're') --> error
# print("you're") --> no error

name = ''
while name != 'your name':
	print('enter your name: ')
	name = input()
print('about time')

print('My name is')
for i in range(5): # runs 5 times starting at 0
	print('Jimmy Five Times (' + str(i) + ')')

# Jimmy Five Times (0)
# Jimmy Five Times (1)
# Jimmy Five Times (2)
# Jimmy Five Times (3)
# Jimmy Five Times (4)

total = 0
for num in range(101):
	total += num
print(total)

# same thing as the for loop
print('My Name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i += 1 # i++ isnt a thing, which is dumb

for i in range(12, 16): # range where i is, starts at 12, stops at 16
    print(i)

# 12
# 13
# 14
# 15

for i in range(0, 10, 2): # 0 = start value, 10 = stop value, 2 = itteration amount
    print(i)
print('')
# 0
# 2
# 4
# 6
# 8

for i in range(5, -1, -1): # can also go down into negative
    print(i)
print ('')
# 5
# 4
# 3
# 2
# 1
# 0

import random, sys, os, math # can import more than one library in one statement
for i in range(5):
    print(random.randint(1,10)) # prints a random number between 1 and 10
print('')

while True: # case sensative, true != True
    print('Type exit to exit, no to break')
    response = input()
    if response == 'exit':
        sys.exit() # system.exit(0);
    elif response == 'no':
        break
    print('you typed: ' + response + '.')
print('')
print('')
print('Random Number Game')

secretnum = random.randint(1,20)
print('I have a number between 1 to 20, try to guess it')

for guesses in range(1,6):
    print('Take a guess: ')
    guess = int(input())

    if guess < secretnum:
        print('Your guess is too low')
    elif guess > secretnum:
        print('Your guess is too high')
    else:
        break
if guess == secretnum:
    print('Congrats, you got the number in '+ str(guesses) + ' guesses')
else:
    print('You almost had it, the number was ' + str(secretnum))

print('')
print('')
print('Rock Paper Scissors Game')
wins = 0
losses = 0
ties = 0

while True:
    print('%s wins, %s losses, %s ties' % (wins,losses,ties))
    while True:
        print('Enter your move: (r)rock (p)paper (s)scissors or (q)quit')
        playermove = input()
        if playermove == 'q':
            sys.exit()
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break
        print('Type one of r, p, s, or q')
    if playermove == 'r':
        print('ROCK vs..')
    elif playermove == 'p':
        print('PAPER vs..')
    else:
        print('SCISSORS vs..')
    
    randomnum = random.randint(1,3)
    if randomnum == 1:
        cpumove = 'r'
        print('ROCK')
    elif randomnum == 2:
        cpumove = 'p'
        print('PAPER')
    else:
        cpumove = 's'
        print('SCISSORS')
    
    if playermove == cpumove:
        print('It is a tie')
        ties += 1
    elif playermove == 'r' and cpumove == 's':
        print('You win')
        wins += 1
    elif playermove == 'p' and cpumove == 'r':
        print('You win')
        wins += 1
    elif playermove == 's' and cpumove == 'p':
        print('You win')
        wins += 1
    elif playermove == 'r' and cpumove == 'p':
        print('You lose')
        losses += 1
    elif playermove == 'p' and cpumove == 's':
        print('You lose')
        losses += 1
    elif playermove == 's' and cpumove == 'r':
        print('You lose')
        losses += 1
    print('')
    

    


