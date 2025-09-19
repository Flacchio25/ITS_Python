from abc import abstractmethod

class Volo(ABC):
    """
    Classe astratta per definire le funzionalità base di ogni tipo di volo.
    """
    def __init__(self, codice_volo: str, capacita_massima: int):
        """costruttore della classe volo."""

        if not isinstance(codice_volo, str) or not codice_volo:
            raise ValueError("Il codice del volo deve essere una stringa non vuota.")
        if not isinstance(capacita_massima, int) or capacita_massima <=0:
            raise ValueError("La capacità massima deve essere un intero positivo.")
        
        self.codice_volo = codice_volo
        self.capacita_massima = capacita_massima
        self.prenotazioni = 0

    @abstractmethod
    def prenota_posto(self, *args, **kwargs):
        '''metodo astratto per prenotare un posto sul volo.
           Deve essere implementato dalle sottoclassi.'''
        
        pass

    def posti_disponibili(self, *args, **kwargs):
        '''metodo astratto per ottenere il numero di posti disponibili.
           Deve essere implementato dalle sottoclassi.'''
        pass