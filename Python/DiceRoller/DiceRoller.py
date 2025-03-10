# Alex Miller
# Dice Roller

import random, sys

# main method
def main():
    num = input('How many 6-sided dice do you want to roll? (up to 10) ') # ask for how many dice
    while not num.isdecimal() or int(num) <= 0 or int(num) > 10: # if it's above ten, 0 or below, or isn't a number
        print('That doesn\'t work, try again')
        print()
        num = input('How many 6-sided dice do you want to roll? ')
    
    # All the dice
    ONE = """
+-------+
|       |
|   O   |
|       |
+-------+
"""
    TWO_1 = """
+-------+
| O     |
|       |
|     O |
+-------+
"""
    TWO_2 = """
+-------+
|     O |
|       |
| O     |
+-------+
"""
    THREE_1 = """
+-------+
| O     |
|   O   |
|     O |
+-------+
"""
    THREE_2 = """
+-------+
|     O |
|   O   |
| O     |
+-------+
"""
    FOUR = """
+-------+
| O   O |
|       |
| O   O |
+-------+
"""
    FIVE = """
+-------+
| O   O |
|   O   |
| O   O |
+-------+
"""
    SIX_1 = """
+-------+
| O   O |
| O   O |
| O   O |
+-------+
"""
    SIX_2 = """ 
+-------+
| O O O |
|       |
| O O O |
+-------+
"""

    # putting all the dice in one array
    Dice = [ONE, TWO_1, TWO_2, THREE_1, THREE_2, FOUR, FIVE, SIX_1, SIX_2]
    print()
    print('Printing the dice...')
    print()
    amount = 0
    dicenums = []

    # adding the numerical values to an array
    for i in range(int(num)):
        rand = random.randint(0,len(Dice)-1)
        if Dice[rand] == ONE:
            amount += 1
        elif Dice[rand] == TWO_1 or Dice[rand] == TWO_2:
            amount += 2
        elif Dice[rand] == THREE_1 or Dice[rand] == THREE_2:
            amount += 3
        elif Dice[rand] == FOUR:
            amount += 4
        elif Dice[rand] == FIVE:
            amount += 5
        elif Dice[rand] == SIX_1 or Dice[rand] == SIX_2:
            amount += 6
        dicenums.append(Dice[rand])
    
    # printing all the dice in not a dumb way
    d = [j.split("\n") for j in dicenums]
    zipped = zip(*d)
    a = 0
    for elems in zipped:
        print(' '.join(elems))
        

        
    
    print()
    print('You rolled a {}!'.format(amount)) # print amount rolled
    print()

    again = input('Would you like to roll again? (yes or no): ')
    if again.lower().startswith('y'): # roll again
        print()
        main()
    else:
        print()
        print('Thanks for rolling!')
        print()
        sys.exit()


if __name__ == '__main__': # run main()
    main()