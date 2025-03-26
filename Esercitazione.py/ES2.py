'''Scrivi una funzione che, dato un numero intero, determina se è un "numero magico".
   Un numero magico è definito come un numero che contiene il numero 7.'''

def is_magic_number(n: int) -> bool:
    return '7' in str(n)

print(is_magic_number(56127389823))
