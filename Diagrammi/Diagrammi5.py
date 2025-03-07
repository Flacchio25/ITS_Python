'''5. Verifica se un numero è primo

Progetta un algoritmo per determinare se un numero intero positivo inserito dall'utente è un numero primo.'''

numero = int(input("Inserisci un numero intero positivo: "))


if numero <= 1:
    print(f"{numero} non è un numero primo.")
elif numero == 2:
    print(f"{numero} è un numero primo.")
else:
    primo = True 
    for i in range(2, int(numero**0.5) + 1):  
        if numero % i == 0: 
            primo = False 
            break
    
    if primo:
        print(f"{numero} è un numero primo.")
    else:
        print(f"{numero} non è un numero primo.")
