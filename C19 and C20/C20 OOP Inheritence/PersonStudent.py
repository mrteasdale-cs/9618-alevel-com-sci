class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    def greet(self):
        return f"Hello, I'm {self.name}."

class Student(Person):
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_student_info(self):
        return f"Student ID: {self.student_id}"

    def study(self):
        return f"{self.name} is studying."

student = Student("Alice", 18, "12345")
print(student.introduce())
print(student.display_student_info())
print(student.greet())
print(student.study())
