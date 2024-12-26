import os
import pypdf

def extractContent(pdfPath):
    try:
        pdfReader=pypdf.PdfReader(pdfPath)
    except:
        print('File not exsisting!')
        return None
    else:
        pdfContent=''
        for page in pdfReader.pages:
            pdfContent=pdfContent+page.extract_text()
        return pdfContent 

def wordFrequencies(pdfContent):
    wordFreq={}
    pdfContent=pdfContent.replace('\n',' ').replace('.','').replace(',','').replace("'",'').lower().split()
    for word in pdfContent:
        if not word in wordFreq:
            wordFreq[word]=0
        else:
            wordFreq[word]+=1
    pairedData=zip(wordFreq.keys(),wordFreq.values())
    wordFreq=dict(sorted(pairedData,key=lambda x: x[1],reverse=True))
    return wordFreq

def main():
    pdfDir=input("Please, enter the pdf directory: ")
    while not os.path.exists(pdfDir):
        pdfDir=input("Unexisting directory! Please, enter the pdf directory: ")
    pdfName=input("Please enter the pdf name: ")
    pdfPath=os.path.join(pdfDir,pdfName)
    pdfContent=extractContent(pdfPath)
    if pdfContent==None:
        return
    else:
        wordFreq=wordFrequencies(pdfContent)
        print("Here's the word's frequencies in {}".format(pdfName))
        for word in wordFreq:
            print("{}: {}".format(word,wordFreq[word]))

if __name__=='__main__':
    main()