from Dottore import Dottore
from Paziente import Paziente

class Fattura:
    def __init__(self, pazienti: list, dottore: Dottore):
        if not dottore.isAValidDoctor():
            print("Il dottore non è valido")
            self.__pazienti = None
            self.__dottore = None
            self.__salary = None
            self.__fatture = None
        else:
            self.__pazienti = pazienti
            self.__dottore = dottore
            self.__fatture = len(self.__pazienti)
            self.__salary = self.getSalary()

    def getSalary(self):
        self.__salary = self.__dottore.getParcel() * len(self.__pazienti)
        return self.__salary

    def getFatture(self):
        self.__fatture = len(self.__pazienti)
        return self.__fatture

    def addPatient(self, nuovoPaziente):
        if self.__pazienti is not None:
            self.__pazienti.append(nuovoPaziente)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.__dottore.getLastname()} è stato aggiunto il paziente {nuovoPaziente.getidCode()}")

    def removePatient(self, idCode):
        if self.__pazienti is not None:
            for paziente in self.__pazienti:
                if paziente.getidCode() == idCode:
                    self.__pazienti.remove(paziente)
                    self.getFatture()
                    self.getSalary()
                    print(f"Alla lista del Dottor {self.__dottore.getLastname()} è stato rimosso il paziente {idCode}")
                    return
            print(f"Nessun paziente con ID {idCode} trovato.")
