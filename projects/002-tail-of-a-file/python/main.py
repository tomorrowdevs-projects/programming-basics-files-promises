import os
import re

def main():
    directory=os.getcwd()
    command=input('PS {}> '.format(directory))
    if len(command)==0:
        print('void command')
    else:
        if re.match(r'tail -n \d+ .+',command)!=None:
            command=command.split()
            command.pop(0)
            command.pop(0)
            linesNumber=int(command[0])
            for i in range(1,len(command)):
                try:
                    file=open(os.path.join(directory,command[i]),'r')
                except:
                    print('file {} not existing'.format(i))
                else:
                    content=file.readlines()
                    for j in reversed(range(min(linesNumber,len(content))+1)):
                        print(content[len(content)-j])
                finally:
                    continue
        elif re.match(r'tail \+\d+ .+',command)!=None:
            command=command.split()
            command.pop(0)
            startingLine=int(command[0])
            for i in range(1,len(command)):
                try:
                    file=open(os.path.join(directory,command[i]),'r')
                except:
                    print('file {} not existing'.format(i))
                else:
                    content=file.readlines()
                    if len(content)<startingLine:
                        print('starting line number exceeds file {} length'.format(i))
                    else:
                        linesNumber=len(content)-startingLine
                        for j in reversed(range(linesNumber+2)):
                            print(content[len(content)-j])
                finally:
                    continue
        elif re.match(r'tail .+',command)!=None:
            command=command.split()
            for i in range(1,len(command)):
                try:
                    file=open(os.path.join(directory,command[i]),'r')
                except:
                    print('file {} not existing'.format(i))
                else:
                    content=file.readlines()
                    for j in reversed(range(min(10,len(content))+1)):
                        print(content[len(content)-j])
                finally:
                    continue
        else:
            print('unknown command')


if __name__=='__main__':
    main()