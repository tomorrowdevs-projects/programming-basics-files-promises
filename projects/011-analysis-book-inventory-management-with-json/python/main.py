import json

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Errore: File non trovato.")
        return None

def calculate_average_rating(data):
    ratings = [book['rating'] for book in data]
    average = sum(ratings) / len(ratings)
    print(f"Media dei voti: {average:.2f}")

def calculate_oldest_and_newest_books(data):
    try:
        books_with_year = [book for book in data if 'publication_year' in book]
        if not books_with_year:
            print("Nessun libro con l'anno di pubblicazione disponibile.")
            return
        
        oldest = min(books_with_year, key=lambda x: x['publication_year'])
        newest = max(books_with_year, key=lambda x: x['publication_year'])
        
        print(f"Libro più vecchio: '{oldest['title']}' di {oldest['author']} ({oldest['publication_year']})")
        print(f"Libro più recente: '{newest['title']}' di {newest['author']} ({newest['publication_year']})")
    except Exception as e:
        print(f"Errore durante il calcolo: {e}")


def calculate_genre_distribution(data):
    genres = {}
    for book in data:
        genre = book['genre']
        genres[genre] = genres.get(genre, 0) + 1
    for genre, count in genres.items():
        print(f"{genre}: {count} libri")

def calculate_highly_rated_books(data):
    print("Libri con voti >= 4.5:")
    for book in data:
        if book['rating'] >= 4.5:
            print(f"{book['title']} di {book['author']}")

def calculate_top_rated_book(data):
    top_book = max(data, key=lambda x: x['rating'])
    print(f"Libro con voto più alto: {top_book['title']} di {top_book['author']} ({top_book['rating']})")

def calculate_genre_average_rating(data):
    genre_ratings = {}
    for book in data:
        genre = book['genre']
        genre_ratings.setdefault(genre, []).append(book['rating'])
    for genre, ratings in genre_ratings.items():
        average = sum(ratings) / len(ratings)
        print(f"Media dei voti per {genre}: {average:.2f}")

def book_recommendation(data):
    favorite_genre = input("Inserisci il tuo genere preferito: ")
    year = int(input("Inserisci un anno: "))
    print("Libri consigliati:")
    for book in data:
        if book['genre'] == favorite_genre and book['rating'] > 4.0 and book['year'] >= year:
            print(f"{book['title']} di {book['author']} ({book['year']})")

def main():
    data = read_json_file("projects/011-analysis-book-inventory-management-with-json/python/books.json")
    if data is None:
        return

    while True:
        print("\nScegli un'operazione:")
        print("1. Calcola media dei voti")
        print("2. Trova libro più vecchio e più recente")
        print("3. Conta libri per genere")
        print("4. Trova libri con voti >= 4.5")
        print("5. Trova libro con voto più alto")
        print("6. Calcola media dei voti per genere")
        print("7. Consiglia un libro")
        print("8. Esci")

        scelta = input("Inserisci il numero dell'operazione: ")

        if scelta == '1':
            calculate_average_rating(data)
        elif scelta == '2':
            calculate_oldest_and_newest_books(data)
        elif scelta == '3':
            calculate_genre_distribution(data)
        elif scelta == '4':
            calculate_highly_rated_books(data)
        elif scelta == '5':
            calculate_top_rated_book(data)
        elif scelta == '6':
            calculate_genre_average_rating(data)
        elif scelta == '7':
            book_recommendation(data)
        elif scelta == '8':
            print("Uscita...")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()