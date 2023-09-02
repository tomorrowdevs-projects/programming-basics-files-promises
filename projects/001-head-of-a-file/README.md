# Head of a File

Unix-based operating systems usually include the command **head**, 
by default it displays the first 10 lines of a file.

The command are quite useful for quickly viewing parts of files, 
especially log files or other large text files, without having to open the entire file in a text editor.

### Head
The options of the head command that we want to simulate:

- **The -n option**. Change the number of lines in the output, add the **-n** (--lines) argument before the file name:   
  `head -n [number] file_name`


- **The -v option**. Display the file name before outputting the specified lines with the **-v** argument 
  before the file name and the other options.  

    `head -v -n 3 file1`     
    `====> file1 <====`      
    `line1`  
    `line2`  
    `line3`


- **Multiple File**. Display the first lines of multiple files using a single command:  
  `head [option] file_name1 file_name2`

Create a program that simulate the default use and 
the suggested options as optionally arguments of the command.   

The script should be executed via command line with the necessary arguments.
		 


# Documentation

For this project solution you may use:

- Files and Exceptions

# Deadline

This project requires to be completed in a maximum of **4 hours**
