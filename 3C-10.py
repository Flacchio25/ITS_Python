'''Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica)
Salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data.'''


# l'utente inserisce la data
giorno = int(input("Inserisci il giorno: "))
mese = int(input("Inserisci il mese: "))
data = (giorno, mese) #creazione della tupla con i dati inseriti dall'utente

match data:
    case (1,1):
        print("Capodanno")
    case (14,2):
        print("San Valentino")
    case (2,6):
        print("Festa della Repubblica Italiana") 
    case (15,8):
        print("Ferragosto")
    case (31,10):
        print("Halloween")
    case (25,12):
        print("Natale")
    case _:
        print("Nessuna festività importante in questa data.")