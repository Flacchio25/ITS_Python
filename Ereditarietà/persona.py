
class Persona:

    def __init__(self, name: str, lastname:str, age:int):
        self.name = name
        self.lastname = lastname
        self.age = age

    

def __str__(self):
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}"
    
def __call__(self):
    if self.age <18:
        print(f"{self.name} {self.lastname} è minorenne")
    else:
        print(f"{self.name} {self.lastname} è una persona adulta")