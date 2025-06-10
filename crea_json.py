import json

dati = {
"corso": "AnalisiDati",
"studenti": 19,
"attivo": True,
"moduli": ["Python","AI","Python4"]
}

with open("corso.json", "w") as file:
	json.dump(dati, file, indent=4)
