'''Write a function called describe_city() that accepts the name of a city and its country.
The function should print a simple sentence, such as Reykjavik is in Iceland.
Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.'''

def describe_city(city:str="Roma", country:str="Italia"):
    print(f"la città di {city} è in {country}") 
          

describe_city()
describe_city("Palermo")
describe_city("New York", "America")