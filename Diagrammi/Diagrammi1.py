'''Progetta un algoritmo per ottenere la misura di un cateto c in un triangolo rettangolo, conoscendo quelle dell’ipotenusa a e dell’altro cateto b.'''
#Senza ciclo ne funzione

a = float(input("Inserisci la lunghezza dell'ipotenusa: "))
b = float(input("Inserisci la lunghezza di un cateto: "))

if a > b:
    c = (a**2 - b**2) ** 0.5  # Calcolo della radice quadrata
    print(f"Il valore del cateto è: {c:.2f}")
else:
    print("Errore: l'ipotenusa deve essere maggiore del cateto.")


#Utilizzo funzioni

def calcola_cateto(a, b):
    return (a**2 - b**2) ** 0.5  # Radice quadrata

while True:
    try:
        a = float(input("Inserisci la lunghezza dell'ipotenusa: "))
        b = float(input("Inserisci la lunghezza di un cateto: "))

        if a > b:
            c = calcola_cateto(a, b)
            print(f"Il valore del cateto è: {c:.2f}")
            break  # Esce dal ciclo dopo un calcolo valido
        else:
            print("Errore: l'ipotenusa deve essere maggiore del cateto. Riprova.")

    except ValueError: #ValuerError evita che il programma crasha in caso si inserisce valore non valido tipo lettere
        print("Errore: inserisci numeri validi.")
