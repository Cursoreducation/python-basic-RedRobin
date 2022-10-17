class Person():
    def __init__(self, name, surname, age=None):
        self.name = name
        self.surname = surname
        self.age = age

    def info(self):
        is_age = f' and I am {self.age} years old' if self.age else ''
        print(f'I am {self.name} {self.surname}{is_age}')

class Student(Person):
    def __init__(self, name, surname, university, grade):
        super().__init__(name, surname)
        self.university = university
        self.grade = grade

    def student_info(self):
        self.info()
        print(f'My university: {self.university} and grade: {self.grade}')


jeff = Person('Jeff', 'Body', 35)
jeff.info()




john = Student('John', 'Torse', 'Polytechnics University', 'A')
john.student_info()

print(issubclass(Student, Person))
print(isinstance(john, Student))