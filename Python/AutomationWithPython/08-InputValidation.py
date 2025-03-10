# Alex Miller 8-Input Validation

while True:
    print('Enter your age: ')
    age = input()
    try:
        age = int(age)
    except:
        print('Please enter numeric digits')
        continue
    if age < 1:
        print('Please enter a positive number')
        continue
    break

print(f'your age is {age}')

print()

# The PyInputPlus Module

import pyinputplus as pyip # using the 'as' when importing makes it so you can use a smaller name to call the functions
# inputStr() == built in input() function, can pass custom validation function to it
# inputNum() == ensures the user enters a number and returns an int or float 
# inputChoice() == ensures the user enters one of the provided choices
# inputMenu() == similar to inputChoice() but provides a menu with numbered or lettered options
# inputDatatime() == ensure the user enters a data and time
# inputYesNo() == ensures the user enters a yes or no response
# inputBool() == similar to inputYesNo() but takes a boolean and returns a boolean
# inputEmail() == ensures the user enteres a valid email address
# inputFilepath() == ensures the user enters a valid file path and filename, and can optionally check that a file with that name exists
# inputPassword() == like input() but displays '*' as the user types the password

response = pyip.inputNum()
print(response)

print()

response = input('Enter a number: ') # doesn't print a newline after input()
print(response)

response = pyip.inputInt(prompt='Enter a number: ')
print(response)

print()

# The min, max, greaterThan, and lessThan Keyword Arguments

response = pyip.inputNum('Enter a number: ', min=4)
print(response)

response = pyip.inputNum('Enter a number: ', greaterThan=4)
print(response)

response = pyip.inputNum('>', min=4, lessThan=6)
print(response)

print()

# The Blank Keyword Argument

# by default, a blank isnt allowed unless the blank keyword is set to True

response = pyip.inputNum('Enter num: ')
response = pyip.inputNum('Enter num: ', blank=True)

# The limit, timeout, and default Keyword Arguments

# used to limit the amount of times python asks for valid input

response = pyip.inputNum(limit=2, default='N/A') # if no 'default' keyword, then TimeoutException

print()

# The allowRegexes and blockRegexes Keywords Arguments

response = pyip.inputNum(prompt='Enter Roman Numeral: ', allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zerp'])
print(response)
response = pyip.inputNum(prompt='Enter Roman Numeral: ', allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
print(response)

response = pyip.inputNum(prompt='Enter a number: ', blockRegexes=[r'[02468]$'])
print(response)

response = pyip.inputStr(prompt='Enter a string: ', allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
print(response)

print()

# Passing a Custom Validation Function to inputCustom()

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
    return int(numbers)

response = pyip.inputCustom(addsUpToTen) # although a funtion, doesn't need parentheses after the function name
