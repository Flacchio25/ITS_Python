'''Scrivere un programma in Python che legga una frase di una riga e mostri una delle seguenti risposte:
- "Si" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è pari;
- "No" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è dispari;
- "Wow!" -> se la frase termina con un punto esclamativo (!)
- "Tu dici" seguito dalla frase inserita racchiusa tra doppi apici in tutti gli altri casi.'''

frase = input("Inserisci una stringa: ")
lunghezza = len(frase)

match frase:
    case _ if frase[-1] == "?" and lunghezza % 2 == 0:
        print("Si")
    case _ if frase[-1] == "?" and lunghezza % 2 != 0:
        print("No")
    case _ if frase [-1] == "!":
        print("Wow!")
    case _:
        print(f"Tu dici \"{frase}\"")
