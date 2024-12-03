'''Unix-based operating systems usually include the command **tail**, 
by default it displays the last 10 lines of a file

The command are quite useful for quickly viewing parts of files, 
especially log files or other large text files, without having to open the entire file in a text editor.'''

with open('projects/002-tail-of-a-file/python/example.txt', 'r') as file:
    result = file.readlines()[-10:]
    print(result)