'''Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.'''

def somma_elementi(lista1, lista2):
    somma_finale = []  # Lista vuota per raccogliere le somme
    for i in range(len(lista1)):  # Scorri tramite gli indici
        somma = lista1[i] + lista2[i]  # Somma l'elemento corrispondente
        somma_finale.append(somma)  # Aggiungi la somma alla lista
    return somma_finale  # Restituisci la lista con tutte le somme


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(somma_elementi(lista1, lista2))  # Output: [5, 7, 9]
