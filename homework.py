class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress: #and course in student.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_mean_grade(self):
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0

    def __str__(self):
        Z_C = ''.join(self.finished_courses)
        C_P = ', '.join(self.courses_in_progress)
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за домашнее задание: {self.get_mean_grade()}\n' f'Курсы в процессе изучения: {C_P}\n' f'Завершенные курсы: {Z_C}\n'

    def __lt__(self, other):
        return self.get_mean_grade() < other.get_mean_grade()

    def __le__(self, other):
        return self.get_mean_grade() <= other.get_mean_grade()

    def __eq__(self, other):
        return self.get_mean_grade() == other.get_mean_grade()

    def __ne__(self, other):
        return self.get_mean_grade() != other.get_mean_grade()

    def __gt__(self, other):
        return self.get_mean_grade() > other.get_mean_grade()

    def __ge__(self, other):
        return self.get_mean_grade() >= other.get_mean_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_mean_grade(self):
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {self.get_mean_grade()}\n'

    def __lt__(self, other):
        return self.get_mean_grade() < other.get_mean_grade()

    def __le__(self, other):
        return self.get_mean_grade() <= other.get_mean_grade()

    def __eq__(self, other):
        return self.get_mean_grade() == other.get_mean_grade()

    def __ne__(self, other):
        return self.get_mean_grade() != other.get_mean_grade()

    def __gt__(self, other):
        return self.get_mean_grade() > other.get_mean_grade()

    def __ge__(self, other):
        return self.get_mean_grade() >= other.get_mean_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')     #Задание 1 и 2 - оценки ставит подкласс "проверяющий"
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(f'Оценки студента по курсу {best_student.grades}')

cool_lecturer = Lecturer('Some', 'Buddy')
best_student.courses_in_progress += ['python']

best_student.rate_lecturer(cool_lecturer, 'python', 10)
best_student.rate_lecturer(cool_lecturer, 'python', 10)
best_student.rate_lecturer(cool_lecturer, 'python', 8)

print(f'Оценка лектора студентом по курсу {cool_lecturer.grades}\n')

some_lecturer = Lecturer('SoMe', 'BuDdY')
some_lecturer.courses_attached += ['Python']

some_student = Student('some', 'student', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['ВВедение в программирование']

some_student.rate_lecturer(some_lecturer, 'Python', 5)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 8)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 1)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 7)

print(some_reviewer)

print(some_lecturer)

print(some_student)

#появляется имбовый лектор для сравнения
best_lecturer = Lecturer('Best','Lecturer')

some_student.rate_lecturer(best_lecturer, 'Python', 10)
some_student.rate_lecturer(best_lecturer, 'Python', 10)
some_student.rate_lecturer(best_lecturer, 'Python', 10)

print(some_lecturer <= best_lecturer)
#так же сравним пару студентов
print(f'{some_student == best_student}\n')

# задание 4. создаем экземпляры классов
student1 = Student('Alex', 'Nevskiy', 'male')
student2 = Student('Ksenia', 'Sobchak', 'female')

lecturer1 = Lecturer('Bob', 'Marley')
lecturer2 = Lecturer('Snoop', 'Dogg')

reviewer1 = Reviewer('Danna', 'Scally')
reviewer2 = Reviewer('Fox', 'Maulder')

# Добавляем курсы для студентов и лекторов
student1.courses_in_progress += ['Python']
