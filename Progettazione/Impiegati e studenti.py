from __future__ import annotations

from custom_types import *
from datetime import date

class Persona:
    _nome: str
    _cognome: str
    _cf: CodiceFiscale
    _nascita: date #immutabile

    _is_uomo: bool # da fusione
    _is_donna: bool #da fusione 
    _maternita: IntGEZ | None #da fusione con Donna
    _posizione_militare: _posizione_militare | None #da fusione con Uomo e aggregazione

    def __init__(self, nome: str, cognome: str, cf: CodiceFiscale, nascita: date,
                 maternita: IntGEZ| None= None,
                 posizione_militare: _posizione_militare | None=None) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_cf(cf)
        self._cf = cf


        if maternita is not None:
            self.set_attributi_donna(maternita)

        if posizione_militare is not None:
            self.set_attributi_uomo(posizione_militare)
        
        if not (self._is_uomo() or self._is_donna()):
            # [V.Persona.fusione]
            #Per ogni p: Persona: p.is_donna == True or p.is_uomo == True
            raise ValueError("Ogni persona deve essere uomo, donna o entrambi!")

    
    def set_attributi_donna(self, maternita: IntGEZ) -> None:
        self._is_donna = True 
        self._maternita = maternita       
    
    def set_attribtui_uomo(self, posizione_militare) -> None:
        self._is_uomo = True

    def is_uomo(self) -> bool:
        return self._is_uomo
    
    def is_donna(self) -> bool:
        return self._is_donna


    def set_nome(self, nome: str)-> None:
        self._nome = nome