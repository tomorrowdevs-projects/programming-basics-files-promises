import os

def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):
    name = input("Inserisci il nome dell'attività: ")
    description = input("Inserisci la descrizione dell'attività: ")
    priority = input("Inserisci la priorità (Alta/Media/Bassa): ")
    due_date = input("Inserisci la data di scadenza (es. 2025-01-30): ")
    task = f"{name} | {description} | {priority} | {due_date} | Incompleta"
    tasks.append(task)
    print("Attività aggiunta con successo!")

def show_tasks(tasks):
    if not tasks:
        print("Non ci sono attività.")
        return
    print("\nElenco delle attività:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nInserisci il numero dell'attività da completare: ")) - 1
        if 0 <= task_num < len(tasks):
            task_parts = tasks[task_num].split(" | ")
            task_parts[-1] = "Completa"
            tasks[task_num] = " | ".join(task_parts)
            print("Attività completata con successo!")
        else:
            print("Numero attività non valido.")
    except ValueError:
        print("Errore: Inserisci un numero valido.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nInserisci il numero dell'attività da eliminare: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            print("Attività eliminata con successo!")
        else:
            print("Numero attività non valido.")
    except ValueError:
        print("Errore: Inserisci un numero valido.")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)
    
    while True:
        print("\n--- Gestione Attività ---")
        print("1. Visualizza attività")
        print("2. Aggiungi attività")
        print("3. Completa attività")
        print("4. Elimina attività")
        print("5. Esci")
        choice = input("Scegli un'opzione: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(filename, tasks)
            print("Attività salvate. Uscita...")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
