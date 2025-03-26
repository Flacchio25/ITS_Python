'''Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
ritorni un nuovo insieme senza i numeri specificati nella lista.'''

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    set1 = original_set.copy()
    for e in elements_to_remove:
        if e in original_set:
            set1.remove(e)
    return set1

print(remove_elements({5, 6, 7}, [7, 8, 9]))