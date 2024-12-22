# Tail of a File

Unix-based operating systems usually include the command **tail**,
by default it displays the last 10 lines of a file

The command are quite useful for quickly viewing parts of files,
especially log files or other large text files, without having to open the entire file in a text editor.

### Tail

The options of the tail command that we want to simulate:

- __The -n option__. Change the number of lines in the output, add the __-n__ (--lines) argument before the file name:  
   `tail -n [number] file_name`
- **The +NUM sign**. To specify the starting line.  
   For example, `tail +15 input.txt` prints input.txt starting from line number 15, until the end of the file.
- __Multiple File__. Display the last lines of multiple files using a single command:  
   `tail [option] file_name1 file_name2`

Create a program that simulate the default use and
the suggested options as optionally arguments of the command.

The script should be executed via command line with the necessary arguments.

# Documentation

For this project solution you may use:

- Files and Exceptions

# Deadline

This project requires to be completed in a maximum of **4 hours**
