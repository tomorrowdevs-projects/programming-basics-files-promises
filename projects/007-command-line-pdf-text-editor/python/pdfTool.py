import os
import sys
import re
import pymupdf
import fpdf
import pypdf

def extractContent(pdfPath):
    pdf=pymupdf.open(pdfPath)
    pdfLimits=[]
    pdfLimits.append(pdf[0].get_text('blocks')[0][0])
    pdfLimits.append(pdf[0].get_text('blocks')[0][1])
    pdfLimits.append(pdf[0].get_text('blocks')[0][2])
    pdfLimits.append(pdf[0].get_text('blocks')[0][3])
    pdfContent=[]
    for page in pdf:
        pdfContent.append(page.get_text())
        for line in page.get_text('blocks'):
            if line[0]<pdfLimits[0]:
                pdfLimits[0]=line[0]

            if line[1]<pdfLimits[1]:
                pdfLimits[1]=line[1]
            
            if line[2]>pdfLimits[2]:
                pdfLimits[2]=line[2]

            if line[3]>pdfLimits[3]:
                pdfLimits[3]=line[3]
    pdf.close()
    return pdfContent,pdfLimits

def replaceText(pdfContent,newText,oldText):
    searchPattern=oldText.split()
    searchPattern='\s*'.join(searchPattern)
    for i in range(len(pdfContent)):
        pdfContent[i]=re.sub(searchPattern, newText, pdfContent[i])
    return pdfContent

def lineMapping(pageContent):
    lineMap={}
    counter=0
    for i in range(len(pageContent)):
        if pageContent[i].strip()!='':
            lineMap[counter]=i
            counter+=1
    return lineMap

def addText(pdfContent,page,line,word,newText):
    pageContent=pdfContent[page-1].splitlines()
    lineMap=lineMapping(pageContent)
    absLine=lineMap[line-1]
    lineContent=pageContent[absLine].split()
    lineContent.insert(word,newText)
    pageContent[absLine]=' '.join(lineContent)
    pdfContent[page-1]='\n'.join(pageContent)
    return pdfContent

def delText(pdfContent,oldText=None,pageRange=None,lineRange=None,wordRange=None):
    if pageRange!=None:
        if pageRange[0]<1 or pageRange[1]>len(pdfContent):
            raise(IndexError('wrong page range!'))

    if oldText!=None:
        pdfContent=replaceText(pdfContent,'',oldText)
        return pdfContent
    else:
        for i in range(pageRange[0],pageRange[1]+1):
            if lineRange!=None:
                pageContent=pdfContent[i-1].splitlines()
                lineMap=lineMapping(pageContent)
                if lineRange[0]<1 or lineRange[1]>len(lineMap):
                    raise(IndexError('wrong line range!'))
                if wordRange!=None:
                    for j in range(lineRange[0],lineRange[1]+1):
                        absLine=lineMap[j-1]
                        lineContent=pageContent[absLine].split()
                        if wordRange[0]<1 or wordRange[1]>len(lineContent):
                            raise(IndexError('wrong word range!'))
                        del(lineContent[wordRange[0]-1:wordRange[1]])
                        pageContent[absLine]=' '.join(lineContent)
                else:
                    del(pageContent[lineMap[lineRange[0]-1]:lineMap[lineRange[1]]])
                pdfContent[i-1]='\n'.join(pageContent)
            else:
                pdfContent[i-1]=''
    return pdfContent

def writeToPdf(fileName,pdfContent,pdfLimits):
    pdf = fpdf.FPDF('P', 'pt', 'A4')
    pdf.set_font('Arial', '', 10)
    pdf.set_margins(pdfLimits[0],pdfLimits[1])
    pdf.add_page()
    for pageContent in pdfContent:
        pdf.multi_cell(pdfLimits[2]-pdfLimits[0],10,pageContent)
    pdf.output('{}_modified.pdf'.format(fileName), 'F')

def mergePdf(firstPath,*args):
    mainPdf=pymupdf.open(firstPath)
    for filePath in args:
        pdf=pymupdf.open(filePath)
        mainPdf.insert_pdf(pdf)
    pdf.close()
    mainPdf.save('merged.pdf')
    mainPdf.close()

def splitPdf(pdfPath,*args):
    originalPdf = pypdf.PdfReader(pdfPath)
    if len(args)%2>0:
        raise(ValueError('input must always be a range'))
    counter=1
    for interval in args:
        if counter%2>0:
            merger = pypdf.PdfWriter()
            rangeStart=interval-1
            counter+=1
        else:
            rangeClose=interval-1
            merger.append(originalPdf,(rangeStart,rangeClose+1)) 
            merger.write('splitted_{}.pdf'.format(counter//2))
            counter+=1

if __name__=='__main__':
    usage="""HELP MESSAGE\n\nUSAGE\npdfTool.py [subcommand] [arguments] [options]\n\nSUBCOMMANDS\n-h\--help: show this help message\n
rt: replace [oldString] with [newString] --> usage: pdfTool.py rt [fileName] [newString] [oldString]\n
at: add [newString] after a [word] into a [line] in a [page]. Note that [word], [line] and [page] are int --> usage: pdfTool.py at\n
    [fileName] [page] [line] [word] [newString]\n
dt: delete [searchString] or a range of words. --> usage: pdfTool.py dt [fileName] [-ss/--searchString [searchString]|-r/--range]\n
m: merge tow or more pdf files by the order the user provides them. --> usage: pdfTool.py m [fileNames]\n
s: split one pdf in one or more new files composed by the ranges provided by the user. --> usage: pdfTool.py s [filename] [ranges]"""
    args=sys.argv
    if not args[1] in ['-h','--help','rt','at','dt','m','s']:
        raise(SyntaxError('{} is not a valid subcommand for {}'.format(args[1],args[0])))
    else:
        if args[1]=='-h' or args[1]=='--help':
            if len(args)>2:
                raise(SyntaxError("help can't accept any argument\n{}".format(usage)))
            else:
                print(usage)
        elif args[1]=='rt':
            if len(args[2:])<3:
                raise(SyntaxError('not enough arguments for {} subcommand\n{}'.format(args[1],usage)))
            else:
                if not os.path.exists(args[2]):
                    raise(FileNotFoundError('{} not found in working directory!\n{}'.format(args[2],usage)))
                elif not re.fullmatch('.*\.pdf',args[2]):
                    raise(TypeError('input file has to be a .pdf!\n{}'.format(usage)))
                else:
                    pdfContent,pdfLimits=extractContent(args[2])
                    pdfContent=replaceText(pdfContent,args[3],args[4])
                    writeToPdf(args[2],pdfContent,pdfLimits)
        elif args[1]=='at':
            if len(args[2:])<5:
                raise(SyntaxError('not enough arguments for {} subcommand\n{}'.format(args[1],usage)))
            else:
                if not os.path.exists(args[2]):
                    raise(FileNotFoundError('{} not found in working directory!\n{}'.format(args[2],usage)))
                elif not re.fullmatch('.*\.pdf',args[2]):
                    raise(TypeError('input file has to be a .pdf!\n{}'.format(usage)))
                elif type(args[3])!=int or type(args[4])!=int or type(args[5])!=int:
                    raise(TypeError('page, line and rowd have to be int!\n{}'.format(usage)))
                else:
                    pdfContent,pdfLimits=extractContent(args[2])
                    pdfContent=addText(pdfContent,args[3],args[4],args[5],args[6])
                    writeToPdf(args[2],pdfContent,pdfLimits)
        elif args[1]=='dt':
            if not os.path.exists(args[2]):
                raise(FileNotFoundError('{} not found in working directory!\n{}'.format(args[2],usage)))
            elif not re.fullmatch('.*\.pdf',args[2]):
                raise(TypeError('input file has to be a .pdf!\n{}'.format(usage)))
            else:
                if not args[3] in ['-ss','--searchString','-r','--range']:
                    raise(SyntaxError('{} is not a valid option for {} subcommand!\n{}'.format(args[3],args[1],usage)))
                elif args[3] in ['-ss','--searchString']:
                    if len(args[2:])<3:
                        raise(SyntaxError('not enough arguments for {} subcommand\n{}'.format(args[1],usage)))
                    else:
                        pdfContent,pdfLimits=extractContent(args[2])
                        pdfContent=delText(pdfContent,oldText=args[4])
                        writeToPdf(args[2],pdfContent,pdfLimits)
                elif args[3] in ['-r','--range']:
                    for parameter in ['pageRangeStart','pageRangeClose','lineRangeStart','lineRangeClose','wordRangeStart','wordRangeClose']:
                        value=input('Enter the {} or leave blanck to skip this parmeter: ')
                    rangeParameters={'page':[],'line':[],'word':[]}
                    for parameter in rangeParameters:
                        try:
                            rangeParameters[parameter].append(int(input('Enter the {} range start or -1 to skip: '.format(parameter))))
                        except:
                            raise(TypeError('Range values has to be integers!'))
                        
                        if rangeParameters[parameter][0]<0:
                            rangeParameters[parameter]=None
                            continue
                        else:
                            rangeParameters[parameter].append(int(input('Enter the {} range end: '.format(parameter))))
                    pdfContent,pdfLimits=extractContent(args[2])
                    pdfContent=delText(pdfContent,pageRange=rangeParameters['page'],lineRange=rangeParameters['line'],wordRange=rangeParameters['word'])
                    writeToPdf(args[2],pdfContent,pdfLimits)
        elif args[1]=='m':
            if len(args[2:])<2:
                raise(SyntaxError('not enough arguments for {} subcommand\n{}'.format(args[1],usage)))
            elif not os.path.exists(args[2]) or not os.path.exists(args[3]):
                raise(FileNotFoundError('at least 2 existing files are required for {} subcommand\n{}'.format(args[1],usage)))
            elif not re.fullmatch('.*\.pdf',args[2]) or not re.fullmatch('.*\.pdf',args[3]):
                raise(TypeError('input file has to be a .pdf!\n{}'.format(usage)))
            else:
                pathList=[]
                for path in args[3:]:
                    if os.path.exists(path):
                        if not re.fullmatch('.*\.pdf',path):
                            print('Warning: {} is not a pdf! It will be ignored.'.format(path))
                        pathList.append(path)
                    else:
                        print('Warning: {} not existing in working directory! It will be ignored.'.format(path))
                mergePdf(args[2],*pathList)
        elif args[1]=='s':
            if len(args[2:])<3 or len(args[3:])%2>0:
                raise(SyntaxError('not enough arguments for {} subcommand\n{}'.format(args[1],usage)))
            elif not os.path.exists(args[2]):
                raise(FileNotFoundError('{}not found in working directory\n{}'.format(args[2],usage)))
            elif not re.fullmatch('.*\.pdf',args[2]):
                raise(TypeError('input file has to be a .pdf!\n{}'.format(usage)))
            else:
                pageRange=[]
                for value in args[3:]:
                    try:
                        pageRange.append(int(value))
                    except:
                        raise(TypeError('Range values has to be integers!'))
                splitPdf(args[2],*pageRange)