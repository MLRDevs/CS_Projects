# Alex Miller
# 11-Debugging

# raise statement:

# raise keyword
# a call to the Exception() function
# a string with a helpful error message passed to the Exception() function

# raise Exception('This is an error')

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' '* (width-2)) + symbol)
    print(symbol * width)

for sym, w, h, in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))

print()

# Getting the Traceback as a String

import traceback 
try:
    raise Exception('This is an error message')
except: # takes the traceback errors and moves it into a file
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')

print()

# Assertions

# Assertion statement:

# the assert keyword
# a condition, that is an expression that evaluates to True or False (bool)
# a comma
# a string to display when the condition is False

# basically the info is true, if its not, then there is a bug somewhere and stop the program 

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)
assert ages[0] <= ages[-1] # asserts the first age is less than or equal to the last age

# because the assert is True, it did nothing, it's bug free, basically its a sanity check

ages.reverse()
print(ages)
# assert ages[0] <= ages[-1] # its false so AssertionError

print()

# Logging Module

import logging 
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of Program')
# when python logs an event it creates a LogRecord object 
# the basicConfig() method lets you specify what deatails about the LogRecord object you want to see and how you want it displayed

def factorial(n):
    logging.debug('Start of the factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ' total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of Program')

print()

# Logging Levels

# DEBUG ==> loggin.debug() ==> used for small details, only when diagnosing problems
# INFO ==> logging.info() ==> used to record info on general events in your program or confirm that things are working at that point
# WARNING ==> logging.warning() ==> used to indicate a potential problem that doesn't prevent the program from working but might do so in the future
# ERROR ==> logging.error() ==> used to record an error that caused the program to fail to do something
# CRITICAL ==> loggin.critical() ==> used to indicate a fatal erro that has caused or is about to cause the whole program to stop running entirely

logging.debug('Some debugging details')
logging.info('The logging module is working')
logging.warning('An error message is about to be logged')
logging.error('An error has occured')
logging.critical('The program is unable to recover')

print()

# Disabling Logging

logging.disable(logging.CRITICAL)
logging.critical('CRITICAL')
logging.error('ERROR')

print()





