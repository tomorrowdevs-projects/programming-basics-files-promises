import os

def main():
    directory=os.getcwd()
    command=input('PS {}> '.format(directory))
    if len(command)<0:
        print('no command')
    else:
        if 'head -v -n ' in command:
            command=command.replace('head -v -n ','')
            command=command.split()
            if len(command)>0:
                try:
                    linesNumber=int(command.pop(0))
                except:
                    print('wrong input')
                else:
                    for i in range(len(command)):
                        try:
                            file=open(os.path.join(directory,command[i]),'r')
                        except:
                            print('file {} not existing'.format(i+1))
                        else:
                            print("====> {} <====".format(command[i]))
                            content=file.readlines()
                            for j in range(min(len(content),linesNumber)):
                                print(content[j])
                        finally:
                            continue
            else:
                print('unknown command')
        elif 'head -v ' in command:
            command=command.replace('head -v ','')
            command=command.split()
            if len(command)>0:
                for i in range(len(command)):
                    try:
                        file=open(os.path.join(directory,command[i]),'r')
                    except:
                        print('file {} not existing'.format(i))
                    else:
                        content=file.readlines()
                        print("====> {} <====".format(command[i]))
                        for j in range(min(10,len(content))):
                            print(content[j])
                    finally:
                        continue
            else:
                print('unknown command')
        elif 'head -n ' in command:
            command=command.replace('head -n ','')
            command=command.split()
            if len(command)>0:
                try:
                    linesNumber=int(command.pop(0))
                except:
                    print('wrong input')
                else:
                    for i in range(len(command)):
                        try:
                            file=open(os.path.join(directory,command[i]),'r')
                        except:
                            print('file {} not existing'.format(i+1))
                        else:
                            content=file.readlines()
                            for j in range(min(linesNumber,len(content))):
                                print(content[j])
                        finally:
                            continue
            else:
                print('unknown command')
        else:
            command=command.split()
            if len(command)>0:
                if command[0]=='head':
                    command.pop(0)
                    for i in range(len(command)):
                        try:
                            file=open(os.path.join(directory,command[i]),'r')
                        except:
                            print('file {} not existing'.format(i+1))
                        else:
                            content=file.readlines()
                            for j in range(min(10,len(content))):
                                print(content[j])
                        finally:
                            continue
                else:
                    print('unknown command')
            else:
                print('unknown command')

if __name__=='__main__':
    main()