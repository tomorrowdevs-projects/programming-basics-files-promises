import re
import matplotlib.pyplot

def readFile(filePath):
    with open(filePath,'r') as file:
        content=file.read()
    return content

def textProcessing(content):
    groups=re.findall('[a-zA-ZàèéìòùÀÈÉÌÒÙ]+',content.strip('\n'))
    procContent=''
    for element in groups:
        procContent=procContent+element
    return procContent

def letterFreq(procContent):
    freqDict={}
    for letter in procContent:
        if letter in freqDict:
            freqDict[letter]+=1
        else:
            freqDict[letter]=1
    return freqDict

def plot(freqDict):
    fig,ax=matplotlib.pyplot.subplots(figsize=(5, 2.7),layout='constrained')
    categories=freqDict.keys()
    val=freqDict.values()
    ax.bar(categories,val)
    matplotlib.pyplot.show()

def main():
    filePath=input('Enter the file path: ')
    content=readFile(filePath)
    content=textProcessing(content)
    freqDict=letterFreq(content)
    plot(freqDict)

if __name__=='__main__':
    main()