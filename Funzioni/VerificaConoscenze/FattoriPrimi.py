'''Scrivi una funzione che calcoli i fattori primi di un numero intero positivo n.'''

def fattori_primi(n):
    fattori = []
    divisore = 2
    
    while n > 1:
        while n % divisore == 0:
            fattori.append(divisore)
            n //= divisore
        divisore += 1
    
    return fattori

print(fattori_primi(4))   
print(fattori_primi(60))  
