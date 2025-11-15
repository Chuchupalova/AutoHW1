class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade
    def change_average_grade(self, new_average_grade):
        self.average_grade = new_average_grade
    def info(self):
        return (f"Student: {self.name} {self.surname} {self.age} {self.average_grade}")
    #object
    student1 = Student("John", "Smith", "19", 90)
    #info
    print(student1.info())
    #change average grade
    student1.change_average_grade(100)
    #print new info
    print(student1.info())