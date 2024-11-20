class Faculty:
    pass

class Course:
    pass


class Student:
    def __init__(self, course, faculty):
        self.course = course
        self.faculty = faculty


course = Course()
faculty = Faculty()

s1 = Student(course, faculty)
