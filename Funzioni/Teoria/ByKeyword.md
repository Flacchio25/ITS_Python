- Functions with parameters passed by keyword

In Python, i parametri passati per parole chiave (o keyword arguments) sono parametri che vengono specificati
con il loro nome al momento della chiamata della funzione. Questo permette di passare gli argomenti in qualsiasi ordine
e rende il codice più leggibile.

Esempio base: 

def saluto(nome, messaggio="Ciao"):
    print(f"{messaggio}, {nome}!")

# Chiamata con parametri per parole chiave

saluto(nome="Marco", messaggio="Buongiorno")  
saluto(messaggio="Hey", nome="Anna")  # Ordine invertito
saluto(nome="Luca")  # Usa il valore predefinito per "messaggio"


- Functions with default values

In Python, possiamo assegnare valori predefiniti ai parametri di una funzione. Questo significa che se l’utente non fornisce un valore per quel parametro, verrà usato automaticamente il valore predefinito.

def saluto(nome="Utente"):
    print(f"Ciao, {nome}!")
    
saluto()         # Usa il valore predefinito → "Ciao, Utente!"
saluto("Marco")  # Sovrascrive il valore predefinito → "Ciao, Marco!"

- Functions without parameters

In Python, possiamo definire funzioni senza parametri, ovvero funzioni che non richiedono nessun valore in ingresso per essere eseguite. Queste funzioni vengono usate quando l’operazione da svolgere non ha bisogno di informazioni esterne o quando i dati sono già definiti all’interno della funzione stessa.

def saluto():
    print("Ciao! Benvenuto nel programma.")

saluto()  # Chiamata della funzione

Esempio con operazioni matematiche:

def somma():
    a = 5
    b = 3
    risultato = a + b
    print(f"La somma è: {risultato}")

somma()  # Output: La somma è: 8

-Functions calls and execution

In Python, per eseguire una funzione, dobbiamo chiamarla nel codice. La chiamata di una funzione è l'operazione con cui diciamo al programma di eseguire il blocco di istruzioni contenuto nella funzione.

Definizione e chiamata di una funzione

Prima di poter chiamare una funzione, dobbiamo definirla usando la parola chiave def.
Esempio base

def saluta():
    print("Ciao! Benvenuto!")

# Chiamata della funzione
saluta()

🔹 def saluta(): → Definisce la funzione ma non la esegue.
🔹 saluta() → Chiama la funzione e la esegue.
🔹 Output del programma:

Chiamata di una funzione con parametri

Alcune funzioni possono richiedere parametri in ingresso.
Esempio con parametri

def saluta_utente(nome):
    print(f"Ciao, {nome}!")

saluta_utente("Marco")  # Chiamata con il parametro "Marco"
saluta_utente("Anna")   # Chiamata con il parametro "Anna"

🔹 La funzione saluta_utente(nome) accetta un parametro nome.
🔹 Quando chiamiamo saluta_utente("Marco"), il valore "Marco" viene assegnato a nome.

Differenza tra chiamata ed esecuzione

    Definire una funzione significa solo scrivere il suo codice, senza eseguirlo.
    Chiamare una funzione significa dire al programma di eseguire quel codice.


-Functions and args

Le funzioni in Python possono ricevere argomenti (o parametri) per eseguire operazioni su dati specifici.

Se non sappiamo in anticipo quanti argomenti avrà la funzione, possiamo usare *args.

def somma(*numeri):
    totale = sum(numeri)
    print(f"La somma è: {totale}")

somma(1, 2, 3)          # Output: La somma è: 6
somma(10, 20, 30, 40)   # Output: La somma è: 100

*args raccoglie tutti gli argomenti in una tupla e possiamo usarli nel codice.

-Functions and kwargs

Se vogliamo passare un numero variabile di argomenti con nome, usiamo **kwargs.

def info_persona(**dati):
    for chiave, valore in dati.items():
        print(f"{chiave}: {valore}")

info_persona(nome="Marco", eta=25, città="Roma")

**kwargs raccoglie gli argomenti in un dizionario, quindi possiamo accedere a chiavi e valori.
**kwargs = scompone gli elementi in molteplici chiave: valore
- Esempio:
def total_price(**kwargs):
    total:float = 0
    for product, price in kwargs.items():
        print(f"{product}: {price}€")
        total += price
    return round(total, 2)
print(total_price(coffee=2.99, cake=4.55, juice=2.99))

-Built-In Functions
Le funzioni built-in sono funzioni già integrate in python, che possiamo usare senza doverle definire

Alcune delle funzioni base più usate:

● print(): Outputs data to the console.
● len(): Returns the length of an object (e.g., a string or list).
● max(): Returns the largest item in an iterable.
● min(): Returns the smallest item in an iterable.
● sum(): Returns the sum of all items in an iterable.
● abs(): Returns the absolute value of a number.
● round(): Rounds a number to a specified number of decimal places.
● sorted(): Returns a new sorted list from the elements of an iterable.
● range(): Generates a sequence of numbers.