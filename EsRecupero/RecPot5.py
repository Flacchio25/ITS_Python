import random 
from typing import List

def genera(dim: int)-> List[List[int]]:
    matrice :List[List[int]] = []
    #ciclo esterno per le righe
    for riga_idx in range(dim):
        riga_corrente: List[int] = [] # lista vuota per la riga corrente

        #generazione primo elemento della riga( colonna 0)
        primo_elemento_riga = random.randint(0,13)
        riga_corrente.append(primo_elemento_riga)

        #Ciclo interno per le altre colonne(1 a dim-1)
        for col_idx in range(1, dim): #parte da range 1 a dim-1
            elemento_generato = random.randint(0,13)

            #Vincolo: l'elemento generato deve essere diverso dal primo elemento della riga
            while elemento_generato == primo_elemento_riga:
                elemento_generato = random.randint(0,13)

            riga_corrente.append(elemento_generato)
        
        matrice.append(riga_corrente)
    return matrice

if __name__ == "__main__":
    print("--- Test: Matrice 3x3 ---")
    matrice_test_3x3 = genera(3)
    for riga in matrice_test_3x3:
        print(riga)
    print("\n")

    print("Verifica manuale del vincolo (es. 3x3):")
    for riga in matrice_test_3x3:
        if len(riga) > 0:
            first_element = riga[0]
            # Controlla se tutti gli elementi successivi sono diversi dal primo
            all_others_different = all(el != first_element for el in riga[1:])
            print(f"Riga: {riga}, Primo elemento: {first_element}, Tutti gli altri diversi: {all_others_different}")


