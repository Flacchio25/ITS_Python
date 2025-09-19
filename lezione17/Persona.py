class Persona:
    def __init__(self, nome, cognome):
        #verifica che nome sia una stringa
        if isinstance(nome, str):
            self.__nome = nome
        else:
            self.__nome = None
            print("il nome inserito non è una stringa!")
        
        #verifica che cognome sia una stringa
        if isinstance(cognome, str):
            self._cognome = cognome
        else:
            self._cognome = None
            print("il cognome inserito non è una stringa!")
        #imposta età a 0 solo se nome e cognome siano stringhe valide
        if self.__nome is not None and self.__cognome is not None:
            self.__eta = 0
        else:
            self.__eta = None
        
        #Setter per nome
    def setNome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print("Il nome inserito non è una stringa!")
        
    def setCognome(self, cognome):
        if isinstance(cognome, str):
            self.__cognome = cognome
        else:
            print("Il cognome inserito non è una stringa!")
    
    def setEta(self, eta):
        if isinstance(eta, int):
            self.__eta = eta
        else:
            print("L'età deve essere un numero intero!")
        
    def getNome(self):
        return self.__nome
    
    def getCognome(self):
        return self.__cognome
    
    def getEta(self):
        return self.__eta
    
    def greet(self):
        nome = self.__nome if self.__nome is not None else "[nome non disponibile]"
        cognome = self.__cognome if self.__cognome is not None else "[cognome non disponibile]"
        eta = f"{self.__eta}" if self.__eta is not None else "[età non disponibile]"
        print(f"Ciao, sono {nome} {cognome}! Ho {eta} anni!")
        