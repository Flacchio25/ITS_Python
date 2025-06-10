from string import ascii_lowercase


def cifrario(s: str, k:int) -> str:
    l: str = ""

    for carattere in s:
        
        if carattere in ascii_lowercase:

            index: int = ascii_lowercase.index(carattere)

            index = (index + k) % len(ascii_lowercase)

            l += ascii_lowercase(index)

        elif carattere in ascii_uppercase:

            index: int = ascii_uppercase.index(carattere)

            index = (index + k) % len(ascii_uppercase)

            l += ascii_uppercase[index]
        
        else:

            l += carattere

    return l

def bin_search(lista: list[int]) -> None:

    mid: int = len(lista) // 2

    if lista[mid] == numero: 

        print("il numero è stato trovato")

    elif len(lista) == 1:

        print("Numero non trovato")

    elif lista[mid] < numero:

        bin_search(lista[mid + 1:], numero)

    elif lista[mid] > numero:
        bin_search(lista[mid], numero)
