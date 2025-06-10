
import json

PATH: str = "Lezione15/config.json"
mode: str = "r"

with open(PATH, mode=mode) as file:

    config: dict = json.load(file)

    print(config)

    nome_applicazione: str = config("appName")

    print(nome_applicazione)



PATH: str= "Lezione15/config.json"
mode: str = "w"

with open(PATH, mode = mode) as file:
    config: dict = {
        "nome": "2048"
        "versione": "1.1.42"
        "OS": "android 16.1.0"
    }

json. dump(config, file)



#crea un file json usando i comandi touch, e nano e leggete il file
#appena creato e stampate il valore

#crea un file json da python salvando un dizionario a vostra scelta

#crea un file json che contiene codici fiscali come chiavi e come valori 
#dei dizionari che contengono nome e cognome ed età della persona e poi
#modificate il file json aggiungiendo una persona 