import os

def readFile(filePath):
    with open(filePath,'r',encoding='utf-8') as file:
        dataDict={}
        for line in file.readlines()[1:]:
            line=line.strip('\n').replace('"','').split(',')
            year=int(line[0])
            sex=line[3]
            name=line[1]
            percent=float(line[2])*100
            if year in dataDict:
                if sex in dataDict[year]:
                    dataDict[year][sex][name]=percent
                else:
                    dataDict[year][sex]={name:percent}
            else:
                dataDict[year]={sex:{name:percent}}
    return dataDict

def askYear(dataDict):
    inputOk=False
    while not inputOk:
        try:
            year=int(input('Enter the year on wich perform the analysis: '))
        except:
            print('Only numeric values!')
        else:
            if year in dataDict.keys():
                inputOk=True
            else:
                print('Only years between {} and {}').format(min(dataDict.keys()),max(dataDict.keys()))
        finally:
            pass
    return year

def nameDiversityAnalysis(dataDict,year):
    for sex in dataDict[year]:
        print('In {}, {} uniques names of {}s have been registered.'.format(year,len(dataDict[year][sex]),sex))
    return

def nameLengthAnalysis(dataDict):
    for year in dataDict:
        for sex in dataDict[year]:
            meanLegth=0
            for name in dataDict[year][sex]:
                meanLegth+=len(name)
            meanLegth=meanLegth/len(dataDict[year][sex])
            print('{} - {}: {}'.format(year,sex,meanLegth))

def yrPopularAnalysis(dataDict,year):
    print("""Here's the name rank for {}""".format(year))
    for sex in dataDict[year]:
        print("""{}s' rank""".format(sex))
        names=dataDict[year][sex].keys()
        frequency=dataDict[year][sex].values()
        pairedData=sorted(zip(names,frequency),key=lambda x:x[1])
        i=1
        for elem in pairedData:
            if i<11:
                print("""{} - {}""".format(i,elem[0]))
                i+=1
            else:
                break

def letterAnalysis(dataDict,index):
    for sex in ['boy','girl']:
        print("""{}s' rank""".format(sex))
        firstLetterFreq={}
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            firstLetterFreq[letter]=0

        for year in dataDict:
            for name in dataDict[year][sex]:
                firstLetterFreq[name[index].lower()]+=dataDict[year][sex][name]

        pairedData=sorted(zip(firstLetterFreq.keys(),firstLetterFreq.values()),key=lambda x:x[1])
        i=1
        for elem in pairedData:
            if i<6:
                print("""{} - {}""".format(i,elem[0]))
                i+=1
            else:
                break

def decadePopularAnalysis(dataDict):
    decadeDataDict={}
    decade=min(dataDict.keys())
    decadeDataDict[decade]={}
    for year in dataDict:
        if year-decade>9:
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
        print("""{}'s""".format(decade))
        for sex in decadeDataDict[decade]:
            rankString='{}s: '.format(sex)
            names=decadeDataDict[decade][sex].keys()
            frequency=decadeDataDict[decade][sex].values()
            pairedData=sorted(zip(names,frequency),key=lambda x:x[1])
            i=1
            for elem in pairedData:
                if i<6:
                    rankString=rankString+'{} - {}, '.format(i,elem[0])
                    i+=1
                else:
                    break
            rankString=rankString.rstrip(', ')
            print(rankString)
    return

def main():
    filePath=input('Enter the path where the name dataset is saved: ')
    while not os.path.exists(filePath):
        filePath=input('Please, check the file path and retry or press enter to quit: ')
        if filePath=='':
            return
    dataDict=readFile(filePath)

    operation=''
    operation=input("""You can perform:\n-Diversity analysis [1]\n-Name length analysis [2]\n-Top 10 analysis [3]\n-First letter analysis [4]\n-Last letter analysis [5]\n-Top 5 decade analysis [6]\nEnter the number of operation you want to perform or enter 0 to quit: """)
    while operation!='0':
        while len(operation)==0 and not operation in ['0','1','2','3','4','5','6']:
            operation=input("""You can perform:\n-Diversity analysis [1]\n-Name length analysis [2]\n-Top 10 analysis [3]\n-First letter analysis [4]\n-Last letter analysis [5]\n-Top 5 decade analysis [6]\nEnter the number of operation you want to perform: """)

        if operation=='0':
            return
        elif operation=='1':
            year=askYear(dataDict)
            nameDiversityAnalysis(dataDict,year)
        elif operation=='2':
            nameLengthAnalysis(dataDict)
        elif operation=='3':
            year=askYear(dataDict)
            yrPopularAnalysis(dataDict,year)
        elif operation=='4':
            letterAnalysis(dataDict,0)
        elif operation=='5':
            letterAnalysis(dataDict,-1)
        elif operation=='6':
            decadePopularAnalysis(dataDict)
        operation=input("""You can perform:\n-Diversity analysis [1]\n-Name length analysis [2]\n-Top 10 analysis [3]\n-First letter analysis [4]\n-Last letter analysis [5]\n-Top 5 decade analysis [6]\nEnter the number of operation you want to perform or enter 0 to quit: """)

if __name__=='__main__':
    main()