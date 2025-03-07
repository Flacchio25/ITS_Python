#leggi un intero a quattro cifre
numero = int(input("Inserisci un numero intero di quattro cifre: "))

#Bisogna convertire il numero in una stringa per poter accedere a ciascuna cifra
numero_str = str(numero)

for cifra in numero_str:
    print(cifra)