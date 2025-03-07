'''Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters'''

def check_lenght(monopoli):
    if len(monopoli) > 10:
        print(f"la parola {monopoli} ha più di 10 caratteri")
    elif len(monopoli) < 10:
        print(f"la parola{monopoli} ha meno di 10 caratteri")
    else:
        print(f"la parola{monopoli} ha 10 caratteri")

check_lenght("Mirko")