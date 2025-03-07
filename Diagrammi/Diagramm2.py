'''Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente.'''


max_num = float(input("Inserisci il numero 1: "))  # Il primo numero diventa il massimo iniziale

for i in range(3):  # Ripetiamo il ciclo solo per i restanti 3 numeri
    num = float(input(f"Inserisci il numero {i + 2}: "))
    
    if num > max_num:  # Se il numero è maggiore del massimo attuale, lo aggiorniamo
        max_num = num

print(f"Il numero massimo è: {max_num}")
