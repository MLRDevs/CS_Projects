# Alex Miller
# Reading and Writing Files

# BackSlash (\) for Windows, ForwardSlash (/) for Mac and Linux

from pathlib import Path
print(Path('spam', 'eggs', 'bacon')) # spam\eggs\bacon # or WindowsPath('spam/eggs/bacon')
print(str(Path('spam', 'eggs', 'bacon'))) # same as above # or spam\\eggs\\bacon

print()

myFiles = [
    'accounts.txt',
    'details.csv',
    'invite.docx'
]
for filename in myFiles:
    print(Path(r'C:\Users\mille', filename))

print()

# Using the (/) to Join Paths

# All print the same things, weird
print(Path('spam') / 'bacon' / 'eggs')
print(Path('spam') / Path('bacon/eggs'))
print(Path('spam') / Path('bacon', 'eggs'))

print()

homeFolder = r'C:\Users\mille'
subFolder = 'spam'

# Prints the same thing
print(homeFolder + '\\' + subFolder)
print('\\'.join([homeFolder, subFolder]))

print()

homeFolder = Path('C:/Users/mille')
subFolder = Path('spam')
print(homeFolder / subFolder)

print()

# The Current Working Directory

import os 
print(Path.cwd())

# The Home Directory

print(Path.home()) # C:\Users\mille

print()

# Aboslute and Relative Paths

# Absolute: start with root folder
# Relative: start with current working directory (cwd)

# Creating New Folders Using the on.makedirs() Function

# makes more than one directory at a time
# os.makedirs('C:\\Users\\mille\\Documents\\CS\\Projects\\Python\\AutomationWithPython\\9-ReadingAndWritingFiles\\Walnut\\Waffles')
# or
# makes only one directory at a time
# Path(r'C:\Users\mille\Documents\CS\Projects\Python\AutomationWithPython\9-ReadingAndWritingFiles\Walnut\Pankcakes').mkdir()

# Handing Absolute and Relative Paths

print(Path.cwd().is_absolute()) # True
print(Path('my/relative/path')) # relative path
print(Path.cwd() / Path('my/relative/path')) # absolute path
print(Path.home() / Path('my/relative/path')) # absolute path

print()

# os.path module

# os.path.abspath(path) == resturn string of the absolute path of the argument, easy way to convert from relative to absolute
# os.path.isabs(path) == will return True if the argument is an absolute path, False if it's a relative path
# os.path.relpath(path, start) == return a string of the relative path from the 'start' to 'path', if 'start' is not provided, cwd is used

print(os.path.abspath('.')) # current path
print(os.path.abspath('.\\Scripts')) # current path + \Scripts
print(os.path.isabs('.')) # False
print(os.path.isabs(os.path.abspath('.'))) # True

print()

print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.path.relpath('C:\\Windows', 'C:\\Walnut\\Waffles'))

print()

# Getting the Parts of a File Path

# C:\Users\Al\Spam.txt
# C: == Drive
# C:\ == Anchor
# \Users\Al\ == Parent
# Spam.txt == Name
# Spam == Stem
# .txt == Suffix

# /home/al/spam.txt
# / == Anchor
# home\al\ == Parent
# spam.txt == Name
# spam == Stem
# .txt == Suffix

p = Path('C:/Users/Al/spam.txt')
print(p.drive)
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)

print()

p = Path.cwd()
print(p)
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])
print(p.parents[3])
print(p.parents[4])
print(p.parents[5])
print(p.parents[6])
print(p.parents[7])
# print(p.parents[8]) == index error

print()

# C:\Windows\System32\clac.exe
# C:\Windows\System32\ == Dir name
# calc.exe == Base name

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(calcFilePath)) # calc.exe
print(os.path.dirname(calcFilePath)) # C:\Windows\System32
print(os.path.split(calcFilePath)) # ('C:\\Windows\\System32', 'calc.exe')
print(calcFilePath.split(os.sep)) # ['C:', 'Windows', 'System32', 'calc.exe']

print()

# Finding File Sizes and Folder Contents

# os.path.getsize(path) == return size in bytes of the file in the 'path' argument
# os.listdir(path) == return a list of filename strings for each file in the 'path' argument

print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
print(os.listdir('C:\\Users\\mille\\Documents\\CS'))

print()

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize += os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)

print()

# Modifying a List of Files Using Glob Patterns

p = Path('C:/Users/mille/Desktop')
print(p.glob('*'))
print(list(p.glob('*'))) # everything on desktop
print()
print(list(p.glob('*.txt'))) # everything ending with that extension
print()
print(list(p.glob('project?.docx'))) # ? stands for any single character, list could be something like ['project1.docx', 'project2.docx'], will not return 'project10.docx' since its only one character, not two
print()
print(list(p.glob('*.?x?'))) # can combine the two, would return both .txt and .exe files
print()

for textFilePathObj in p.glob('*.txt'): # prints every .txt file in the desktop
    print(textFilePathObj)

print()

# Checking Path Validity

# p holds a path object
# p.exists() == returns True if the path exists, False if it does not
# p.is_file() == returns True if the path exists and is a file, False otherwise
# p.is_dir() == returns True if the path exists and is a directory, False otherwise

winDir = Path('C:/Windows')
notExistsDir = Path('C:/This/Folder/Does/Not/Exist')
calcFile = Path('C:/Windows/System32/calc.exe')
print(winDir.exists()) # True
print(winDir.is_dir()) # True
print(notExistsDir.exists()) # False
print(calcFile.is_file()) # True
print(calcFile.is_dir()) # False

print()

dDrive = Path('D:/') # a way to check if there is a flashdrive inserted
print(dDrive.exists()) # False

print()

# The File Reading / Writing Process

# read_text() == returns a string of the full contents of a text file
# write_text() == creates a new text file, or overwrites an existing one, with the string passed to it

p = Path('spam.txt')
p.write_text('Hello, World!')
print(p.read_text())

# open() == return a File object
# read() or write() == on the File object
# close() == clock the file on the File object

# Opening Files With open() Function

helloFile = open(Path.home() / 'hello.txt') # = open('C:\\Users\\mille\\hello.txt') ==> same thing

# Reading the Contents of Files

helloContent = helloFile.read()
print(helloContent) # prints what was in the file

helloFile.close()

print()

p = Path.cwd()
helloFile = open(p / 'hello.txt')
helloContent = helloFile.read()
print(helloContent)

helloFile.close()

sonnetFile = open(p / 'sonnet29.txt')
print(sonnetFile.readlines()) # read multiple lines with line breaks

sonnetFile.close()

print()

# Writing to Files

# cannot write to a file that has been opened in read mode

# pass 'w' as the second argument to open() to open the file in write mode, will overwrite the existing file and start from scratch
# pass 'a' as the second argument to open() to open the file in append mode, append text to an existing file

baconFile = open('bacon.txt', 'w') # open file to write mode, python creates it if it doesn't exist yet
baconFile.write('Hello, World!\n') # write to the file

baconFile.close() # closes he file
baconFile = open('bacon.txt', 'a') # open the file in append mode (adding text to existing files)
baconFile.write('Bacon is not a vegetable') # write to the file

baconFile.close() # close the file
baconFile = open('bacon.txt') # open the file in default mode (read)
content = baconFile.read() # set the contents of the file to the variable
baconFile.close() # close the file

print(content) # print the contents of the file

print()

# Saving Variable with the Shelve Module

import shelve

# saves .bat and that files in the cwd, these files contain the data stored in the shelf
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))

print()

# Saving Variables with the pprint.pformat() Function

import pprint
cats = [{
    'name': 'Zophie',
    'desc': 'chubby'
},
{
    'name': 'Pooka',
    'desc': 'fluffy'
}]
print(pprint.pformat(cats))

fileObj = open('myCats.py', 'w') # create a python program for writing
fileObj.write('cats = ' + pprint.pformat(cats) + '\n') # put the cats dictionary in the .py file
fileObj.close() # close the file

import myCats # we can now import the new .py file we made and use it
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])