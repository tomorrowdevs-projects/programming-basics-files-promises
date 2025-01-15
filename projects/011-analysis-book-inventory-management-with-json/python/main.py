import json
import os
import random

def readJson(filePath):
    if os.path.exists(filePath):
        with open("books.json", mode="r", encoding="utf-8") as read_file:
            jsonData = json.load(read_file)
        return jsonData
    else:
        raise(FileExistsError("{} doesn't exist in current directory!".format(filePath)))

def averageRating(data):
    rating=0
    for book in data:
        rating+=book['rating']
    rating=round(rating/len(data),2)
    print('Average rating: {}'.format(rating))

def yearAnalysis(data):
    yearList=[]
    for book in data:
        yearList.append(book['publication_year'])
    minYear=min(yearList)
    maxYear=max(yearList)
    oldestBooksData=[]
    newestBooksData=[]
    for book in data:
        if book['publication_year']==minYear:
            oldestBooksData.append({'title':book['title'],'author':book['author'],'publication_year':book['publication_year']})
        elif book['publication_year']==maxYear:
            newestBooksData.append({'title':book['title'],'author':book['author'],'publication_year':book['publication_year']})
    
    print("Here's the list of the oldest books:")
    for book in oldestBooksData:
        print('Title: {}\nAuthor: {}\nPublication year: {}'.format(book['title'],book['author'],book['publication_year']))

    print("Here's the list of the newest books:")
    for book in newestBooksData:
        print('Title: {}\nAuthor: {}\nPublication year: {}'.format(book['title'],book['author'],book['publication_year']))
    
def genreAnalysis(data):
    genreList=[]
    for book in data:
        genreList.append(book['genre'])
    
    genreAnalysis={}
    for genre in genreList:
        genreAnalysis[genre]=0
        for book in data:
            if genre==book['genre']:
                genreAnalysis[genre]+=1
    
    print("Here's the genre analysis")
    for genre in genreAnalysis:
        print('{}: {}'.format(genre,genreAnalysis[genre]))

def highlyRatedBooks(data):
    for book in data:
        if book['rating']>=4.5:
            print('Title: {} - Author: {}'.format(book['title'],book['author']))

def highestRatedBooks(data):
    ratingList=[]
    for book in data:
        ratingList.append(book['rating'])
    maxRating=max(ratingList)
    print("Here's the list of books with the maximum rating")
    for book in data:
        if book['rating']==maxRating:
            print('Title: {} - Author: {}'.format(book['title'],book['author']))

def averegeGenreRating(data):
    genreRatingAnalysis={}
    for book in data:
        if not book['genre'] in genreRatingAnalysis:
            genreRatingAnalysis[book['genre']]={'ratingSum':book['rating'],'bookCounter':1}
        else:
            genreRatingAnalysis[book['genre']]['ratingSum']+=book['rating']
            genreRatingAnalysis[book['genre']]['bookCounter']+=1
    
    print("Here's the book genre rating analysis:")
    for genre in genreRatingAnalysis:
        print('{}: {}'.format(genre,round(genreRatingAnalysis[genre]['ratingSum']/genreRatingAnalysis[genre]['bookCounter'],2)))

def bookRecommendation(data):
    option=input("Possible operations:\n- book recomendation [1]\n- book published after a certain year [2]\nPlease enter the number of the operation you want to perform: ")
    while not option in ['1','2']:
        option=input('Unwknow operation! Please, retry: ')
    
    if option=='1':
        genreList=[]
        for book in data:
            genreList.append(book['genre'])
        favouriteGenre=input('Enter your favourite genre: ')
        if not favouriteGenre in genreList:
            print('No books of this genre available!')
        else:
            bookList=[]
            for book in data:
                if book['rating']>4.0 and book['genre']==favouriteGenre:
                    bookList.append(book['title'])
            index=random.randint(0,len(bookList))
            print("We recomend you '{}'".format(bookList[index]))
    else:
        yearList=[]
        for book in data:
            yearList.append(book['publication_year'])
        year=input('Enter the desired year: ')
        while not year.isdigit():
            year=input('Only numerical values: ')
        year=int(year)
        
        if year>max(yearList):
            year=input('No books after your year')
        else:
            bookTitles=[]
            bookAuthors=[]
            for book in data:
                if book['publication_year']>year:
                    bookTitles.append(book['title'])
                    bookAuthors.append(book['author'])
        print("Here's the list of the books published after the desired year:")
        for i in range(len(bookTitles)):
            print('Title: {} - Author: {}'.format(bookTitles[i],bookAuthors[i]))

if __name__=='__main__':
    option=input("Please enter the number of the operation you want to perform: ")
    while not option in ['1','2','3','4','5','6','7']:
        option=input('Unwknow operation! Please, retry: ')
    
    data=readJson('books.json')
    if option=='1':
        averageRating(data)
    elif option=='2':
        yearAnalysis(data)
    elif option=='3':
        genreAnalysis(data)
    elif option=='4':
        highlyRatedBooks(data)
    elif option=='5':
        highestRatedBooks(data)
    elif option=='6':
        averegeGenreRating(data)
    else:
        bookRecommendation(data)
