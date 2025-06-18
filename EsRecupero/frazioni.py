# Potrebbe essere utile importare typing se usi Any o Union per i type hints
from typing import Union, Any

class Frazione:
    _numeratore: int
    _denominatore: int

    # --- 2. Definire il Metodo __init__ (Costruttore) ---
    def __init__(self, numeratore_iniziale: int, denominatore_iniziale: int) -> None:
        # All'interno di __init__, userai i metodi setter per impostare i valori.
        # Questo garantisce che la logica di validazione dei setter venga applicata
        # anche al momento della creazione di una nuova frazione.

        # Chiamata al setter per il numeratore
        self.set_numeratore(numeratore_iniziale)

        # Chiamata al setter per il denominatore
        self.set_denominatore(denominatore_iniziale)


    # --- 3. Definire i Metodi Setter (set_numeratore, set_denominatore) ---
    def set_numeratore(self, nuovo_numeratore: Any) -> None: # Usiamo Any temporaneamente per il type hint per permettere il controllo
        # Qui devi implementare la logica di validazione:
        # 1. Controlla se 'nuovo_numeratore' è un numero intero.
        #    Suggerimento: isinstance(variabile, int) è un buon modo per controllare se è un int puro.
        #    Se vuoi gestire anche float che sono interi (es. 5.0), dovrai convertire a float e usare .is_integer(),
        #    ma fai attenzione al caso int puro.
        # 2. Se NON è un intero, imposta self._numeratore a 13.
        # 3. Altrimenti, imposta self._numeratore al 'nuovo_numeratore'.

        # Logica da implementare qui:
        # if ... (condizione per non essere un intero) ...:
        #     self._numeratore = 13
        # else:
        #     self._numeratore = nuovo_numeratore
        pass # Rimuovi questa riga e scrivi il tuo codice qui

    def set_denominatore(self, nuovo_denominatore: Any) -> None: # Usiamo Any temporaneamente per il type hint
        # Qui devi implementare la logica di validazione:
        # 1. Controlla se 'nuovo_denominatore' è un numero intero (stessa logica del numeratore).
        # 2. Controlla se 'nuovo_denominatore' è uguale a 0.
        # 3. Applica i valori di default (5) in caso di non intero O di zero.

        # Logica da implementare qui:
        # if ... (condizione per non essere un intero O essere zero) ...:
        #     self._denominatore = 5
        # else:
        #     self._denominatore = nuovo_denominatore
        pass # Rimuovi questa riga e scrivi il tuo codice qui


    # --- 4. Definire i Metodi Getter (get_numeratore, get_denominatore) ---
    def get_numeratore(self) -> int:
        return self._numeratore

    def get_denominatore(self) -> int:
        return self._denominatore


    # --- 5. Definire il Metodo __str__ ---
    def __str__(self) -> str:
        # Deve mostrare in output la frazione nel seguente modo: "numeratore / denominatore "
        # Usa gli attributi _numeratore e _denominatore.
        # Esempio: f"{self._numeratore} / {self._denominatore} "
        pass # Rimuovi questa riga e scrivi il tuo codice qui


    # --- 6. Definire il Metodo value() ---
    def value(self) -> float:
        # Deve restituire il valore della frazione (numeratore / denominatore)
        # arrotondato a 3 cifre decimali.
        # Ricorda che la divisione in Python tra interi produce un float,
        # ma devi assicurarti che il denominatore non sia 0 (cosa che i setter dovrebbero già prevenire).
        # Per l'arrotondamento, puoi usare la funzione round().
        pass # Rimuovi questa riga e scrivi il tuo codice qui