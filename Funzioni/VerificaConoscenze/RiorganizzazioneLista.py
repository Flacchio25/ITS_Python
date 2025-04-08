'''Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:

    tutti i numeri pari vengano prima di tutti i numeri dispari;

    l’ordine relativo tra pari e dispari va mantenuto;

    l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi.
'''

def even_odd_pattern(numbers:list[int]) -> list[int]:
    pari = []
    dispari = []
    for num in numbers:
        if num % 2 == 0:
            pari.append(num)
        else:
            dispari.append(num)
    return pari + dispari

print(even_odd_pattern([1, 2, 3, 4, 5])) 
print(even_odd_pattern([7, 8, 9, 10]))   
print(even_odd_pattern([4, 3, 2, 1]))   
