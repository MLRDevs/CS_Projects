# Alex Miller
# Collatz Conjecture

import time, sys

def main():
    print("""
    The Collatz Conjecture (Sequence or 3n+1) is a sequence starting at n.

    It follows three basic rules:

        if n is odd  -> n = 3n+1
        if n is even -> n = n/2
        if n is 1    -> Sequence done otherwise infinite loop
    
    It is said that every positive number eventually leads down to 1""")
    print()

    num = input('Enter the starting number (greater than 0 or QUIT to quit): ')
    print()

    if num.upper() == 'QUIT':
        print()
        print('Thanks for playing!')
        sys.exit()

    while not num.isdecimal() or num == 0:
        print('That is not a number or not greater than 0, try again')
        num = input('Enter the starting number: ')
    
    n = int(num)
    print(n, end ='', flush=True)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        
        print(', ' + str(n), end='', flush=True)
        time.sleep(0.1)
    print()
    print()
    again = input('Would you like to try another number? (yes or no): ')
    if again.lower().startswith('y'):
        main()
    else:
        print()
        print('Thanks for playing!')
        print()
        sys.exit()

if __name__ == '__main__':
    main()
