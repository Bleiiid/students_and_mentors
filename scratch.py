class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rating(self, summ = 0, counter = 0):
        for key in self.grades:
            for grade in self.grades[key]:
                summ += grade
                counter += 1
        if counter > 0:
            return summ / counter

    def __lt__(self, other):
        return self._average_rating < other._average_rating


    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self._average_rating()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}'''

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rating(self, summ = 0, counter = 0):
        for key in self.grades:
            for grade in self.grades[key]:
                summ += grade
                counter += 1
        if counter > 0:
            return summ / counter

    def __lt__(self, other):
        return self._average_rating < other._average_rating

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self._average_rating()}'''

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}'''

def average_rating_students(students, course):
    summ = 0
    counter = 0
    for student in students:
        if isinstance(student, Student):
            for grade in student.grades[course]:
                summ += grade
                counter += 1
    return summ / counter

def average_rating_lecturers(lecturers, course):
    summ = 0
    counter = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            for grade in lecturer.grades[course]:
                summ += grade
                counter += 1
    return summ / counter


student_1 = Student('Евгений', 'Удилов', 'муж')
student_2 = Student('Evgeniy', 'Udilov', 'муж')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в Python']
student_2.finished_courses += ['Введение в Python']

lecturer_1 = Lecturer('Oleg', 'Bulygin')
lecturer_2 = Lecturer('Олег', 'Булыгин')
lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Алена', 'Батицкая')
reviewer_2 = Reviewer('Alena', 'Batitskaya')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_2, 'Python', 10)
student_2.rate_hw(lecturer_1, 'Python', 9)
student_2.rate_hw(lecturer_2, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 9)

print(student_1)
print(lecturer_1)
print(reviewer_1)


