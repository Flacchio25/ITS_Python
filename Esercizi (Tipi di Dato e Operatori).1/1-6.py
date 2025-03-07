its_bakery_menu = {"Pizza":9.00, "Pasta":10.50, "Zuppa":7.00, "Hamburger":15.50, "Cotoletta":10.00, "Salmone":20.20, "Patatine Fritte":5.50, "Patate al forno":5.50, "Verdura del giorno":7.00, "Cheesecake":6.00, "Tiramisu'":6.00, "Focaccia con Nutella":6.00, "Coca Cola":3.50, "Acqua":1.50, "Vino":5.00}
ordine ={"primo":"Pasta", "secondo": "Hamburger","contorno": "Patatine Fritte", "bevanda": "Coca Cola", "dolce": "Cheesecake"}
conto_totale = 0
for piatto in ordine.values():
    conto_totale += its_bakery_menu[piatto]

print(f"Il conto totale è: {conto_totale:.2f} euro.")