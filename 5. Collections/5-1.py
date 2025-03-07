'''5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.'''


car = 'subaru'

# Test che restituiscono True
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')  # True

print("\nIs the length of car == 6? I predict True.")
print(len(car) == 6)  # True

print("\nIs car in the list ['subaru', 'toyota', 'honda']? I predict True.")
print(car in ['subaru', 'toyota', 'honda'])  # True

print("\nIs car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

# Test che restituiscono False
print("\nIs car == 'audi'? I predict False.")   
print(car == 'audi')  # False

print("\nIs car == 'toyota'? I predict False.")
print(car == 'toyota')  # False

print("\nIs the length of car == 5? I predict False.")
print(len(car) == 5)  # False

print("\nIs car not in the list ['subaru', 'toyota', 'honda']? I predict False.")
print(car not in ['subaru', 'toyota', 'honda'])  # False

print("\nIs car == 'AUDI'? I predict False.")
print(car.upper() == 'AUDI')  # False
