'''# dal file Persona.py importa la classe Persona
from persona import Persona

#creare un oggetto di tipo persona

fc:Persona = Persona("Flaviano", "Corsi", 24)

print(fc)

print(fc.name, fc.lastname, fc.age)'''

#dal file persona2.py importa la classe Persona
from persona2 import Persona

fc:Persona = Persona()

#voglio richiamare la funzione displayData della calsse Persona per stampare in output le informazioni relative alla persona fc
fc.displayData()

#imposta il nome della persona fc
fc.setName("Flaviano")

print("--------")
fc.displayData()

#impostare il cognome della persona fc
fc.setLastname("Corsi")

#impostare l'età della persona fc
fc.setAge(24)

print("------")
fc.displayData()

print("------")

print(fc.getName(), fc.getLastname(), fc.getAge())

