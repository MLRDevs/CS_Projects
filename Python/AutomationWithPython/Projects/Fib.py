# Alex Miller
# Fibonacci Sequence, enter the number you want in the sequence

import sys, time

while True: # main loop
    while True:
        print('The Fibonacci sequence goes as follows 0, 1, 1, 2, 3, 5, 8, 13...') # explain the sequence
        print('Ex: 5 --> prints 3')
        print('Enter the Nth Fibonacci number you want to calulate, or QUIT to quit')

        response = input('> ').upper()
        if response == 'QUIT': # if user quits
            print()
            print('Thanks for calculating!')
            sys.exit()
    
        if response.isdecimal() and int(response) != 0: # if it's a number that's above 0
            nth = int(response)
            break
        print()
        print('Enter a number greater than 0') # if it's not a number or 0 and below
        print()

    print()

    # base cases
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci number is 1.')
        continue
    
    # if n is too big, takes a long time to calculate and print so warning is issued
    if nth >= 10000:
        print('This is going to take a lot of time so buckle up')
        time.sleep(2)
    
    secondToLastNumber = 0 # 2nd to last number
    lastNumber = 1 # last number
    fibNumbersCalculated = 2
    print('0, 1, ', end='')

    while True: # calculating loop
        nextNumber = secondToLastNumber + lastNumber # get the next number
        fibNumbersCalculated += 1 # counter

        print(nextNumber, end='')

        if fibNumbersCalculated == nth: # when you get to the number inputted
            print()
            print()
            print('The #', fibNumbersCalculated, ' Fibonacci ',
                  'number is ', nextNumber, sep='')
            print()
            break
        
        print(', ', end='')

        # change the variables for the next calculation
        secondToLastNumber = lastNumber
        lastNumber = nextNumber