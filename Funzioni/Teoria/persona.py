class Persona:
    """Classe che rappresenta una persona con nome, cognome ed età."""
    
    def __init__(self, name: str, lastname: str, age: int):
        """
        Inizializza un'istanza della classe Persona.
        
        :param name: Nome della persona (stringa)
        :param lastname: Cognome della persona (stringa)
        :param age: Età della persona (intero)
        """
        self.name = name
        self.lastname = lastname
        self.age = age
