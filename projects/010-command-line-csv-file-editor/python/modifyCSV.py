import os
import sys
import re

def writeToLog(string):
    logFileName='logFile.txt'
    if os.path.exists(logFileName):
        with open(logFileName,'a') as file:
            file.write(string+'\n')
    else:
        with open(logFileName,'w') as file:
            file.write(string+'\n')

def readData(fileName):
    with open(fileName,'r',encoding='utf-8') as file:
        colsNumber=input('Enter the columns number of the csv file: ')
        while not colsNumber.isdigit():
            colsNumber=input('The columns number has to be a an integer! Retry: ')
        colsNumber=int(colsNumber)
        
        data=[]
        counter=1
        for line in file.readlines():
            line=line.strip().split(',')
            if len(line)!=colsNumber:
                writeToLog('Warning: line {} has a different columns number compared to your input ({} columns)!'.format(counter,colsNumber))
            data.append(line)
            counter+=1
    
    if os.path.exists('logFile.txt'):
        print('Warning: a log file has been created into working directory! Please, take a view of it!')
    return data

def paddingValues(data):
    padding=[]
    for i in range(len(data[0])):
        columnPadding=0
        for j in range(len(data)):
            if len(data[j][i])>columnPadding:
                columnPadding=len(data[j][i])
        padding.append(columnPadding)
    return padding

def printTable(data,linesToPrint=None):
    headerFlag=input('Data has an header? (y/n) ')
    while not headerFlag in ['y','n']:
        headerFlag=input('You can only enter y or n: ')
    if headerFlag=='y':
        headerFlag=True
    else:
        headerFlag=False

    if linesToPrint==None:
        linesToPrint=len(data)
    else:
        if linesToPrint>len(data):
            raise(IndexError('linesToPrint out of data dimension!'))
    
    padding=paddingValues(data)
    table='| '
    for i in range(len(data[0])):
        if headerFlag:
            table=table+' {}{} |'.format(' '*(padding[i]-len(data[0][i])),data[0][i])
        else:
            table=table+' {}{} |'.format(' '*(padding[i]-len('column {}'.format(i+1))),'column {}'.format(i+1))
    table=table+'\n'+'-'*(4+3*(len(data[0])-1)+sum(padding))

    if headerFlag:
        startingIndex=1
    else:
        startingIndex=0

    for i in range(startingIndex,linesToPrint):
        table=table+'\n| '
        for j in range(len(data[0])):
            table=table+' {}{} |'.format(' '*(padding[j]-len(data[i][j])),data[i][j])
    print(table)

def writeToFile(data):
    with open('modified.csv',encoding='utf-8',mode='w') as outputFile:
        for i in range(len(data)):
            line=','.join(data[i])+'\n'
            outputFile.write(line)

def addRow(data,destIndex,filePath=None,originIndex=None):
    dataHeaderFlag=input('Data has an header? (y/n) ')
    while not dataHeaderFlag in ['y','n']:
        dataHeaderFlag=input('You can only enter y or n: ')
    if dataHeaderFlag=='y':
        dataHeaderFlag=True
    else:
        dataHeaderFlag=False

    if filePath!=None:
        newDataHeaderFlag=input('New data has an header? (y/n) ')
        while not newDataHeaderFlag in ['y','n']:
            newDataHeaderFlag=input('You can only enter y or n: ')
        if newDataHeaderFlag=='y':
            newDataHeaderFlag=True
        else:
            newDataHeaderFlag=False

        if destIndex<1 or destIndex>len(data[0]):
            raise(IndexError('{} not out of data dimensions!'.format(destIndex)))
        
        try:
            file=open(filePath,encoding='utf-8',mode='r')
        except:
            raise(FileNotFoundError('{} not found'.format(filePath)))
        
        try:
            newRow=file.readlines()[originIndex-1].strip().split(',')
        except:
            raise(IndexError('{} not out of origin data dimensions!'.format(originIndex)))
        
        if len(newRow)!=len(data[0]):
            raise(ValueError("{} doesn't have the same dimension of destination csv file!".format(filePath)))

        if dataHeaderFlag and not newDataHeaderFlag:
            print('Warning: note that the new row source has no header, so its columns are assumed to be in the same order of the destination csv.')
            data.insert(destIndex-1,newRow)
        elif not dataHeaderFlag and newDataHeaderFlag:
            print('Warning: note that the destination csv has no header, so columns of the new rows are assumed to be in the same order of the destination csv.')
            data.insert(destIndex-1,newRow)
        elif dataHeaderFlag and newDataHeaderFlag:
            option=input('Destination csv and new row source have and header. Do you want to use header to obtain the right order of data insertion? (y/n)')
            while not option in ['y','n']:
                option=input('You can only input y or n: ')

            if option=='n':
                data.insert(destIndex-1,newRow)
            else:
                file.seek(0,0)
                header=file.readline().strip().split(',')
                newRowSorted=[]
                for column in header:
                    if not column in data[0]:
                        raise(TypeError("The data provided for the new line insertion don't match with the original data!"))
                    newRowSorted.append(newRow[data[0].index(column)])
                data.insert(destIndex-1,newRowSorted)
        else:
            print('Warning: note that input files have no header, so its columns are assumed to be in the same order.')
            data.insert(destIndex-1,newRow)
        file.close()
    else:
        newRow=[]
        for i in range(len(data[0])):
            if dataHeaderFlag:
                value=input('Enter the value for {}: '.format(data[0][i]))
            else:
                value=input('Enter the value for column {}: '.format(i+1))
            newRow.append(value)
        data.insert(destIndex-1,newRow)
    writeToFile(data)

def addCol(data,destIndex,filePath=None,originIndex=None):
    dataHeaderFlag=input('Data has an header? (y/n) ')
    while not dataHeaderFlag in ['y','n']:
        dataHeaderFlag=input('You can only enter y or n: ')
    if dataHeaderFlag=='y':
        dataHeaderFlag=True
    else:
        dataHeaderFlag=False

    if filePath!=None:
        newDataHeaderFlag=input('New data has an header? (y/n) ')
        while not newDataHeaderFlag in ['y','n']:
            newDataHeaderFlag=input('You can only enter y or n: ')
        if newDataHeaderFlag=='y':
            newDataHeaderFlag=True
        else:
            newDataHeaderFlag=False

        if destIndex<1 or destIndex>len(data[0]):
            raise(IndexError('{} not out of destination data dimensions!'.format(destIndex)))
        
        try:
            file=open(filePath,encoding='utf-8',mode='r')
        except:
            raise(FileNotFoundError('{} not found'.format(filePath)))
        
        newData=file.readlines()
        if destIndex<1 or destIndex>len(newData[0]):
            raise(IndexError('{} not out of origin data dimensions!'.format(destIndex)))

        if dataHeaderFlag and not newDataHeaderFlag:
            if len(newData)!=len(data)-1:
                raise(ValueError("{} doesn't have the same dimension of original csv file!".format(filePath)))
            newColHeader=input('Enter the header for the new column: ')
            data[0].insert(destIndex-1,newColHeader)
            for i in range(len(newData)):
                data[i+1].insert(destIndex-1,newData[i].strip().split(',')[originIndex-1])
        elif not dataHeaderFlag and newDataHeaderFlag:
            if len(newData)!=len(data)+1:
                raise(ValueError("{} doesn't have the same dimension of original csv file!".format(filePath)))
            for i in range(len(newData)-1):
                data[i].insert(destIndex-1,newData[i+1].strip().split(',')[originIndex-1])
        else:
            if len(newData)!=len(data):
                raise(ValueError("{} doesn't have the same dimension of original csv file!".format(filePath)))
            for i in range(len(newData)):
                data[i].insert(destIndex-1,newData[i].strip().split(',')[originIndex-1])
        file.close()
    else:
        if dataHeaderFlag:
            newColHeader=input('Enter the header for the new column: ')
            data[0].insert(destIndex-1,newColHeader)
            startingIndex=1
        else:
            startingIndex=0
                
        for i in range(startingIndex,len(data)):
            value=input('Enter the value for line {}: '.format(i))
            data[i].insert(destIndex-1,value)

    writeToFile(data)

def editData(data,rowIndex,newValue,colIndex=None,colName=None):
    if rowIndex<1 or rowIndex>len(data[0]):
        raise(IndexError('{} not out of data dimensions!'.format(rowIndex)))

    if colIndex:
        if colIndex<1 or colIndex>len(data[0]):
            raise(IndexError('{} not out of data dimensions!'.format(colIndex)))
        data[rowIndex-1][colIndex-1]=newValue
    else:
        try:
            colIndex=data[0].index(colName)
        except:
            raise(ValueError('{} is not in file header!'.format(colName)))
        data[rowIndex-1][colIndex]=newValue
    writeToFile(data)

def deleteRow(data,rowIndex):
    if rowIndex<1 or rowIndex>len(data[0]):
        raise(IndexError('{} not out of data dimensions!'.format(rowIndex)))
    
    del data[rowIndex-1]
    writeToFile(data)

def deleteCol(data,colIndex=None,colName=None):
    if colIndex:
        if colIndex<1 or colIndex>len(data[0]):
            raise(IndexError('{} not out of data dimensions!'.format(colIndex)))
        
        for i in range(len(data)):
            del data[i][colIndex-1]
    else:
        try:
            colIndex=data[0].index(colName)
        except:
            raise(ValueError('{} is not in file header!'.format(colName)))
        
        for i in range(len(data)):
            del data[i][colIndex]
    writeToFile(data)

def sortData(data,reverseFlag=False,colIndex=None,colName=None):
    dataHeaderFlag=input('Data has an header? (y/n) ')
    while not dataHeaderFlag in ['y','n']:
        dataHeaderFlag=input('You can only enter y or n: ')
    if dataHeaderFlag=='y':
        dataHeaderFlag=True
    else:
        dataHeaderFlag=False
    
    if colName:
        try:
            colIndex=data[0].index(colName)
        except:
            raise(ValueError('{} not found in data header!'.format(colName)))
        else:
            header=data[0]
            data=sorted(data[1:],key=lambda line: line[colIndex],reverse=reverseFlag)
            data.insert(0,header)
    else:
        if colIndex<1 or colIndex>len(data[0]):
            raise(IndexError('{} not out of data dimensions!'.format(colIndex)))

        if dataHeaderFlag:
            header=data[0]
            data=sorted(data[1:],key=lambda line: line[colIndex-1],reverse=reverseFlag)
            data.insert(0,header)
        else:
            data=sorted(data,key=lambda line: line[colIndex-1],reverse=reverseFlag)
    writeToFile(data)

def filterData(data,colIndex=None,colName=None,operator=None,operatorArgument=None,regEx=None):
    dataHeaderFlag=input('Data has an header? (y/n) ')
    while not dataHeaderFlag in ['y','n']:
        dataHeaderFlag=input('You can only enter y or n: ')
    if dataHeaderFlag=='y':
        dataHeaderFlag=True
    else:
        dataHeaderFlag=False
    
    if colName:
        try:
            colIndex=data[0].index(colName)+1
        except:
            raise(ValueError('{} not found in data header!'.format(colName)))
    elif colIndex:
        if colIndex<1 or colIndex>len(data[0]):
            raise(IndexError('{} not out of data dimensions!'.format(colIndex)))
    
    if dataHeaderFlag:
        firstIndex=1
    else:
        firstIndex=0

    filteredData=[]
    if operator:
        if operator=='>':
            for i in range(firstIndex,len(data)):
                if data[i][colIndex-1]>operatorArgument:
                    filteredData.append(data[i])
        elif operator=='<':
            for i in range(firstIndex,len(data)):
                if data[i][colIndex-1]<operatorArgument:
                    filteredData.append(data[i])
        elif operator=='==':
            for i in range(firstIndex,len(data)):
                if data[i][colIndex-1]==operatorArgument:
                    filteredData.append(data[i])
        elif operator=='<=':
            for i in range(firstIndex,len(data)):
                if data[i][colIndex-1]<=operatorArgument:
                    filteredData.append(data[i])
        elif operator=='>=':
            for i in range(firstIndex,len(data)):
                if data[i][colIndex-1]>=operatorArgument:
                    filteredData.append(data[i])
        elif operator=='<>':
            for i in range(firstIndex,len(data)):
                if data[i][colIndex-1]!=operatorArgument:
                    filteredData.append(data[i])
        else:
            raise(ValueError('Unknown logical operator!'))

    if regEx:
        for i in range(firstIndex,len(data)):
            if re.fullmatch(regEx,data[i][colIndex-1]):
                filteredData.append(data[i])
    
    if dataHeaderFlag:
        filteredData.insert(0,data[0])

    writeToFile(filteredData)

if __name__=='__main__':
    usage="""USAGE\nRead doc for a deeper description\nmodifyCSV.py [subcommands]\nAvailable subcommands:\nView data in tabular format within comand line: v [filePath] [-l [linesToPrint]]
\nAdd row: ar [filePath] [destIndex] [[sourceFilePath] [sourceIndex]]\nAdd column: ac [filePath] [destIndex] [[sourceFilePath] [sourceIndex]]
\nModify data: md [filePath] [rowIndex] [-c [colIndex]|-h [colName]] [newValue]\nDelte row: dr [filePath] [rowIndex]\nDelete column: dc [filePath] [-c [colIndex]|-h [colName]]
\nSort data: s [filePath] [-c [colIndex]|-h [colName]] -r\nFiter data: f [filePath] [-c [colIndex]|-h [colName]] [-op [operator] [operatorArgument]|-r [regEx]]"""
    args=sys.argv[1:]
    if len(args)<2:
        raise(SyntaxError('Not enough input arguments!\n{}'.format(usage)))
    else:
        if not os.path.exists(args[1]):
            raise(FileNotFoundError('{} not found in working directory!'.format(args[1])))

        if args[0]=='v':
            cmdLineLength=len(args)
            if cmdLineLength==2:
                fileName=args[1]
                linesToPrint=None
            elif cmdLineLength==4:
                if not args[2]=='-l':
                    raise(SyntaxError('Unknow command\n{}'.format(usage)))
                        
                fileName=args[1]
                try:
                    linesToPrint=int(args[3])
                except:
                    raise(ValueError('linesToPrint has to be an integer!\n{}'.format(usage)))
            else:
                raise(SyntaxError('Unknown syntax!\n{}'.format(usage)))
            data=readData(fileName)
            printTable(data,linesToPrint)
        elif args[0]=='ar':
            cmdLineLength=len(args)
            if cmdLineLength==3:
                fileName=args[1]
                try:
                    destIndex=int(args[2])
                except:
                    TypeError('The destination index has to be and integer!')
                filePath=None
                originIndex=None
            elif cmdLineLength==5:
                fileName=args[1]
                try:
                    destIndex=int(args[2])
                except:
                    TypeError('The destination index has to be and integer!')
                
                filePath=args[3]
                try:
                    originIndex=int(args[4])
                except:
                    TypeError('The destination index has to be and integer!')
            else:
                raise(SyntaxError('Unknown syntax!\n{}'.format(usage)))
            data=readData(fileName)
            addRow(data,destIndex,filePath,originIndex)
        elif args[0]=='ac':
            cmdLineLength=len(args)
            if cmdLineLength==3:
                fileName=args[1]
                try:
                    destIndex=int(args[2])
                except:
                    TypeError('The destination index has to be and integer!')
                filePath=None
                originIndex=None
            elif cmdLineLength==5:
                fileName=args[1]
                try:
                    destIndex=int(args[2])
                except:
                    TypeError('The destination index has to be and integer!')
                
                filePath=args[3]
                try:
                    originIndex=int(args[4])
                except:
                    TypeError('The destination index has to be and integer!')
            else:
                raise(SyntaxError('Unknown syntax!\n{}'.format(usage)))
            data=readData(fileName)
            addCol(data,destIndex,filePath,originIndex)
        elif args[0]=='md':
            cmdLineLength=len(args)
            if cmdLineLength==6:
                fileName=args[1]
                try:
                    rowIndex=int(args[2])
                except:
                    raise(TypeError('The row index has to be an integer!'))
                
                if args[3]=='-c':
                    try:
                        colIndex=int(args[4])
                    except:
                        raise(TypeError('The row index has to be an integer!'))
                    colName=None
                elif args[3]=='-h':
                    colIndex=None
                    colName=args[4]
                else:
                    raise(ValueError('Unknown syntax!\n{}'.format(usage)))
                
                newValue=args[5]
            else:
                raise(SyntaxError('Unknown syntax!\n{}'.format(usage)))
            data=readData(fileName)
            editData(data,rowIndex,newValue,colIndex,colName)
        elif args[0]=='dr':
            cmdLineLength=len(args)
            if cmdLineLength==3:
                fileName=args[1]
                try:
                    rowIndex=int(args[2])
                except:
                    raise(TypeError('The row index has to be an integer!'))
            else:
                raise(SyntaxError('Unknown syntax!\n{}'.format(usage)))
            data=readData(fileName)
            deleteRow(data,rowIndex)
        elif args[0]=='dc': 
            cmdLineLength=len(args)
            if cmdLineLength==4:
                fileName=args[1]
                if args[2]=='-c':
                    try:
                        colIndex=int(args[3])
                    except:
                        raise(TypeError('The column index has to be an integer!'))
                    colName=None
                elif args[2]=='-h':
                    colIndex=None
                    colName=args[3]
                else:
                    raise(ValueError('Unknown syntax!\n{}'.format(usage)))
            else:
                raise(SyntaxError('Unknown syntax!\n{}'.format(usage)))
            data=readData(fileName)
            deleteCol(data,colIndex,colName)
        elif args[0]=='s': 
            cmdLineLength=len(args)
            if cmdLineLength==4:
                fileName=args[1]
                if args[2]=='-c':
                    try:
                        colIndex=int(args[3])
                    except:
                        raise(TypeError('The column index has to be an integer!'))
                    colName=None
                elif args[2]=='-h':
                    colIndex=None
                    colName=args[3]
                else:
                    raise(ValueError('Unknown syntax!\n{}'.format(usage)))
                reverseFlag=False
            elif cmdLineLength==5:
                fileName=args[1]
                if args[2]=='-c':
                    try:
                        colIndex=int(args[3])
                    except:
                        raise(TypeError('The column index has to be an integer!'))
                    colName=None
                elif args[2]=='-h':
                    colIndex=None
                    colName=args[3]
                else:
                    raise(ValueError('Unknown syntax!\n{}'.format(usage)))
                
                if args[4]=='-r':
                    reverseFlag=True
                else:
                    raise(ValueError('Unknown syntax!\n{}'.format(usage)))
            else:
                raise(SyntaxError('Unknown syntax!\n{}'.format(usage)))
            data=readData(fileName)
            sortData(data,reverseFlag,colIndex,colName)
        elif args[0]=='f': 
            cmdLineLength=len(args)
            if cmdLineLength==6:
                fileName=args[1]
                if args[2]=='-c':
                    try:
                        colIndex=int(args[3])
                    except:
                        raise(TypeError('The column index has to be an integer!'))
                    colName=None
                elif args[2]=='-h':
                    colIndex=None
                    colName=args[3]
                else:
                    raise(ValueError('Unknown syntax!\n{}'.format(usage)))
                
                if args[4]=='-r':
                    regEx=args[5]
                    operator=None
                    operatorArgument=None
                else:
                    raise(ValueError('Unknown syntax!\n{}'.format(usage)))
            elif cmdLineLength==7:
                fileName=args[1]
                if args[2]=='-c':
                    try:
                        colIndex=int(args[3])
                    except:
                        raise(TypeError('The column index has to be an integer!'))
                    colName=None
                elif args[2]=='-h':
                    colIndex=None
                    colName=args[3]
                else:
                    raise(ValueError('Unknown syntax!\n{}'.format(usage)))
                
                if args[4]=='-op':
                    regEx=None
                    operator=args[5]
                    operatorArgument=args[6]
                else:
                    raise(ValueError('Unknown syntax!\n{}'.format(usage)))
            else:
                raise(SyntaxError('Unknown syntax!\n{}'.format(usage)))
            data=readData(fileName)
            filterData(data,colIndex,colName,operator,operatorArgument,regEx)
        else:
            raise(SyntaxError('Unknown command!\n{}'.format(usage)))
    
    if os.path.exists('logFile.txt'):
        print('Warning: a log file has been created into working directory! Please, take a view of it!')