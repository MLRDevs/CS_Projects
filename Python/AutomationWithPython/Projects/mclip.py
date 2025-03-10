# Alex Miller
# A multi-clipboard program

TEXT = {
    'email': 'milleral@nmu.edu',
    'phone': '+1-906-235-4870',
    'address': '384 3rd Street Allouez, MI 49805'
}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard')
else:
    print('There is no text for ' + keyphrase)