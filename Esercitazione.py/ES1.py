'''Scrivi una funzione che, data una lista,
ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.'''
def frequency_dict(elements: list) -> dict:
    freq = {}  
    for item in elements:
        if item in freq:
            freq[item] += 1  
        else:
            freq[item] = 1  
    return freq  

print(frequency_dict(['mela', 'banana', 'mela']))
