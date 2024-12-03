'''Unix-based operating systems usually include the command **head**, 
by default it displays the first 10 lines of a file.

The command are quite useful for quickly viewing parts of files, 
especially log files or other large text files, without having to open the entire file in a text editor.'''

import os
file = open('example.txt', 'r')
'''for _ in range(10):
    result1 = file.readline()
    print(result1)'''
result2 = file.readlines()[:10]
file.close()
for i in result2:
    print(i)