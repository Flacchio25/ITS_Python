'''Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, dove n è la lunghezza della lista.
Tuttavia, alcuni numeri potrebbero mancare: la lista può contenere duplicati, ma non tutti i numeri da 1 a n sono presenti.
Il tuo compito è individuare i numeri mancanti.
Scrivi una funzione che, data in input una lista,restituisca una nuova lista ordinata contenente tutti i numeri da 1 a n
che non sono presenti nella lista originale.'''

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    n = len(nums)
    tutti_i_numeri = set(range(1, n + 1))
    numeri_presenti = set(nums)
    numeri_mancanti = tutti_i_numeri.difference(numeri_presenti)
    return list(numeri_mancanti)


nums = [52,48,49,51,50,54,53,53]
print(find_disappeared_numbers(nums))  