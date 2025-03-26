'''Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate,
    cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.'''

def check_parentheses(expression: str) -> bool:
    bilanciato = 0
    for element in expression:
        if element == "(":
            bilanciato += 1
        elif element == ")":
            bilanciato -= 1
            if bilanciato < 0:
                return False
    return bilanciato == 0

print(check_parentheses("()()"))
print(check_parentheses("(()))("))