import os
import argparse
import sys
import re

def positiveInt(string):
    expression=re.compile('\+\d+')
    result=re.fullmatch(expression,string)
    if result!=None:
        return int(result.group(0))
    else:
        return None

def initArgParser():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [options] [fileNames]",
        description="By default prints the last 10 lines of one or more text files. Some options are provided.",
    )
    parser.register('type','+int',lambda string: positiveInt(string))
    parser.add_argument(
        "printFromLine",
        type='+int',
        help= "set the line number from which print. Note that this option can't be used with -n",
        nargs='?'
    )
    parser.add_argument(
        "-n","--linesNumber",
        type=int,
        help= "set a different number of text lines to be printed. Note that this option can't be used with printFromLine"
    )
    parser.add_argument('fileNames',nargs='+')
    return parser

def mutualExclusionCheck(args):
    if args.printFromLine!=None and args.linesNumber!=None:
        return False
    else:
        return True

def argsInOrder(args):
    if args.linesNumber and args.printFromLine:
        if not sys.argv[1] in ['-n','--linesNumber','+'+str(args.printFromLine)]:
            return False
        else:
            return True
    else:
        return True
   
def main():
    directory=os.getcwd()
    parser=initArgParser()
    args=parser.parse_intermixed_args()
    if mutualExclusionCheck(args):
        print("-n option and +int option can't be used at the same time")
        parser.print_help()
        return
    elif argsInOrder(args):
        print('wrong arguments order!')
        parser.print_help()
        return
    else:
        if args.linesNumber:
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
                if args.printFromLine:
                    for i in range(args.printFromLine-1,len(text)):
                        print(text[i])
                else:
                    for i in range(len(text)-min(linesNumber,len(text)),len(text)):
                        print(text[i])

if __name__=='__main__':
    main()