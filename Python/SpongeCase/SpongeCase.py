# Alex Miller
# Convert normal text to SpongeCase

import sys

def main():
    sponge = ''
    text = input('Enter your text: ') # get the text from user
    for i in range(len(text)): # every char
        if i % 2 == 0: # if i is even, upper
            sponge += text[i].upper()
        else: # if i is odd, lower
            sponge += text[i].lower()
    
    print(sponge) # print the result
    print()
    again = input('Another one? (yes or no): ') # ask if the user wants to do another one
    if again.startswith('y'): # if they do another one
        main()
    else: # if they don't, exit
        print()
        print('Thanks!')
        sys.exit()

if __name__ == '__main__':
    main()