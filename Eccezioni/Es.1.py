'''Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt().
Handle ValueError if the input is negative by returning an informative message.'''
def safe_sqrt(number):
    import math
    try:
        return math.sqrt(number)
    except ValueError:
        return "Errore: impossibile calcolare la radice quadrata di un numero negativo."


print(safe_sqrt(81))   
print(safe_sqrt(-9))  
