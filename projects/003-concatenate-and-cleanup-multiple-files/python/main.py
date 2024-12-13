import argparse
import re
import os

def initCmdLineParser():
    parser=argparse.ArgumentParser(usage='dataCleaner.py [inputFilesPath] [outputFilePath]')
    parser.add_argument('inputFilesPath',help='directory of the original files')
    parser.add_argument('outputFilesPath',help='directory where the cleaned data will be saved')
    return parser

def concatFiles(filesPath):
    filesNames=os.listdir(filesPath)
    with open(os.path.join(filesPath,filesNames[0]),'r') as file:
        header=file.readline()

    content=[]
    for fileName in filesNames:
        with open(os.path.join(filesPath,fileName),'r') as file:
            content=content+file.readlines()[1:]
    content=[header]+content
    return content,header

def splitFile(content):
    for i in range(len(content)):
        content[i]=content[i].strip('\n').split(',')
    return content

def delUncompleteLines(content,header):
    i=0
    while i<len(content):
        if len(content[i])<len(header)-1:
            del content[i]
        i+=1
    return content

def stripTrailingSpaces(content):
    for i in range(len(content)):
        for j in range(len(content[i])):
            content[i][j]=content[i][j].rstrip().lstrip()
    return content

def checkData(content):
    productExpression=re.compile('.+ - .+')
    priceExpression=re.compile('\d+.\d\d')
    stockExpression=re.compile('\d+')
    for i in range(1,len(content)):
        productMatch=productExpression.fullmatch(content[i][0])
        priceMatch=priceExpression.fullmatch(content[i][2])
        stockMatch=stockExpression.fullmatch(content[i][3])
        if productMatch==None or priceMatch==None or stockMatch==None:
            del content[i]
    return content

def delDuplicatedLines(content):
    for line in content:
        if content.count(line)>1:
            i=content.index(line)+1
            while i<len(content)-1:
                if content[i]==line:
                    del content[i]
                i+=1
    return content

def writeToFile(content,outputFilePath):
    with open(outputFilePath,'w') as file:
        for i in range(len(content)):
            line=','.join(content[i])
            file.write(line+'\n')

parser=initCmdLineParser()
args=parser.parse_args()
content,header=concatFiles(args.inputFilesPath)
content=splitFile(content)
content=delUncompleteLines(content,header)
content=stripTrailingSpaces(content)
content=checkData(content)
content=delDuplicatedLines(content)
writeToFile(content,args.outputFilesPath)