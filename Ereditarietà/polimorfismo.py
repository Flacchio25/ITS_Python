from persona import Persona

from alieno import Alieno

# creare un oggetto p della classe Persona

p: Persona = Persona("Flaviano", "Corsi", 24)

#visualizzare le informazioni relative alla Pesona P 
print(p)

#creare un oggetto et della classe Alieno
et:Alieno = Alieno ("Andromeda")

#visualizzare le informazioni relative all'alieno et
print(et)       
#l'oggetto p invoca il metodo speak()
p.speak()

#l'oggetto et invoca il metodo speak()
et.speak()
            