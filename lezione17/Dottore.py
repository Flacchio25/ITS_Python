from Persona import Persona

class Dottore(Persona):
    def __init__(self, nome, cognome, specializzazione, parcella):
        super().__init__(nome, cognome)

        if isinstance(specializzazione, str):
            self.__specializzazione = specializzazione
        else:
            self.__specializzazione = None
            print("La specializzazione inserita non è una stringa!")

        if isinstance(parcella, float):
            self.__parcella = parcella
        else:
            self.__parcella = None
            print("La parcella inserita non è un float!")
    
    def setSpecializzazione(self, specializzazione):
        if isinstance(specializzazione, str):
            self.__specializzazione = specializzazione
        else:
            print("La specializzazione inserita non è una stringa!")

    def setParcel(self, parcella):
        return self.__parcella
    
    def isAValidDoctor(self):
        eta = self.getEta()
        nome = self.getNome() or "[nome]"
        cognome = self.getCognome() or "[cognome]"
        if eta is not None and eta > 30:
            print(f"il Dottore {nome} {cognome} è valido")

    def doctorGreet(self):
        self.greet()
        specializzazione = self.__specializzazione if self.__specializzazione else "[specializzazione non disponibile]" 
        print(f"Sono un medico {specializzazione}")       