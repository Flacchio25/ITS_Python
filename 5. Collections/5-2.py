'''5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''

# 1. Test di uguaglianza e disuguaglianza con stringhe
fruit = "apple"
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')  # True

print("\nIs fruit != 'apple'? I predict False.")
print(fruit != 'apple')  # False

#2. Uso di lower()

name = "Flavio"
print("\n Is name.lower() == 'flavio? I predict True")
print(name.lower() == 'flavio')
print("\n is name.lower == 'FLAVIO'? I predict False")
print(name.lower() == 'FLAVIO')

#3. Test numerici
age = 25
print("\nIs age > 20 ? I predict True")
print(age > 20)
print("\nIs age < 18 ? I predict False")
print(age <18)

year = 2025
print("\nIs year == 2025? I predict True")
print( year == 2025)
print("\nIs year != 2025? I predict False")
print(year != 2025)

number = 10
print("\nIs number >= 10? I predict True")
print(number >= 10)
print("\nIs number <= 9? I predict False")
print(number <= 9)

#Test con and e or

temperatura = 25
umidità = 75
print("\nIs temperatura > 24 and umidità < 80? I predict True.")
print(temperatura > 24 and umidità < 80) 
print("\nIs temperatura > 25 and umidità <75? I predict false")
print(temperatura > 25 or umidità < 75)

#Verifica se un elemento è presente in una lista

alunni = ["Flaviano", "Alessio", "Mirko", "Leonardo"]
print("\nIs Alessio in alunni? I predict True")
print("Alessio" in alunni)


#Verifica se un elemento non è presente in una lista
print("\nIs Mattia in alunni? I predict False")
print("Mattia" in alunni)

