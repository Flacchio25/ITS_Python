Lezione spiegazione Funzioni

Suppose that you need to find the sum of integers from 1 to 10, 20 to 37, and 35 to 49. Write a Python program that
compute these three different sums.

sum1= 0
sum2= 0
sum3= 0

for i in range(1,10):
    sum1 +=i
for i in range(20,37):
    sum2 +=i
for i in range(35,49):
    sum3 +=i
    
print(f"{sum1}\n{sum2}\n{sum3}")


Analisi del codice che hai fornito :

Ecco una versione corretta e ben formattata della funzione:

def functionName(a: int, b: int) -> int:
    sum = 0
    for i in range(a, b + 1):
        sum = sum + i
    return sum

Ora spieghiamo il codice riga per riga:
1. Definizione della funzione

def functionName(a: int, b: int) -> int:

    def indica che stiamo definendo una funzione.

    functionName è il nome della funzione (può essere qualsiasi nome significativo).
    
    (a: int, b: int) sono parametri: a e b sono numeri interi (int).
    
    -> int è un'annotazione di tipo opzionale, che indica che la funzione restituirà un valore intero.

2. Inizializzazione della variabile sum

sum = 0

    Creiamo una variabile sum per memorizzare la somma dei numeri nell'intervallo.

3. Ciclo for per sommare tutti i numeri da a a b

for i in range(a, b + 1):
    sum = sum + i

    range(a, b + 1): genera una sequenza di numeri da a a b (incluso).
    sum = sum + i: aggiorna la somma aggiungendo il valore corrente i.

4. Restituzione del risultato

return sum

    Restituisce la somma totale calcolata.

Esempio di utilizzo della funzione

Ora proviamo a chiamare la funzione con dei valori:

result = functionName(1, 5)
print(result)  # Output: 15

Cosa succede?

    functionName(1, 5) somma tutti i numeri da 1 a 5:

    1 + 2 + 3 + 4 + 5 = 15

    La funzione restituisce 15, che viene memorizzato in result.
    print(result) stampa 15.

Perché usare le funzioni?

✅ Riutilizzabilità: Una volta definita, possiamo chiamarla più volte con diversi valori.
✅ Modularità: Il codice diventa più leggibile e organizzato.
✅ Facilità di manutenzione: Se dobbiamo modificare il comportamento della funzione, possiamo farlo in un solo posto.


User-Defined Functions
