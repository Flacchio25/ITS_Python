class Film:
    def __init__(self, id, titolo):
        self.__id = id
        self.__titolo = titolo

    def setID(self, ID):
        if isinstance(ID, int):
            self.__id = ID
        else:
            print("Errore, l'ID deve essere un numero intero!")

    def setTitle(self, title):
        if isinstance(title, str):
            self.__title = title
        else:
            print("Errore: il titolo deve essere una stringa!")
    
    def getID(self):
        return self.__id
    
    def getTitle(self):
        return self.__title
    
    def isEqual(self, otherFilm):
        if isinstance(otherFilm, Film):  # verifica che otherFilm sia un oggetto Film
            return self.getID() == otherFilm.getID()
        else:
            print("Errore: il parametro passato non è un oggetto Film")
            return False

class Azione(Film):

    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = "Azione"
        self.__penale = 3.0
    
    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni):
        return self.penale * giorni


class Commedia(Film):

    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = "Azione"
        self.__penale = 2.50
    
    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni):
        return self.penale * giorni



class Drama:

    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = "Azione"
        self.__penale = 2.0
    
    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni):
        return self.penale * giorni