from abc import ABC, abstractmethod

class FormaGenerica(ABC): 
    
    def draw(self) -> None:
        pass

    def setShape(self, shape: str) -> None:
        if shape:
            self.shape = shape
        else:
            print("Errore! Shape non pul essere una stringa vuota")
    
    def getShape(self) -> str:
        return self.shape