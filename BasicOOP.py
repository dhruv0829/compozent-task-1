class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}")

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

student1 = Student("Alice", 22, [90, 88, 93])
student1.display_details()
print(f"Average Grade: {student1.calculate_average_grade()}")
