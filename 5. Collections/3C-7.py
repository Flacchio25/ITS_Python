'''Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.'''
# Input utente
num_lanci = 8
teste = 0 
croci = 0

for i in range(num_lanci):#ciclo for per ripetere l'input dell'utente per 8 volte
        lancio = input(f"Inserisci il risultato del lancio {i+1} (T/t per Testa, C/c per Croce): ").strip().lower() #.strip() rimuove eventuali spazi all'inizio o alla fine dell'input.
        
        match lancio:
            case "t":
                teste += 1
            case "c":
                croci += 1
            case _:
                print("Input non valido. Riprova.")
            
    
percentuale_teste = (teste / num_lanci) * 100
percentuale_croci = (croci / num_lanci) * 100
    
print(f"Risultati:")
print(f"Testa: {teste} ({percentuale_teste:.2f}%)")     
print(f"Croce: {croci} ({percentuale_croci:.2f}%)")
