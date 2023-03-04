# Files in Python

# Create empty file
fl1 = open('test1.txt', 'w')
fl1.close()

# Create file with text
with open('test2.txt', 'w') as fl2:
    fl2.write('This file made from Python')

# Append text to file
with open('test2.txt', 'a') as fl2:
    fl2.write('\nBy Andrey Tarasenko')

# Append text to file by print()
with open('test2.txt', 'a') as fl2:
    print('\nFebruary, 2023', file = fl2)

# Read text from file line by line
with open('test2.txt', 'r') as fl2:
    for i in fl2:
        print(i, end = '')

print()

# Read text from file by line
with open('test2.txt', 'r') as fl2:
    print(fl2.readline())

# Read entire text from file
with open('test2.txt', 'r') as fl2:
    print(fl2.read())

# Read text from file by lines to list
with open('test2.txt', 'r') as fl2:
    print(fl2.readlines())

with open('test1.txt', 'a') as fl1:
    for i in range(3):
        fl1.write(input('Input a string '))
        fl1.write('\n')

with open('test1.txt', 'r') as fl1:
    print(fl1.read())

import os

# Make directory
fold = input('Input name for make new folder ')
os.mkdir(fold)

# Rename directory
print('Input new name for rename created folder', fold)
nfold = input()
os.rename(fold, nfold)

# Remove directory
if input('Remove the folder? y/n ') == 'y':
    os.rmdir(nfold)

# Remove files
if input('Remove the files? y/n ') == 'y':
    os.remove('test1.txt')
    os.remove('test2.txt')
