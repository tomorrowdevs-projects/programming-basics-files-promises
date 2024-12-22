import os
import sys
import re
   
def main():
    filesPath=os.getcwd()
    helpString="""show the last 10 lines of one or more text files. Some options are provided.\n\nUSAGE\ntail.py [options] [filenames]\n\nPositional arguments\nfilenames: one or more file text names to be shown (remember that the text file has to be in the same place of the script)\n\noptions:\n-n: change the number of lines to be printed (can't be used with +int option)\n+int: print the last lines of the text file starting by the int-th line (can't be used with -n option)\n-h/--help: show this help message"""
    args=sys.argv
    if  len(args)<2:
        print('Error: at least one file name is required')
        print(helpString)
    elif args[1]=='-h' or args[1]=='--help':
        print(helpString)
    else:
        fileNamesIndex=1
        linesToPrint=10
        startingLine=None
        match=re.match('\+\d+',args[1])
        if '-n' in args[1]=='-n':
            try: 
                linesToPrint=int(args[2])
            except:
                print('Error: -n option requires a valid int as argument')
                print(helpString)
                return
            fileNamesIndex=3
        elif match:
            startingLine=int(args[1].strip('+'))
            fileNamesIndex=2

        if len(args)<fileNamesIndex+1:
            print('Error: at least one file name is required')
            print(helpString)
            return
        else:
            for fileName in args[fileNamesIndex:]:
                try:
                    file=open(os.path.join(filesPath,fileName),'r')
                except:
                    print('Warning: {} not existing in {}'.format(fileName,filesPath))    
                else:
                    text=file.readlines()
                    if startingLine==None:
                        startingLine=len(text)-min(linesToPrint,len(text))+1
                    else:
                        if startingLine>len(text):
                            print('warning: {} has only {} lines'.format(fileName,len(text)))
                            continue
                    
                    for i in range(startingLine-1,len(text)):
                            print(text[i])

if __name__=='__main__':
    main()