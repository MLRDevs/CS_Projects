# Alex Miller
# Organizing Files

import shutil, os

from pathlib import Path

# shutil.copy(source, destination) ==> can be strings or path objects ==> 
# method will copy the file at the path 'source' tp the folder at path 'destination'
# if 'destination' is a filename, it will be used as the new name of the copied file
# this method returns a string or path object of the copied file
p = Path.cwd()
# shutil.copy(p / 'spam.txt', p / 'some_folder')
# shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')

# shutil.copytree() ==> copy whole tree

# shutil.copytree(p / 'spam', p / 'spam_backup') # takes the entire spam folder and makes a new folder 'spam_backup' and puts the contents of the spam folder in there

print()

# Moving and Renaming Files and Folders

# shutil.move(source, destination) ==> will move from one destination to another 
# if the destination is a folder, the source gets moved into the folder
# if the file exists already at the destination, it is overwritten

# shutil.move(p / 'eggs.txt', p / 'spam') == moves the eggs.txt into the spam folder

# shutil.move(p / 'spam.txt', p / 'spammy.txt') == renames spam.txt to spammy.txt

# shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt') == moves bacon to eggs folder and renames it new_bacon

print()

# Permanently Deleting Files and Folders

# os.unlink(path) == delete the file at path
# os.rmdir(path) == delete folder at path
# shutil.rmtree(path) == remove folder at path and all files and folders it contains
for filename in p.glob('*.txt'):
    # os.unlink(filename) == delete 'spammy.txt'
    print(filename)

print()

# Safe Deletes with the send2trash Module

import send2trash

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable')
baconFile.close()

send2trash.send2trash('bacon.txt') # sends to recycling bin

print()

# Walking a Directory Tree

# prints all the folders and files at a directory
for folderName, subfolders, filenames in os.walk('C:\\Users\\mille\\Documents\\CS\\Projects\\Python\\AutomationWithPython'):
    print('the current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print()

# os.walk returns three values through each iteration:

# a string of the current folder's name
# a list of strings of the folders in the current folder (current iteration)
# a list of strings of the files in the current folder (current iteration)


# Compressing Files with the zipfile Module

# Reading ZIP Files

import zipfile

p = Path.cwd()
exampleZip = zipfile.ZipFile(p / 'example.zip')
print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}')
exampleZip.close()

print()

# Extracting from ZIP Files

exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.extractall() # defaults to the cwd, can also pass a path through this method to extract it to
exampleZip.close()

print()

# Creating and Adding to ZIP Files

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


