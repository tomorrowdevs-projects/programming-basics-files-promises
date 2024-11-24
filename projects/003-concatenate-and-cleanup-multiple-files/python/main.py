import os

def readFile(filePath):
    with open(filePath,'r') as file:
        content=file.readlines()
        return content

def concatFiles(contentList):
    curDir=os.getcwd()
    with open(os.path.join(curDir,'combined_products.txt'),'w') as file:
        file.write('Product Name,Category,Price,Stock Quantity\n')
        for content in contentList:
            for i in range(1,len(content)):
                file.write(content[i].replace(', ',','))
    return os.path.join(curDir,'combined_products.txt')

def cleanDataset(filePath):
    seenLines=[]
    with open(filePath,'r') as file:
        content=file.readlines()
    with open(filePath,'w') as file:
        for line in content:
            if line in seenLines or len(line.split(','))<4:
                continue
            else:
                seenLines.append(line)
        file.writelines(seenLines)
            
def main():
    dataDir=input('Enter the data directory: ')
    try:
        fileNames=os.listdir(dataDir)
    except:
        print('Unexisting directory, retry.')
        return
    contents=[]
    for fileName in fileNames:
        filePath=os.path.join(dataDir,fileName)
        contents.append(readFile(filePath))
    savingDir=concatFiles(contents)
    cleanDataset(savingDir)

if __name__=='__main__':
    main()
