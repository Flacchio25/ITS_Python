
class Persona:

    def __init__(self, name: str, lastname:str, age:int):
        self.setName = name
        self.setLastname = lastname
        self.setAge = age

    

def __str__(self):
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}"
    
def __call__(self):
    if self.age <18:
        print(f"{self.name} {self.lastname} è minorenne")
    else:
        print(f"{self.name} {self.lastname} è una persona adulta")

def SetName(self, name:str):
    if name:
          self.name = name
    else:
        print("Error! Il nome non può essere una stringa vuota")

def SetLastName(self, lastname:str):
    if lastname:
          self.lastname = lastname
    else:
        print("Error! Il cognome non può essere una stringa vuota")

def SetAge(self, age:int):
    if age < 0 or age > 130:
        self.age = 0
    else:
         
def speak(self):
    
    