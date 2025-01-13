import json

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Errore: Il file '{filename}' non è stato trovato. Creazione di un nuovo file...")
        with open(filename, 'w') as file:
            json.dump([], file)
        return []
    except json.JSONDecodeError:
        print("Errore: Il file JSON non è valido.")
        return []

def accessing_data(data):
    book_title = input("Inserisci il titolo del libro: ")
    book = next((b for b in data if b['title'].lower() == book_title.lower()), None)
    if book:
        print("\nInformazioni sul libro:")
        for key, value in book.items():
            print(f"{key.capitalize()}: {value}")
        
        same_genre_books = [b['title'] for b in data if b['genre'] == book['genre'] and b['title'] != book['title']]
        if same_genre_books:
            print("\nSuggerimenti di altri libri nello stesso genere:")
            for title in same_genre_books:
                print(f"- {title}")
        else:
            print("\nNon ci sono altri libri di questo genere.")
    else:
        print("Errore: Libro non trovato.")

def update_price(data):
    book_title = input("Inserisci il titolo del libro da aggiornare: ")
    book = next((b for b in data if b['title'].lower() == book_title.lower()), None)
    if book:
        try:
            new_price = float(input(f"Inserisci il nuovo prezzo per '{book['title']}': "))
            book['price'] = new_price
            print(f"Prezzo aggiornato! Il nuovo prezzo di '{book['title']}' è {new_price:.2f}€.")
        except ValueError:
            print("Errore: Il prezzo deve essere un numero.")
    else:
        print("Errore: Libro non trovato.")

def add_book(data):
    print("Inserisci i dettagli del nuovo libro:")
    title = input("Titolo: ")
    author = input("Autore: ")
    try:
        year = int(input("Anno di pubblicazione: "))
        genre = input("Genere: ")
        rating = float(input("Valutazione (da 0 a 5): "))
        price = float(input("Prezzo: "))
        new_book = {
            "title": title,
            "author": author,
            "publication_year": year,
            "genre": genre,
            "rating": rating,
            "price": price
        }
        data.append(new_book)
        print(f"Libro '{title}' aggiunto con successo!")
    except ValueError:
        print("Errore: Assicurati che anno, valutazione e prezzo siano numeri validi.")

def main():
    books = read_json_file("books.json")
    if not books:
        return

    while True:
        print("\nScegli un'operazione:")
        print("1. Visualizza informazioni su un libro")
        print("2. Aggiorna il prezzo di un libro")
        print("3. Aggiungi un nuovo libro")
        print("4. Esci")
        
        choice = input("Inserisci il numero dell'operazione: ")
        if choice == "1":
            accessing_data(books)
        elif choice == "2":
            update_price(books)
        elif choice == "3":
            add_book(books)
        elif choice == "4":
            try:
                with open("books.json", 'w') as file:
                    json.dump(books, file, indent=4)
                print("Modifiche salvate. Uscita...")
            except Exception as e:
                print(f"Errore durante il salvataggio del file: {e}")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()