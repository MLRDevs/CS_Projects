# Alex Miller
# Magic 8 Ball

import random, sys

def main():
    messages = [ # messages displayed after asking a question
        'sure why not',
        'no way hosay',
        'fuuuuuuck no',
        'fuuuuuuck yes',
        'well of course',
        'in your dreams',
        'yes',
        'nah',
        'why would you even ask that',
        'absolutely not',
        'absolutely',
        'ask me later',
        'I don\'t care',
        'ask later, not because I want you to but because I don\'t want to answer',
        'duh',
        'that\'s a stupid question',
        'it is certain',
        'it\'s cloudy, I cannot see',
        'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm no'
    ]
    print('\t\t---Magic 8 Ball---')
    print()
    question = input('Enter your question: ')
    print()
    if question[len(question)-1:] == '?': # if the question asked has a ?
        print(messages[random.randint(0,len(messages)-1)])
    else: # else keep asking until there is 
        KeepAsking(messages)
    
    print()
    again = input('Ask again? (yes or no): ') # ask user to ask again
    if again.lower().startswith('y'):
        print()
        main()
    else:
        print()
        print('Thanks for asking!')
        print()
        sys.exit()

def KeepAsking(messages): # keep asking if there is no ?
    while True:
        print('Let\'s try that again (might be missing \'?\')')
        print()
        question = input('Enter your question: ')
        if question[len(question)-1:] == '?':
            print(messages[random.randint(0,len(messages)-1)])
            break
        else:
            KeepAsking(messages)


if __name__ == '__main__': # run main()
    main()