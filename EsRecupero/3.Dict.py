'''3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali'''

dict_5: dict = {"pallone": 34.5, "Samsung": 220.5, "HP": 3245.67}

def dict_prezzi(dict_1:dict) -> dict:

    dict_4: dict= {}

    for key, value in dict_1.items():
        if value > 50:
            
            continue #l'azione da qui in poi viene ignorata e si passa direttamente alla prossima

        else:
            dict_4[key] = round(value + value * 0.10, 2)

    return dict_4

dict_out: dict = dict_prezzi(dict_1=dict_5)
print(f"La soluzione dell'esercizio 3 è: {dict_out}")