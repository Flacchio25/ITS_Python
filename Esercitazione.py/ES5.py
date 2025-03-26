'''La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
Codice da correggere: '''

'''def calculate_average(numbers: list[int])-> float:
        if len(numbers) == 0:
            return sum(numbers) / len(numbers)
        else:
            return len(numbers) / sum(numbers)

    print(calculate_average([1, 2, 3, 4, 5]))'''

def calculate_average(numbers: list[int])-> float:
    if len(numbers) == 0:
        return 0
    return sum(numbers)/ len(numbers)