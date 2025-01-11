import csv

def load_csv(filename):
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        print("Errore: File non trovato.")
        return None

def view_data(data):
    for row in data:
        print("\t".join(row))

def add_row(data):
    new_row = input("Inserisci i valori separati da virgola per la nuova riga: ").split(',')
    data.append(new_row)

def add_column(data):
    col_name = input("Inserisci il nome della nuova colonna: ")
    if data:
        data[0].append(col_name)
        for row in data[1:]:
            row.append(input(f"Valore per la nuova colonna nella riga {data.index(row)}: "))

def edit_data(data):
    try:
        row_idx = int(input("Indice della riga da modificare (0 per la prima riga): "))
        col_idx = int(input("Indice della colonna da modificare (0 per la prima colonna): "))
        new_value = input("Inserisci il nuovo valore: ")
        data[row_idx][col_idx] = new_value
    except (IndexError, ValueError):
        print("Errore: Indice non valido.")

def delete_row(data):
    try:
        row_idx = int(input("Indice della riga da eliminare (0 per la prima riga): "))
        data.pop(row_idx)
    except (IndexError, ValueError):
        print("Errore: Indice non valido.")

def delete_column(data):
    try:
        col_idx = int(input("Indice della colonna da eliminare (0 per la prima colonna): "))
        for row in data:
            row.pop(col_idx)
    except (IndexError, ValueError):
        print("Errore: Indice non valido.")

def sort_data(data):
    try:
        col_idx = int(input("Indice della colonna per ordinare (0 per la prima colonna): "))
        header, rows = data[0], data[1:]
        rows.sort(key=lambda x: x[col_idx])
        data[1:] = rows
    except (IndexError, ValueError):
        print("Errore: Indice non valido.")

def filter_data(data):
    try:
        col_idx = int(input("Indice della colonna per filtrare (0 per la prima colonna): "))
        value = input("Inserisci il valore da filtrare: ")
        header, rows = data[0], data[1:]
        filtered_rows = [row for row in rows if row[col_idx] == value]
        print("\nDati filtrati:")
        view_data([header] + filtered_rows)
    except (IndexError, ValueError):
        print("Errore: Indice non valido.")

def save_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def main():
    data = load_csv("projects/010-command-line-csv-file-editor/python/example.csv")

    if data is None:
        return

    while True:
        print("\nScegli un'operazione:")
        print("1. Visualizza dati")
        print("2. Aggiungi riga")
        print("3. Aggiungi colonna")
        print("4. Modifica dati")
        print("5. Elimina riga")
        print("6. Elimina colonna")
        print("7. Ordina dati")
        print("8. Filtra dati")
        print("9. Salva e uscire")

        scelta = input("Inserisci il numero dell'operazione: ")

        if scelta == '1':
            view_data(data)
        elif scelta == '2':
            add_row(data)
        elif scelta == '3':
            add_column(data)
        elif scelta == '4':
            edit_data(data)
        elif scelta == '5':
            delete_row(data)
        elif scelta == '6':
            delete_column(data)
        elif scelta == '7':
            sort_data(data)
        elif scelta == '8':
            filter_data(data)
        elif scelta == '9':
            save_csv(data)
            print("Modifiche salvate. Uscita...")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()