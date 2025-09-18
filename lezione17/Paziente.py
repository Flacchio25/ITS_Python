from Persona import Persona

class Paziente(Persona):
    def __init__(self, nome, cognome, eta, IDCodice: str):
        super().__init__(nome, cognome, eta)
        
        self.__IDCodice = self.set_IDCodice(IDCodice)

    def set_IDCodice(self, IDCodice):
        self.__IDCodice = IDCodice

    def getIDCodice(self, IDCodice):
        return self.__IDCodice
    
    def patientinfo(self):
        print(f"Paziente: {self.nome} {self.cognome}\nID: {self.__IDCodice}")

