# Definizione delle categorie
mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci = ["squalo", "trota", "salmone", "carpa"]

# Categorie di habitat
habitat_validi = {"acqua", "aria", "terra"}

distribuzione_habitat = {
    "cane": "terra", "gatto": "terra", "cavallo": "terra", "elefante": "terra", "leone": "terra", 
    "balena": "acqua", "delfino": "acqua", "serpente": "terra", "lucertola": "terra", "tartaruga": "terra", "coccodrillo": "acqua",
    "aquila": "aria", "pappagallo": "aria", "gufo": "aria", "falco": "aria", "cigno": "acqua", "anatra": "acqua", "gallina": "terra", "tacchino": "terra", 
    "squalo": "acqua", "trota": "acqua", "salmone": "acqua", "carpa": "acqua"
}

# Input utente
animale = input("Inserisci il nome di un animale: ").strip().lower() # .strip() rimuove eventuali spazi all'inizio o alla fine dell'input.
habitat = input("Inserisci un habitat (acqua, aria, terra): ").strip().lower() #.lower() converte il testo in minuscolo per evitare problemi con lettere maiuscole.

# Classificazione con match statement
animal_type = "unknown"
match animale:
    case _ if animale in mammiferi:
        animal_type = "mammifero"
    case _ if animale in rettili:
        animal_type = "rettile"
    case _ if animale in uccelli:
        animal_type = "uccello"
    case _ if animale in pesci:
        animal_type = "pesce"

# Creazione del dizionario
animale_info = {"nome": animale, "categoria": animal_type, "habitat": habitat}

# Verifica della compatibilità dell'habitat
if animal_type == "unknown" or habitat not in habitat_validi:
    print("Errore: animale o habitat non riconosciuti.")
elif animale in distribuzione_habitat and habitat == distribuzione_habitat[animale]:
    print(f"{animale.capitalize()} ({animal_type}) può vivere in {habitat}.")
elif animale in distribuzione_habitat and habitat != distribuzione_habitat[animale]:
    print(f"Attenzione: {animale.capitalize()} ({animal_type}) non può vivere in {habitat}.")
else:
    print("Non sono in grado di determinare la compatibilità dell'habitat.")
