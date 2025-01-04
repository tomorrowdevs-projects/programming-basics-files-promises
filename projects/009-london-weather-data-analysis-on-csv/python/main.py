import os
import re
from datetime import datetime

def writeToLog(string):
    logFileName='logFile.txt'
    if os.path.exists(logFileName):
        with open(logFileName,'a') as file:
            file.write(string)
    else:
        with open(logFileName,'w') as file:
            file.write(string)

def readData(fileName):
    try:
        file=open(fileName,'r',encoding='utf-8')
    except:
        raise(FileNotFoundError('{} not found in working directory'.format(fileName)))

    #Data checking
    header=file.readline().strip().split(',')
    dataDict={}
    for column in header:
        dataDict[column]=[]  
    counter=2
    for line in file.readlines()[1:]:
        line=line.strip().split(',')
        if len(line)!=len(header):
            message='Warning: line {} entries number is different from header entries number. It will be skipped!\n'.format(counter)
            writeToLog(message)
        elif not (re.fullmatch('\d+\.\d+',line[1]) and re.fullmatch('\d+\.\d+',line[2]) and re.fullmatch('\d+\.\d+',line[3]) and re.fullmatch('-?\d+\.\d+',line[4]) and re.fullmatch('-?\d+\.\d+',line[5]) and re.fullmatch('-?\d+\.\d+',line[6]) and re.fullmatch('\d+\.\d+',line[7]) and re.fullmatch('\d+\.\d+',line[8]) and re.fullmatch('\d+\.\d+',line[9])):
            message='Warning: line {} has irregular content. It will be skipped!\n'.format(counter)
            writeToLog(message)
        else:
            try:
                datetime.strptime(line[0], '%Y%m%d')
            except:
                message='Warning: line {} has irregular content. It will be skipped!\n'.format(counter)
                writeToLog(message)
            else:
                for column in header:
                    if column=='date':
                        date_obj = datetime.strptime(line[header.index(column)], "%Y%m%d")
                        dataDict[column].append([date_obj.year, date_obj.month, date_obj.day])
                    else:
                        dataDict[column].append(float(line[header.index(column)]))
            finally:
                counter+=1
                continue
        counter+=1
    file.close()
    return dataDict

def generalAnalysis(dataDict):
    #Average max temperature
    averageMaxT=round(sum(dataDict['max_temp'])/len(dataDict['max_temp']),2)

    #Day with max sunshine
    indexMax=dataDict['sunshine'].index(max(dataDict['sunshine']))
    maxSunshineDate='{}/{}/{}'.format(*dataDict['date'][indexMax])

    #Total rain amount for August 2023
    indexList=[]
    counter=0
    for date in dataDict['date']:
        if date[0]==2023 and date[1]==8:
            indexList.append(counter)
        counter+=1
    rainAmount=0
    for index in indexList:
        rainAmount+=dataDict['precipitation'][index]
    
    #Cloud cover analysis
    cloudyDayPercentage=0
    for percentage in dataDict['cloud_cover']:
        if percentage>0.5:
            cloudyDayPercentage+=1
    cloudyDayPercentage=round(cloudyDayPercentage/len(dataDict['cloud_cover'])*100,2)

    return [averageMaxT,maxSunshineDate,rainAmount,cloudyDayPercentage]

def weatherExtremes(dataDict):
    extremeDict={}

    #Extreme max temperature day
    indexMax=dataDict['max_temp'].index(max(dataDict['max_temp']))
    maxTempDate='{}/{}/{}'.format(*dataDict['date'][indexMax])
    maxTemp=dataDict['max_temp'][indexMax]
    meanTemp=dataDict['mean_temp'][indexMax]
    minTemp=dataDict['min_temp'][indexMax]
    extremeDict['temp']=[maxTempDate,maxTemp,meanTemp,minTemp]

    #Extreme precipitation day
    indexMax=dataDict['precipitation'].index(max(dataDict['precipitation']))
    maxPrecipitationDate='{}/{}/{}'.format(*dataDict['date'][indexMax])
    maxPrecipitation=dataDict['precipitation'][indexMax]
    extremeDict['pecipitation']=[maxPrecipitationDate,maxPrecipitation]

    #Extreme snow day
    indexMax=dataDict['snow_depth'].index(max(dataDict['snow_depth']))
    maxSnowDate='{}/{}/{}'.format(*dataDict['date'][indexMax])
    maxSnowTemp=dataDict['max_temp'][indexMax]
    extremeDict['snow']=[maxSnowDate,maxSnowTemp]
    
    return extremeDict

def seasonalAnalysis(dataDict):
    dataDict['year']=[]
    for date in dataDict['date']:
        dataDict['year'].append(date[0])
    
    dataDict['month']=[]
    for date in dataDict['date']:
        dataDict['month'].append(date[1])

    #max seasonal temperature
    averageMaxSeasonalTemp=[]
    for i in range(1,13):
        monthTemp=[]
        counter=0
        for month in dataDict['month']:
            if month==i:
                monthTemp.append(dataDict['max_temp'][counter])
            counter+=1
        averageMaxSeasonalTemp.append(round(sum(monthTemp)/len(monthTemp),2))

    #max seasonal precipitation
    averageSeasonalPrecipitation=[]
    for i in range(1,13):
        counter=0
        totalAmount=0
        for month in dataDict['month']:
            if month==i:
                totalAmount+=dataDict['precipitation'][counter]
            counter+=1
        averageSeasonalPrecipitation.append(round(totalAmount,2))
    
    return [averageMaxSeasonalTemp,averageSeasonalPrecipitation]
                
if __name__=='__main__':
    dataDict=readData('london_weather.csv')
    if os.path.exists('logFile.txt'):
        print('Warning: the input dataset seems to have some issues. Please, take a view of logFile.txt')
    print('GENERAL ANALYSIS\n{}'.format(generalAnalysis(dataDict)))
    print('WEATHER EXTREMES\n{}'.format(weatherExtremes(dataDict)))
    print('SEASONAL ANALYSIS\n{}'.format(seasonalAnalysis(dataDict)))