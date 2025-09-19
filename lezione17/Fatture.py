from Dottore import Dottore
from Paziente import Paziente

class Fattura:
   def __init__(self, paziente:list[Paziente], dottore:Dottore):
      if not Dottore.isAValidDoctor(): 
        print("Il dottore non è valido")
        self.__paziente = None
        self.__dottore = None
        self.__salary = None
        self.__fatture = None
      else:
        self.__paziente = paziente 
        self.__dottore = dottore
        self.__salary = self.get_fatture
        self.__fatture = 0.00

   def get_Salary(self, salary):
    value = self.__dottore.parcella * len(self.__paziente)
    self.__salary = value
    return f"Il dottore ha guadagnato {value} euro"
   
   def get_fatture(self, fatture):
    result = len(self.__paziente)
    self.fatture = result
    print(f"Il dottore ha {result}")

   def add_paziente(self, nuovoPaziente):
     self.__paziente.append(nuovoPaziente)