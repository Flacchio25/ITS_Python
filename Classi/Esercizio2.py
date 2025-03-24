'''1. Write a class called Student with the attributes name (str) and
studyProgram (str)
2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.
3. Add a method printInfo that prints the name and studyProgram of a
Student. Test your method on the objects!
4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too.'''

class Student:
    def __init__(self, name, studyProgram, age, gender):
        self.name = name   
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(f"Name: {self.name}, Study Program: {self.studyProgram}, Age: {self.age}, Gender: {self.gender}")

flaviano = Student("Flaviano", "Data Analyst", 25, "Male")
leonardo = Student("Leonardo", "Data Analyst", 24, "Male")
mirko = Student("Mirko", "Data Analyst", 26, "Male")

Student.printInfo(flaviano)
Student.printInfo(leonardo)
Student.printInfo(mirko)


