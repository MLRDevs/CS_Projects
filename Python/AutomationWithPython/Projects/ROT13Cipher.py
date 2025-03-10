# Alex Miller
# Rotation 13 Cipher

import sys

# all the letters
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print('ROT 13 Cipher')
print()

def main(): # main method
    while True:
        print('Enter a message to Encrypt/Decrypt (or QUIT to quit)')
        message = input('> ')
        if message.upper() == 'QUIT': # if the user wants to quit
            print()
            print('Thanks for translating!')
            sys.exit()
        
        translated = ''
        for character in message:
            if character.isupper(): # if the char is an upper case
                transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26 # change the char to 13 down the line
                translated += UPPER_LETTERS[transCharIndex]
            elif character.islower(): # if the char is a lower case
                transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
                translated += LOWER_LETTERS[transCharIndex]
            else: # if it's just a character that's not a letter Ex: / , ; ' 
                translated += character
        
        print('The Translated message is: ') # print the result
        print(translated)
        print()

        again = input('Want to translate another message? (yes or no): ') # if the user wants to cipher again
        if again.startswith('y'):
            main()
        else:
            print()
            print('Thanks for translating!')
            sys.exit()

if __name__ == '__main__':
    main()
