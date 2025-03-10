#Alex Miller 1-Basics

#Expressions

2 ** 3 # exponent, == 8
22 % 8 # module/remainder == 6
22 // 8 # integer, division/floored, quotient == 2
22 / 8 # division, == 2.75
3 * 5 # multiplication, == 15
5 - 2 # subtraction, == 3
2 + 2 # addition, == 4

print(2 ** 3)
print(22 % 8)
print(22 // 8)
print(22 / 8)
print(3 * 5)
print(5 - 2)
print(2 + 2)

#Strings

# variables don't need types

thing = 'Alice' + 'Bob'
print(thing) # 'AliceBob'

thing = 'Alice' * 3 # must be int
print(thing) # AliceAliceAlice

#Variable Names

#Valid
#current_balance
#CurrentBalance
#account4
#_42
#TOTAL_SUM
#hello

#Not Valid
#current-balance == no hyphen
#current balance == no space
#4account == cannot begin with number
#42 == cannot begin with number
#TOTAL_$UM == no special characters
#'hello' == no quotes

print ('enter your name: ')
name = input()
print('your name is ' + name)

# can add only strings to strings and ints to ints, cannot mix the two
# use the str() to convert it to the string
# use int() to convert a string to an int
# use float() to convers a string to a float

print('your name has ' + str(len(name)) + ' characters in it') # this is dumb as shit but makes sense
print(int('42')) # prints 42
print(float('42.3')) # prints 42.3

print('enter an int: ')
spam = input() # takes "int" and puts it into a string
spam = int(spam) # takes the string and converts it into an int
print(spam)
print(spam * 2) # can now use the variable as an int

down = int(7.7) # rounds down == 7
up = int(7.7) + 1 # rounds up == 8

print(down)
print(up)