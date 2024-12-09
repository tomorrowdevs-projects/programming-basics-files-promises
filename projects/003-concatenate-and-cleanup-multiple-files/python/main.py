'''
In this exercise, you will practice concatenating data from multiple text files and cleaning up the combined dataset.   
You'll work with a set of text files containing information about products and their attributes.   
Your task is to concatenate these files into a single dataset and perform some basic data cleaning tasks.

Examine the structure of the text files to understand how the data is organized.

Define functions:
- **read files**, the function will take care of read the content of each text file and store it in a 
    list or another appropriate data structure. Accepts the path as input.


- **concatenate files**, the function will take care of concatenate the content from all the text files 
    to create a single combined dataset.


- **clean dataset**, the function will take care of performing the following data cleaning tasks:
    - Remove any duplicate lines.
    - Remove any lines with missing or incomplete information.
    - Remove any leading or trailing whitespace from each line.


- **save file**, the function will take care of save the cleaned and concatenated dataset to a new text file
    named combined_products.txt including a single header and with each value separated with a comma.
'''

def read_files(file, file2):
    list1 = file.readlines()
    list2 = file2.readlines()
    stringlist = ''.join(list1)
    stringlist2 = ''.join(list2)
    return stringlist, stringlist2

def concatenate_files(file, file2):
    list1 = file.readlines()
    list2 = file2.readlines()
    concatenateddata = list1 + list2
    concatenateddatastring = ''.join(concatenateddata)
    return concatenateddatastring

def clean_dataset(file, file2):
    list1 = file.readlines()
    list2 = file2.readlines()
    concatenatedlists = list1
    concatenatedlists += [line for line in list2 if line not in list1]
    cleanconcatenatedlists = ''.join(concatenatedlists)
    return cleanconcatenatedlists

def save_file(cleanconcatenatedlists):
    with open('projects/003-concatenate-and-cleanup-multiple-files/python/combined_products.txt', 'w') as file3:
        file3.write(cleanconcatenatedlists)

def main():
    file = open('projects/003-concatenate-and-cleanup-multiple-files/python/example.txt', 'r')
    file2 = open('projects/003-concatenate-and-cleanup-multiple-files/python/example 2.txt', 'r')
    stringlist, stringlist2 = read_files(file, file2)
    print(stringlist, "\n", stringlist2)
    print(concatenate_files(file, file2))
    cleanconcatenatedlists = clean_dataset(file, file2)
    print(save_file(cleanconcatenatedlists))
    file.close()
    file2.close()

if __name__ == '__main__':
    main()