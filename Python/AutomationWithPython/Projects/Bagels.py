# Alex Miller
# Number guessing program

import random, sys

NUM_DIGITS = 3
MAX_GUESSES = 10

def main(): # main method
    print(""" 
    Welcome to the Bagels Number game
    I am thinking of a {}-digit number, no repeats, the way you guess is by clues:

        Pico  - one digit is correct but in the wrong spot
        Fermi  - one digit right and in the right spot
        Bagels - no digit is correct
    
    Example: the secret number is 248 and you guess 843.
    The clues would be: Fermi Picco.""".format(NUM_DIGITS)) # printing the rules

    while True: # main game loop
        print() 
        secretNum = getSecretNum() # get the secret number
        print('I have thought of a number.')
        print('You have {} guesses to get it right'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES: # while you have guesses left
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal(): # fool proof
                print('Guess #{}'.format(numGuesses))
                guess = input('< ')
            clues = getClues(guess, secretNum) # get the clues with the numbers provided
            print(clues)
            print()
            numGuesses += 1

            if guess == secretNum: # if the guess is right
                break
            if numGuesses > MAX_GUESSES: # ran out of guesses
                print('You ran out of guesses')
                print('The answer was {}'.format(secretNum))
        
        print('Do you want ot play again> (yes or no)') # playing again
        if not input('> ').lower().startswith('y'):
            break
    print('Thank you for playing!')

def getSecretNum(): # creating the secret number
    numbers = list('0123456789')
    random.shuffle(numbers) # shuffling 0-9

    secretNum = ''
    for i in range(NUM_DIGITS): # grabbing the first three of the shuffled nums to make the secret num
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum): # getting the clues for the guess
    if guess == secretNum: # if the guess is correct
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)): # adding the clues to the array
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0: # if no clues are needed then everything is wrong so bagels
        return 'Bagels'
    else:
        clues.sort() # sorting the clues and adding a space between them
        return ' '.join(clues)

if __name__ == '__main__': # run main()
    main()
