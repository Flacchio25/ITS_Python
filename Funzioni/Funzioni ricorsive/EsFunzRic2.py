''' Si supponga di voler calcolare l'ammontare del denaro depositato su un conto bancario ad interesse composto.
    Se m è la somma depositata sul conto, la somma disponibile alla fine del mese sarà 1.005 volte m.
    Scrivere una funzione ricorsiva compoundInterest che calcoli la somma presente sul conto dopo t mesi
    data una somma di partenza m.'''

'''def compoundInterest(m: float, tmesi: int) -> float:
    if tmesi == 0: 
        return m
    return 1.005 * compoundInterest(m, tmesi - 1)

print(compoundInterest(,))'''

def compoundInterest(m: float, tmesi: int, deposito_mensile: float) -> float:
    if tmesi == 0:
        return m  # Caso base: saldo iniziale
    return compoundInterest(m, tmesi - 1, deposito_mensile) * 1.005 + deposito_mensile

# Esempio di utilizzo: deposito mensile di 200€ per 18 anni (216 mesi)
anni = 30
mesi = anni * 12
deposito_mensile = 200

saldo_finale = compoundInterest(0, mesi, deposito_mensile)
print(f"Saldo finale dopo {anni} anni: {saldo_finale:.2f}€")


