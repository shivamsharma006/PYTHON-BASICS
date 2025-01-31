'''Write a python program to print the contents of a directory using the os module.
Search online for the function which does that. '''

import os

# Get the current working directory or specify a path
directory_path = '/'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

for item in contents :
    print(item)

