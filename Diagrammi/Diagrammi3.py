'''3. Progettare un algoritmo che calcoli la somma dei soli numeri positivi tra 5 valori inseriti dall'utente.
Quindi, se un numero è negativo o zero, ignora quel valore nella somma.'''

somma = 0  # Inizializziamo la somma a 0

for i in range(5):  # Chiediamo 5 numeri
    num = float(input(f"Inserisci il numero {i + 1}: "))
    
    if num > 0:  # Se il numero è positivo
        somma += num  # Aggiungiamo il numero alla somma

print(f"La somma dei numeri positivi è: {somma}")


'''tre esercizi simili per aiutarti a esercitarti:

Esercizio 1: Somma dei numeri pari
Scrivi un algoritmo che calcoli la somma dei numeri pari tra 6 valori inseriti dall'utente. Se il numero è dispari o negativo, ignora quel valore nella somma.'''

somma = 0

for i in range(6):
    num = float(input(f"Inserisci il numero {i+1}: "))  # Aggiunta dello spazio tra {i+1} per migliorare la leggibilità

    if num % 2 == 0:  # Controlliamo se il numero è pari
        somma += num  # Sommiamo il numero se è pari

print(f"La somma dei numeri pari è: {somma}")


'''Esercizio 2: Somma dei numeri maggiori di 10
Scrivi un algoritmo che calcoli la somma dei numeri maggiore di 10 tra 4 valori inseriti dall'utente.
Se il numero è minore o uguale a 10, ignora quel valore nella somma.'''

somma = 0

for i in range(4):
    num = float(input(f"Inserisci il numero {i+1}: "))

    if num > 10:
        somma+=num

print(f"La somma dei numeri maggiori di 10 è: {somma}")


'''Esercizio 3: Somma dei numeri divisibili per 3
Scrivi un algoritmo che calcoli la somma dei numeri divisibili per 3 tra 7 valori inseriti dall'utente. Se un numero non è divisibile per 3, ignoralo nella somma.
'''

somma = 0

for i in range(7):
    num = float(input(f"Inserisci il numero {i+1}: "))

    if num % 3 == 0:  # Verifica se il numero è divisibile per 3
        somma += num  # Somma il numero se è divisibile per 3

print(f"La somma dei numeri divisibili per 3 è: {somma}")




