import os # Importa il modulo os per le operazioni sul filesystem (creazione directory, gestione percorsi)

# Classe base Documento
class Documento:
    """
    Rappresenta un documento generico con contenuto testuale.
    """
    def __init__(self, testo=""):
        """
        Inizializza un oggetto Documento.

        Args:
            testo (str): Il contenuto testuale del documento. Di default è una stringa vuota.
        """
        self.testo = testo

    def getText(self):
        """
        Restituisce il contenuto testuale del documento.

        Returns:
            str: Il testo del documento.
        """
        return self.testo

    def setText(self, nuovo_testo):
        """
        Imposta un nuovo contenuto testuale per il documento.

        Args:
            nuovo_testo (str): Il nuovo testo da impostare.
        """
        self.testo = nuovo_testo

    def isInText(self, parola_chiave):
        """
        Verifica se una parola chiave è presente nel testo del documento (case-insensitive).

        Args:
            parola_chiave (str): La parola chiave da cercare.

        Returns:
            bool: True se la parola chiave è presente, False altrimenti.
        """
        # Convertiamo entrambi in minuscolo per una ricerca case-insensitive
        return parola_chiave.lower() in self.testo.lower()

# Classe Email derivata da Documento
class Email(Documento):
    """
    Rappresenta un'email, estendendo la classe Documento con mittente, destinatario e titolo.
    Il corpo del messaggio è memorizzato nella variabile 'testo' ereditata.
    """
    def __init__(self, mittente, destinatario, titolo, messaggio_corpo):
        """
        Inizializza un oggetto Email.

        Args:
            mittente (str): L'indirizzo email del mittente.
            destinatario (str): L'indirizzo email del destinatario.
            titolo (str): Il titolo del messaggio email.
            messaggio_corpo (str): Il corpo del messaggio email.
        """
        # Chiama il costruttore della classe padre (Documento) per memorizzare il corpo del messaggio
        super().__init__(messaggio_corpo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo = titolo

    # Metodi get e set per mittente, destinatario e titolo
    def getMittente(self):
        return self.mittente

    def setMittente(self, nuovo_mittente):
        self.mittente = nuovo_mittente

    def getDestinatario(self):
        return self.destinatario

    def setDestinatario(self, nuovo_destinatario):
        self.destinatario = nuovo_destinatario

    def getTitolo(self):
        return self.titolo

    def setTitolo(self, nuovo_titolo):
        self.titolo = nuovo_titolo

    def getText(self):
        """
        Ridefinisce il metodo getText() per concatenare e restituire tutti
        i campi di testo specifici dell'email (mittente, destinatario, titolo, e messaggio).

        Returns:
            str: La stringa formattata contenente tutti i dettagli dell'email.
        """
        return (f"Da: {self.mittente}, A: {self.destinatario}\n"
                f"Titolo: {self.titolo}\n"
                f"Messaggio: {self.testo}")

    def writeToFile(self, percorso_file):
        """
        Scrive il risultato del metodo getText() dell'email in un file di testo specificato.

        Args:
            percorso_file (str): Il percorso completo del file in cui scrivere.
        """
        try:
            with open(percorso_file, 'w', encoding='utf-8') as file:
                file.write(self.getText())
            print(f"Contenuto email scritto con successo in: {percorso_file}")
        except IOError as e:
            print(f"Errore durante la scrittura del file {percorso_file}: {e}")

# Classe File derivata da Documento
class File(Documento):
    """
    Rappresenta un documento il cui contenuto è letto da un file esterno.
    """
    def __init__(self, nome_percorso):
        """
        Inizializza un oggetto File.

        Args:
            nome_percorso (str): Il percorso del file da cui leggere il contenuto.
        """
        super().__init__() # Inizializza il testo della classe base come vuoto inizialmente
        self.nome_percorso = nome_percorso

    def getNomePercorso(self):
        return self.nome_percorso

    def setNomePercorso(self, nuovo_nome_percorso):
        self.nome_percorso = nuovo_nome_percorso

    def leggiTestoDaFile(self):
        """
        Legge il contenuto testuale dal file specificato in nomePercorso
        e lo memorizza nella variabile ereditata 'testo'.
        """
        try:
            with open(self.nome_percorso, 'r', encoding='utf-8') as file:
                self.setText(file.read()) # Usa il setter della classe base
            print(f"Contenuto letto con successo da: {self.nome_percorso}")
        except FileNotFoundError:
            print(f"Errore: Il file '{self.nome_percorso}' non è stato trovato.")
            self.setText("") # Imposta il testo a vuoto in caso di errore
        except IOError as e:
            print(f"Errore durante la lettura del file {self.nome_percorso}: {e}")
            self.setText("") # Imposta il testo a vuoto in caso di errore

    def getText(self):
        """
        Ridefinisce il metodo getText() per concatenare e restituire
        il nome del percorso e il contenuto del file.

        Returns:
            str: La stringa formattata contenente il percorso e il contenuto del file.
        """
        # Assicurati che il testo sia stato letto prima di restituirlo
        if not self.testo and os.path.exists(self.nome_percorso):
            self.leggiTestoDaFile() # Tenta di leggere il file se il testo è vuoto e il file esiste

        return (f"Percorso: {self.nome_percorso}\n"
                f"Contenuto: {self.testo}")


# --- Codice Driver per il Test ---
def main():
    """
    Funzione principale per testare le classi Documento, Email e File.
    """
    print("--- Test Classi Testi Digitali ---")

    # Definizione di un percorso temporaneo per i file
    # Usiamo una sottocartella 'temp_docs' per non sporcare la directory corrente
    temp_dir = "temp_docs"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir) # Crea la directory se non esiste

    # --- Test Email ---
    print("\n--- Test Email ---")
    email_path = os.path.join(temp_dir, "email1.txt")

    # Creazione oggetto Email
    email1 = Email(
        mittente="alice@example.com",
        destinatario="bob@example.com",
        titolo="Incontro",
        messaggio_corpo="Ciao Bob, possiamo incontrarci domani?"
    )

    # Stampa del testo dell'email
    print("\nTesto dell'email (metodo getText()):")
    print(email1.getText())

    # Scrittura del contenuto dell'email su un file
    print("\nScrittura del contenuto dell'email su file:")
    email1.writeToFile(email_path)

    # Verifica della presenza di parole chiave nell'email
    print("\nVerifica presenza parole chiave nell'email:")
    parola_email_presente = 'incontrarci'
    parola_email_assente = 'vacanza'
    print(f"La parola '{parola_email_presente}' è presente? {email1.isInText(parola_email_presente)}") # Atteso: True
    print(f"La parola '{parola_email_assente}' è presente? {email1.isInText(parola_email_assente)}") # Atteso: False


    # --- Test File ---
    print("\n--- Test File ---")
    file_name = "document.txt"
    document_path = os.path.join(temp_dir, file_name)
    file_content = "Questo e' il contenuto del file."

    # Crea il file document.txt con il contenuto specificato
    try:
        with open(document_path, 'w', encoding='utf-8') as f:
            f.write(file_content)
        print(f"File '{file_name}' creato con successo in: {document_path}")
    except IOError as e:
        print(f"Errore durante la creazione di '{file_name}': {e}")
        return # Esce se non riesce a creare il file

    # Creazione oggetto File
    file1 = File(document_path)

    # Lettura del testo dal file (avviene implicitamente o esplicitamente)
    # file1.leggiTestoDaFile() # Potremmo chiamarlo esplicitamente, ma getText() lo farà se necessario

    # Stampa del testo del file
    print("\nTesto del file (metodo getText()):")
    print(file1.getText())

    # Verifica della presenza di parole chiave nel file
    print("\nVerifica presenza parole chiave nel file:")
    parola_file_presente = 'contenuto'
    parola_file_assente = 'percorso'
    print(f"La parola '{parola_file_presente}' è presente? {file1.isInText(parola_file_presente)}") # Atteso: True
    print(f"La parola '{parola_file_assente}' è presente? {file1.isInText(parola_file_assente)}")   # Atteso: False

    # --- Pulizia ---
    print("\n--- Pulizia dei file temporanei ---")
    try:
        os.remove(email_path)
        os.remove(document_path)
        os.rmdir(temp_dir)
        print(f"File '{email_path}' e '{document_path}' e directory '{temp_dir}' rimossi.")
    except OSError as e:
        print(f"Errore durante la pulizia: {e}")


if __name__ == "__main__":
    main() # Esegue la funzione principale quando lo script viene eseguito
