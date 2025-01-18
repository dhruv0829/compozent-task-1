class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self, name, age, grades):
        self.students[name] = {"age": age, "grades": grades}

    def update_student(self, name, age=None, grades=None):
        if name in self.students:
            if age:
                self.students[name]["age"] = age
            if grades:
                self.students[name]["grades"] = grades
        else:
            print("Student not found.")

    def delete_student(self, name):
        if name in self.students:
            del self.students[name]
        else:
            print("Student not found.")

    def display_student(self, name):
        if name in self.students:
            print(f"Name: {name}, Age: {self.students[name]['age']}, Grades: {self.students[name]['grades']}")
        else:
            print("Student not found.")

db = StudentDatabase()
db.add_student("John", 20, [85, 90, 78])
db.display_student("John")
db.update_student("John", grades=[88, 92, 80])
db.display_student("John")
db.delete_student("John")
db.display_student("John")
