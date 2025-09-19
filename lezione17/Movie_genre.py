from Film import FIlm

class Azione:

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


class Commedia:

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