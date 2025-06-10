import json

with open("dati.json", "r") as file:
    dati = json.load(file)


print(dati["utente"]["nome"])
