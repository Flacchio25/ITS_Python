'''import saluto

saluto.greet(input("Inserisci il tuo nome: "))'''

import saluto as s

s.greet("Claudia")


'''Se voglio importare solo la funzione greet dal modulo saluto, e ignorare il resto del modulo saluto, farò:'''

from saluto import greet

greet("Claudia")

from saluto import greet as g
b
g("Claudia")