'''Ecco 7 esercizi con difficoltà crescente per allenarti con if, elif ed else.'''

'''1. Classificazione della temperatura

Scrivi un programma che assegni un valore a temperature e classifichi il clima:

    Meno di 0°C: "Fa molto freddo!"
    Da 0 a 15°C: "Fa fresco."
    Da 15 a 25°C: "La temperatura è piacevole."
    Oltre 25°C: "Fa caldo!"'''

temperatura = 8

if temperatura < 0:
    print("Fa molto freddo!")
elif 0 <= temperatura <15:
    print("Fa fresco")
elif 15 <= temperatura <25:
    print("la temperatura è piacevole")
else:  
    print("Fa caldo!")


'''2. Classificazione dell’orario della giornata

Imposta un valore per hour (tra 0 e 23) e stampa:

    Da 0 a 5: "Notte fonda."
    Da 6 a 11: "Buongiorno!"
    Da 12 a 17: "Buon pomeriggio!"
    Da 18 a 21: "Buona sera!"
    Da 22 a 23: "Buona notte!"'''

orario = 17

if 0 <= orario < 6:
    print("Notte fonda")
elif 6 <= orario < 12:
    print("Buongiorno!")
elif 12 <= orario < 18:
    print("Buon pomeriggio!")
elif 18 <= orario < 22:
    print("Buona serata!")
else:
    print("Buona notte!")

