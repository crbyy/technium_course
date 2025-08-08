from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    major: str
    gpa: float


    def display_info(self):
        print (f'Имя студента: {self.name}, возраст студента: {self.age}, Специальность: {self.major}, Средний балл: '
                f'{self.gpa}')



    def calculate_grade(self) -> str:
        """
        Вычисляет оценку, основываясь на среднем балле студента
        """
        if self.gpa >= 4.5:
            return("Отлично")
        if 4.4 > self.gpa > 3.5:
            return("Хорошо")
        if 3.4 > self.gpa > 2.5:
            return("Удовлетворительно")
        if 2.4 > self.gpa > 0:
            return("Неудовлетворительно")



# Создание списка студентов
students = [
    Student("Alice", 20, "Computer Science", 3.8),
    Student("Bob", 22, "Engineering", 3.2),
    Student("Charlie", 21, "Mathematics", 4.5),
    Student("David", 23, "Physics", 2.7),
    Student("Eve", 19, "Biology", 3.9),
    Student("Alice", 20, "Computer Science", 3.8)
]

# Отображение информации о студентах
for student in students:
    student.display_info()

# Сравнение студентов
print("Are Alice and Bob the same student?", students[0] == students[1])
print("Are Alice and Eve the same student?", students[0] == students[4])
print("Are Alice and Alice the same student?", students[0] == students[5])

# Расчет и вывод оценок
for student in students:
    print(f"{student.name} - Grade: {student.calculate_grade()}")


#Сортировка гпа по убыванию
students_sorted = sorted(students, key = lambda x: x.gpa, reverse=True)
for student in students_sorted:
    print(f'{student.name}, {student.gpa}, "{student.calculate_grade()}"')

