from string import punctuation

def count(text: str) -> dict[str, int]:
    d: dict[str, int] = {}
    
    # 1. Normalizzazione a minuscolo prima di dividere
    l_text: str = text.lower()
    
    # 2. Utilizzo di .split() senza argomenti per dividere su qualsiasi sequenza di spazi bianchi
    #    (spazi, tabulazioni, newline) e per eliminare automaticamente i token vuoti risultanti.
    tokens: list[str] = l_text.split()
    
    for token in tokens:
        # 3. Rimozione della punteggiatura iniziale e finale.
        c_token: str = token.strip(punctuation)
        
        # 4. Ignora i token che diventano stringhe vuote dopo la rimozione della punteggiatura.
        if not c_token:
            continue
        
        # 5. Conteggio delle occorrenze.
        if c_token in d:
            d[c_token] += 1
        else:
            d[c_token] = 1

    return d