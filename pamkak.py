class Student:
    student = 'student'

    def __init__(self ,name,grade):
        self.name = name
        self.grade = grade

student1 = Student('Viraj',10)
student2 = Student('Keheliya',11)

print(f'{student1.name} is a grade {student1.grade} {student1.student}')
print(f'{student2.name} is a grade {student2.grade} {student2.student}')