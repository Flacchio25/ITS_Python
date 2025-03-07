'''Let’s try to define a function named subtract ourselves:
● It should take 2 parameters.
● Inside the function, it should subtract the two.
● Then, return the result'''


def subtract(a, b):
    return a - b

result = subtract(10, 5)
print(result)






















'''🔹 Livello 1: Facili
1️⃣ Funzione Somma

Scrivi una funzione che accetti due numeri come parametri e restituisca la loro somma.'''

def sum(a: int, b: int):
    sum: int = 0
    for i in range (a, b+1) :
        sum = sum + i 
    return sum

result_sum = sum(5, 15)
print(f"Sum from 5 to 15 is {sum(5,15)}")


'''2️⃣ Funzione Pari o Dispari

Scrivi una funzione che accetti un numero intero e restituisca "Pari" se il numero è pari, altrimenti "Dispari".'''

def pari_o_dispari(numero):
    if numero % 2 == 0:
        return "Pari"
    else:
        return "Dispari"

risultato = pari_o_dispari(7)
print(risultato) 

'''3️⃣ Funzione Saluto Personalizzato

Scrivi una funzione che accetti un nome come parametro e stampi un saluto del tipo "Ciao, [nome]!".'''

def saluto(nome):
    print(f"Ciao, {nome}!")

saluto("Mirko")


'''4️⃣ Funzione per Calcolare il Fattoriale

Scrivi una funzione che calcoli il fattoriale di un numero intero positivo. Il fattoriale di n (n!) è il prodotto di tutti i numeri da 1 a n.'''

def fattoriale(n):
    if n == 0 or n == 1:
        return 1
    else:
        risultato = 1
        for i in range(2, n + 1):
            risultato *= i
        return risultato

risultato = fattoriale(5)
print(risultato)


'''5️⃣ Contare le Vocali in una Stringa

Scrivi una funzione che accetti una stringa e restituisca il numero di vocali (a, e, i, o, u) presenti.'''

def count_vocals(s):
    vocals = ["a", "e", "i", "o", "u"]
    risultato = 0
    for lettera in s:
        if lettera.lower() in vocals:
            risultato += 1

    return risultato

print(count_vocals("Il sommo DUCE è stato l'ultimo grande dittatore italico"))
