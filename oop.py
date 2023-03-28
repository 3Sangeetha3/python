class Student:
    def __init__(self):
        self.name = input("Enter student's name: ")
        self.age = int(input("Enter student's age: "))
        self.degree = input("Enter student's degree: ")

Stud_1 = Student()
Stud_2 = Student()

print(f"Stud_1.name: {Stud_1.name}")
print(f"Stud_1.age: {Stud_1.age}")
print(f"Stud_1.degree: {Stud_1.degree}")

print(f"Stud_2.name: {Stud_2.name}")
print(f"Stud_2.age: {Stud_2.age}")
print(f"Stud_2.degree: {Stud_2.degree}")