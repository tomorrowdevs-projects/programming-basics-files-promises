import os
import sys
import re
import fpdf

def readData(filePath):
    file=open(filePath)
    header=file.readline().strip().split(',')
    counter=2
    data=[]
    for line in file.readlines()[0:]:
        line=line.strip().split(',')
        if len(line)!=len(header):
            print("Warning: line {} of input data is incomplete and it will be ignored!".format(counter))
        elif not line[0].isnumeric() or not re.fullmatch('\d*\.\d{2}',line[3]) or not line[4].isnumeric() or not re.fullmatch('\d{4}-\d{2}-\d{2}',line[-1]):
            print("Warning: line {} of input data is irregular and it will be ignored!".format(counter))
        else:
            line[0]=int(line[0])
            line[1]=line[1].strip()
            line[2]=line[2].strip()
            line[3]=float(line[3])
            line[4]=int(line[4])
            line[-1]=line[-1].strip()
            data.append(line)
        counter+=1
    return header, data

def orderAnalysis(header,data):
    orderIds=[]
    for line in data:
        if line[header.index('OrderID')] in orderIds:
            continue
        else:
            orderIds.append(header.index('OrderID'))
    ordersNumber=len(orderIds)
    return ordersNumber

def productAnalysis(header,data):
    productDict={}
    for line in data:
        product=line[header.index('Product')]
        if product in productDict:
            productDict[product]['Quantity']+=line[header.index('Quantity')]
            productDict[product]['Price']+=line[header.index('Price')]*line[header.index('Quantity')]
        else:
            productDict[product]={'Quantity':line[header.index('Quantity')],'Price':line[header.index('Price')]}

    for product in productDict:
        productDict[product]['Price']=round(productDict[product]['Price']/productDict[product]['Quantity'],2)

    return productDict    

def categoryAnalysis(header,data):
    categoryDict={}
    for line in data:
        category=line[header.index('Category')]
        price=line[header.index('Price')]
        quantity=line[header.index('Quantity')]
        if category in categoryDict:
            categoryDict[category]['Occurrence']+=quantity
            categoryDict[category]['Price']+=round(price*quantity,2)
        else:
            categoryDict[category]={'Occurrence':quantity,'Price':round(price*quantity,2)}
    return categoryDict

def priceAnalysis(header,data):
    priceList=[]
    for line in data:
        priceList.append(line[header.index('Price')])
    priceStat=[min(priceList),round(sum(priceList)/len(priceList),2),max(priceList)]
    return priceStat

def customerAnalysis(header,data):
    customerDict={}
    for line in data:
        customer=line[header.index('Customer')]
        price=line[header.index('Price')]
        quantity=line[header.index('Quantity')]
        if customer in customerDict:
            customerDict[customer]['Orders']+=1
            customerDict[customer]['Amount']+=round(price*quantity,2)
        else:
            customerDict[customer]={'Orders':1,'Amount':round(price*quantity,2)}
    return customerDict

def generateReport(header,data):
    pdf = fpdf.FPDF('P', 'mm', 'A4')
    pdf.set_font('Arial', '', 16)
    pdf.set_margins(10,25)
    pdf.add_page()
    #Order analysis
    pdf.multi_cell(0,16,'ORDER ANALYSIS\nNumber of orders: {}'.format(orderAnalysis(header,data)))
    
    #Product analysis
    productDict=productAnalysis(header,data)
    productReport='\nPRODUCT ANALYSIS\n'
    for product in productDict:
        productReport=productReport+'{} - Qty: {} - Price: {}\n'.format(product,productDict[product]['Quantity'],productDict[product]['Price'])
    pdf.multi_cell(0,16,productReport)

    #Category analysis
    categoryDict=categoryAnalysis(header,data)
    categoryReport='\nCATEGORY ANALYSIS\n'
    for category in categoryDict:
        categoryReport=categoryReport+'{} - Qty: {} - Revenue: {:.2f}\n'.format(category,categoryDict[category]['Occurrence'],categoryDict[category]['Price'])
    pdf.multi_cell(0,16,categoryReport)

    #Price analysis
    priceStat=priceAnalysis(header,data)
    priceReport='\nPRICE ANALYSIS\n'
    priceReport=priceReport+'minimum price: {} - mean price: {} - max price: {}\n'.format(priceStat[0],priceStat[1],priceStat[2])
    pdf.multi_cell(0,16,priceReport)

    #Customer analysis
    customerDict=customerAnalysis(header,data)
    customerReport='\nCUSTOMER ANALYSIS\n'
    for customer in customerDict:
        customerReport=customerReport+'{} - Orders: {} - Amount: {}\n'.format(customer,customerDict[customer]['Orders'],customerDict[customer]['Amount'])
    pdf.multi_cell(0,16,customerReport)

    pdf.output('report.pdf', 'F')

if __name__=='__main__':
    if not os.path.exists(sys.argv[1]):
        raise(FileNotFoundError('{} not found in working directory'.format(sys.argv[1])))
    elif not re.fullmatch('.*\.csv',sys.argv[1]):
        raise(TypeError('{} is not a csv'.format(sys.argv[1])))
    else:
        header,data=readData(sys.argv[1])
        generateReport(header,data)
