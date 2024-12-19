import os

dataStatDict={}

def readFile(filePath):
    with open(filePath,'r',encoding='utf-8') as file:
        dataDict={}
        for line in file.readlines()[1:]:
            line=line.strip('\n').replace('"','').split(',')
            if line[0] in dataDict:
                if line[3] in dataDict[line[0]]:
                    dataDict[line[0]][line[3]][line[1]]=float(line[2])*100
                else:
                    dataDict[line[0]][line[3]]={line[1]:float(line[2])*100}
            else:
                dataDict[line[0]]={line[3]:{line[1]:float(line[2])*100}}
    return dataDict

def nameDiversityAnalysis(dataDict):
    yrNamesNrDict={}
    for year in dataDict:
        yrNamesNrDict[year]={}
        for sex in dataDict[year]:
            yrNamesNrDict[year][sex]=len(dataDict[year][sex])
    return yrNamesNrDict

def nameLenghtAnalysis(dataDict):
    yrNamesLenDict={}
    for year in dataDict:
        yrNamesLenDict[year]={}
        for sex in dataDict[year]:
            meanLen=0
            for name in dataDict[year][sex].keys():
                meanLen+=len(name)
            yrNamesLenDict[year][sex]=int(meanLen/len(dataDict[year][sex]))
    return yrNamesLenDict

def yrPopularAnalysis(dataDict):
    yrNamesRank={}
    for year in dataDict:
        yrNamesRank[year]={}
        for sex in dataDict[year]:
            yrNamesRank[year][sex]={}
            names=dataDict[year][sex].keys()
            frequency=dataDict[year][sex].values()
            pairedData=sorted(zip(names,frequency),key=lambda x:x[1])
            i=1
            for elem in pairedData:
                if i<11:
                    yrNamesRank[year][sex][i]=elem[0]
                    i+=1
                else:
                    break
    return yrNamesRank

def firstLetterAnalysis(dataDict):
    firstLetterRank={'boy':{},'girl':{}}
    firstLetterFreq={'boy':{},'girl':{}}
    for sex in firstLetterFreq:
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            firstLetterFreq[sex][letter]=0
    for sex in firstLetterFreq:
        for year in dataDict:
            for name in dataDict[year][sex]:
                firstLetterFreq[sex][name[0].lower()]+=dataDict[year][sex][name]
    for sex in firstLetterFreq:
        pairedData=sorted(zip(firstLetterFreq[sex].keys(),firstLetterFreq[sex].values()),key=lambda x:x[1])
        i=1
        for elem in pairedData:
            if i<6:
                firstLetterRank[sex][i]=elem[0]
                i+=1
            else:
                break
    return firstLetterRank

def lastLetterAnalysis(dataDict):
    firstLetterRank={'boy':{},'girl':{}}
    firstLetterFreq={'boy':{},'girl':{}}
    for sex in firstLetterFreq:
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            firstLetterFreq[sex][letter]=0
    for sex in firstLetterFreq:
        for year in dataDict:
            for name in dataDict[year][sex]:
                firstLetterFreq[sex][name[-1].lower()]+=dataDict[year][sex][name]
    for sex in firstLetterFreq:
        pairedData=sorted(zip(firstLetterFreq[sex].keys(),firstLetterFreq[sex].values()),key=lambda x:x[1])
        i=1
        for elem in pairedData:
            if i<6:
                firstLetterRank[sex][i]=elem[0]
                i+=1
            else:
                break
    return firstLetterRank

def decadePopularAnalysis(dataDict):
    yrNamesRank={}
    decadeDataDict={}
    yrList=[]
    for year in dataDict:
        yrList.append(int(year))

    decade=min(yrList)
    decadeDataDict[decade]={}
    for year in dataDict:
        if int(year)-decade>9:
            decade+=10
            decadeDataDict[decade]={}

        for sex in dataDict[year]:
            decadeDataDict[decade][sex]={}
            for name in dataDict[year][sex]:
                if name in decadeDataDict[decade][sex]:
                    decadeDataDict[decade][sex][name]+=dataDict[year][sex][name]
                else:
                    decadeDataDict[decade][sex][name]=dataDict[year][sex][name]
        
    for decade in decadeDataDict:
        yrNamesRank[decade]={}
        for sex in decadeDataDict[decade]:
            yrNamesRank[decade][sex]={}
            names=decadeDataDict[decade][sex].keys()
            frequency=decadeDataDict[decade][sex].values()
            pairedData=sorted(zip(names,frequency),key=lambda x:x[1])
            i=1
            for elem in pairedData:
                if i<6:
                    yrNamesRank[decade][sex][i]=elem[0]
                    i+=1
                else:
                    break
    return yrNamesRank

# def writeToCsv(dataDict,fileName,filePath):
#     with open(os.path.join(filePath,fileName),'w',encoding='utf-8') as file:
#         header='year,sex,'
#         for year

def main():
    filePath=input('Enter the path where the name dataset is saved: ')
    while not os.path.exists(filePath):
        filePath=input('Please, check the file path and retry or press enter to quit: ')
        if filePath=='':
            return
    dataDict=readFile(filePath)
    dataStatDict['diversity analysis']=nameDiversityAnalysis(dataDict)
    dataStatDict['name lenght analysis']=nameLenghtAnalysis(dataDict)
    dataStatDict['top 10 analysis']=yrPopularAnalysis(dataDict)
    dataStatDict['first letter analysis']=firstLetterAnalysis(dataDict)
    dataStatDict['last letter analysis']=lastLetterAnalysis(dataDict)
    dataStatDict['decade top 5 analysis']=decadePopularAnalysis(dataDict)
    print(dataStatDict['top 10 analysis'])

if __name__=='__main__':
    main()