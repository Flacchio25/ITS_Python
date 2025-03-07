dati_utente = {"nome": input("Inserisci il tuo nome: ").strip,#.strip() in Python viene usato per rimuovere gli spazi bianchi iniziali e finali da una stringa. 
    "ruolo": input("Inserisci il tuo ruolo(Admin, Moderatore, Utente, Ospite): ").strip().capitalize(),#capitalize in python serve per impostare la prima lettera maiuscola
                "età": int(input("Inserisci la tua età: ").strip())
                }

#ruolo e livello di accesso
match dati_utente["ruolo"]:
    case "Admin":
        accesso = "Accesso completo a tutte le funzionalità"
    case "Moderatore":
        accesso = "Può gestire i contenuti ma non può modificare le impostazioni"
    case "Utente":
        accesso = "Utente adulto(età >= 18) può visualizzare i contenuti"
    case "Utente minorenne(età < 18)":
        accesso = "limitato! alcune funzionalità sono bloccate"
    case "Utente minorenne(età < 18)":
        accesso = "limitato! alcune funzionalità sono bloccate"
    case "Ospite":
        accesso = "limitato! solo visualizzazione dei contenuti"  
    case _:
        accesso = "Attenzione! Ruolo non riconosciuto! Accesso negato!"

# Output del risultato
print(f"\nNome: {dati_utente['nome']}")
print(f"Ruolo: {dati_utente['ruolo']}")
print(f"Età: {dati_utente['età']}")
print(f"Livello di accesso: {accesso}") 