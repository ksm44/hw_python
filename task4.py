class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        dic = self.grades
        avg = 0
        total_grades_sum = 0
        total_grades_count = 0
        for course, grades in dic.items():
            total_grades_sum += sum(grades)
            total_grades_count += len(grades)
        if total_grades_count != 0:
             avg += round( total_grades_sum / total_grades_count, 1 )
        else:
             avg = 0

        current_courses = ', '.join(self.courses_in_progress)

        oneline_current_courses = ', '.join(self.finished_courses)

        return (f'Имя: {self.name} \n' +
                f'Фамилия: {self.surname} \n' +
                f'Средняя оценка за домашние задания: {avg} \n' +
                f'Курсы в процессе изучения: {current_courses} \n' +
                f'Завершенные курсы: {oneline_current_courses} \n')

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (course in self.courses_in_progress or course in self.finished_courses) and grade in range(1,11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            return None
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

#лекторы
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def avg_rate(self):
        dic = self.grades
        avg = 0
        total_grades_sum = 0
        total_grades_count = 0
        for course, grades in dic.items():
            total_grades_sum += sum(grades)
            total_grades_count += len(grades)
        if total_grades_count != 0:
            return round(total_grades_sum / total_grades_count, 1)
        else:
            return 0

    def __str__(self):
        avg = self.avg_rate()

        return (f'Имя: {self.name} \n' +
                f'Фамилия: {self.surname} \n' +
                f'Средняя оценка за лекции: {avg} \n')

    def __eq__(self, other):
        return self.avg_rate() == other.avg_rate()

    def __lt__(self, other):
        return self.avg_rate() < other.avg_rate()

    def __gt__(self, other):
        return self.avg_rate() > other.avg_rate()

#проверяющие
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \n' + f'Фамилия: {self.surname} \n'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


lecturer = Lecturer('Иван', 'Иванов')
bad_lecturer = Lecturer('Плохих', 'Валерий')

some_reviewer = Reviewer('Some', 'Buddy')
other_reviewer = Reviewer('Другой', 'Ревьюерович')

student = Student('Алёхина', 'Ольга', 'Ж')
good_student = Student('Отличников', 'Петр', 'М')

student.courses_in_progress += ['Python', 'Java' , 'Введение в программирование']
student.finished_courses += ['Математический анализ']
good_student.courses_in_progress += ['Java' , 'Введение в программирование']
good_student.finished_courses += ['Математический счет']


lecturer.courses_attached += ['Python', 'Java' , 'Введение в программирование']
bad_lecturer.courses_attached += ['Python', 'Java' , 'Введение в программирование']

some_reviewer.courses_attached += ['Python', 'Java' , 'Введение в программирование']
other_reviewer.courses_attached += ['Python', 'Введение в программирование']

some_reviewer.rate_hw(student,'Python',10)
some_reviewer.rate_hw(student,'Python',9)
some_reviewer.rate_hw(student,'Java',8)
some_reviewer.rate_hw(student,'Введение в программирование',7)

other_reviewer.rate_hw(good_student,'Python',10)
other_reviewer.rate_hw(good_student,'Python',10)
other_reviewer.rate_hw(good_student,'Введение в программирование',10)
other_reviewer.rate_hw(good_student,'Введение в программирование',10)
other_reviewer.rate_hw(good_student,'Введение в программирование',10)

student.rate_lecture(lecturer, 'Введение в программирование', 10)
student.rate_lecture(lecturer, 'Введение в программирование', 10)
student.rate_lecture(lecturer, 'Введение в программирование', 10)
student.rate_lecture(lecturer, 'Введение в программирование', 10)
student.rate_lecture(lecturer, 'Java', 1)
student.rate_lecture(lecturer, 'Java', 2)
student.rate_lecture(lecturer, 'Java', 3)
student.rate_lecture(lecturer, 'Python', 7)
student.rate_lecture(lecturer, 'Python', 8)
student.rate_lecture(lecturer, 'Python', 9)
student.rate_lecture(lecturer, 'Python', 9)

student.rate_lecture(bad_lecturer, 'Введение в программирование', 1)
student.rate_lecture(bad_lecturer, 'Введение в программирование', 1)
student.rate_lecture(bad_lecturer, 'Введение в программирование', 1)

def avg_students_grade_in_course(students, course):
    total_sum_grades = 0
    total_count_grades = 0
    for student in students:
            if course in student.grades:
                total_sum_grades += sum(student.grades[course])
                total_count_grades += len(student.grades[course])
    if total_count_grades != 0:
        return round(total_sum_grades / total_count_grades, 1)
    else:
        return '0'

def avg_lecturers_grade_in_course(lecturers, course):
    total_sum_grades = 0
    total_count_grades = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_sum_grades += sum(lecturer.grades[course])
            total_count_grades += len(lecturer.grades[course])
    if total_count_grades != 0:
        return round(total_sum_grades / total_count_grades, 1)
    else:
        return '0'

print(avg_students_grade_in_course([student, good_student], 'Введение в программирование'))
print(avg_lecturers_grade_in_course([bad_lecturer, lecturer], 'Введение в программирование'))