'''1. School Grading System:

     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.'''


def classificaStudenti(nome: str, punteggi: int):
    media = sum(punteggi)/len(punteggi)
    risultato = "Superato" if media >= 60 else "fallito"

print(f"Studente: {nome}, Media:{media:.2f}, Risultato:{risultato}")
    
#lista per memorizzare studenti
studenti = []

n = int(input("Quanti studenti vuoi inserire? "))
for _ in range(n):
   nome = input("Inserisci il nome dello studente: ")
   punteggio = Input("Inserisci il punteggio dello studente: ")
   studenti.append((nome, punteggi))

for studente in studenti:
    classificaStudenti(studente[0], studente[1])