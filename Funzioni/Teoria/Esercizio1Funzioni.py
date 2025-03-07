'''Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.'''


def check_value(num):
    if num > 5:
        print(f"Il numero {num} è maggiore di 5")
    elif num < 5:
        print(f"Il numero {num} è minore di 5")
    else:
        print(f"Il numero è uguale a 5")