nome_animale = input("Inserisci il nome dell'animale: ")
match nome_animale:
    case _ if nome_animale in ["cane","gatto","cavallo", "elefante", "leone"]:
        print(f"{nome_animale} è un Mammifero")
    case _ if nome_animale in ["serpente","lucertola","coccodrillo","tartaruga"]:   
        print(f"{nome_animale} appartiene alla famiglia dei Rettili")
    case _ if nome_animale in ["squalo","trota","salmone","carpa"]:   
        print(f"{nome_animale} fa parte della famiglia dei Pesci")
    case _ if nome_animale in ["aquila", "pappagallo", "gufo", "falco"]:
        print(f" {nome_animale} è categorizzato in Uccelli")
    case _:
        print("Il programma non è in grado di classificare l'animale")