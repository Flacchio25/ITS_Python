'''Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.'''

'''Si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri compresi tra il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri'''

def vowelsCounter(s:str)-> str:
    if not s:
        return 0
    if s[0].lower() in ["a", "e", "i", "o", "u"]:
        return 1+ vowelsCounter(s[1:])
    else:
        return 0 + vowelsCounter(s[1:])
    


print(f"La stringa \"Pappagallo\" contiene {vowelsCounter('Pappagallo')} vocali")