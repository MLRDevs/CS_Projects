# Alex Miller
# getting factors of inputted number

import sys, math # imports

def main(): # main method
    while True: # main loop
        print()
        num = input('Enter a positive whole number. (or QUIT to quit): ')
        if num.upper() == 'QUIT': # if user wants to quit
            print()
            print('Thanks for factoring!')
            sys.exit()
        if not (num.isdecimal() and int(num) > 0): # if it is a num and above 0
            continue
        number = int(num)

        factors = []

        for i in range(1, int(math.sqrt(number)) + 1): # get the factors an add it to the list
            if number % i == 0:
                factors.append(i)
                factors.append(number // i)
    
        factors = list(set(factors))
        factors.sort() # sort the factors so they're in the right spot

        for i, factor in enumerate(factors): # print the factors
            factors[i] = str(factor)
        print(', '.join(factors))

        print()
        again = input('Try another number? (yes or no): ') # if users wants to do another number
        if again.lower().startswith('y'):
            main()
        else: # user quits
            print()
            print('Thanks for factoring!')
            print()
            sys.exit()

if __name__ == '__main__': # run main()
    main()