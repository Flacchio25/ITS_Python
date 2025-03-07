'''Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this: "Santiago, Chile". 
Call your function with at least three city-country pairs, and print the values that are returned.'''

def city_country(city, country):
    # Versione I (concatenazione con spazio dopo la virgola)
    return city + ", " + country

    # Versione II (usando f-string - se vuoi usarla invece)
    # return f"{city}, {country}"

# Chiamate della funzione
print(city_country('"Roma"', '"Italia"'))
print(city_country('"Parigi"', '"Francia"'))
print(city_country('"Amsterdam"', '"Olanda"'))

    