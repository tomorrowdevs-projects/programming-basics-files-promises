import os
import argparse
import sys

def initArgParser():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [options] [fileNames]",
        description="By default prints the first 10 lines of one or more text files. Some options are provided."
    )
    parser.add_argument(
        "-v","--showTitle",
        action='store_true',
        help= "adds the file title before the text lines."
    )
    parser.add_argument(
        "-n","--linesNumber",
        type=int,
        help= "set a different number of text lines to be printed."
    )
    parser.add_argument('fileNames', nargs='*')
    return parser

def argsInOrder(args,parser):
    if args.showTitle:
        if not sys.argv[1] in ['-v','--showTitle']:
            return False
        else:
            if ('-n' in sys.argv or '--linesNumber' in sys.argv) and not (sys.argv[2]=='-n' or sys.argv[2]=='--linesNumber'):
                return False
            else:
                return True
    else:
        if ('-n' in sys.argv or '--linesNumber' in sys.argv) and not (sys.argv[1]=='-n' or sys.argv[1]=='--linesNumber'):
            return False
        else:
            return True
        
def main():    
    directory=os.getcwd()
    parser=initArgParser()
    args=parser.parse_args()
    if not args.fileNames:
        print('no input files')
        parser.print_help()
        return
    else:
        if argsInOrder(args,parser):
            if args.linesNumber!=None:
                linesNumber=args.linesNumber
            else:
                linesNumber=10
            
            for fileName in args.fileNames:
                try:
                    file=open(os.path.join(directory,fileName),'r')
                except:
                    print('{} not existing in {}'.format(fileName,directory))    
                else:
                    text=file.readlines()
                    if args.showTitle:
                        print(fileName)
                    for i in range(min(linesNumber,len(text))):
                        print(text[i])
        else:
            print('wrong arguments order!')
            parser.print_help()
            return

if __name__=='__main__':
    main()