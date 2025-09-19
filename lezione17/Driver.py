# Creazione dottori
Alessio = Dottore("Chirurgia", 100.0)
Alessio.setName("Alessio")
Alessio.setLastName("Natale")
Alessio.setAge(31)

Filippo = Dottore("Pediatria", 80.0)
Filippo.setName("Filippo")
Filippo.setLastName("Battisti")
Filippo.setAge(32)

# Creazione pazienti
lista1 = [
    Paziente("Mattia", "Canu", 24, "017a"),
    Paziente("Francesco", "Rossi", 25, "018a"),
    Paziente("Marco", "Pini", 27, "019a")
]
lista2 = [Paziente("Giovanni", "Poni", 24, "020a")]

# Presentazione dottori
Alessio.doctorGreet()
Filippo.doctorGreet()

# Creazione fatture
fattura1 = Fattura(lista1, Alessio)
fattura2 = Fattura(lista2, Filippo)

# Stampa salari
salario1 = fattura1.getSalary()
salario2 = fattura2.getSalary()

print(f"Salario Dottore1: {salario1} euro!")
print(f"Salario Dottore2: {salario2} euro!")

# Rimuovo paziente con ID "017a" da fattura1
fattura1.removePatient("017a")

# Recupero il paziente rimosso dalla lista originale (in realtà serve tenerlo da qualche parte)
# Qui ipotizzo che tu abbia accesso alla lista pazienti originale:
paziente_spostato = None
for paz in lista1:
    if paz.getidCode() == "017a":
        paziente_spostato = paz
        break

# Aggiungo paziente a fattura2
if paziente_spostato is not None:
    fattura2.addPatient(paziente_spostato)
else:
    print("Paziente non trovato nella lista1")

#Stampare i salari aggiornati dopo lo spostamento
salario1 = fattura1.getSalary()
salario2 = fattura2.getSalary()

print(f"Salario Dottore1 aggiornato: {salario1} euro!")
print(f"Salario Dottore2 aggiornato: {salario2} euro!")

#Calcolare il guadagno totale incassato dall’ospedale
guadagno_totale = salario1 + salario2
print(f"In totale, l'ospedale ha incassato: {guadagno_totale} euro!")

