# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об('єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент", '
#             'який дозволяє змінювати середній бал студента. Виведіть інформацію про студента '
#             'та змініть його середній бал.)

class Student():
    def __init__(self, name, surname, age, avg_rate):
        self.name = name
        self.surname = surname
        self.age = age
        self._avg_rate = avg_rate

    def set_avg_rate(self, new_avg_rate):
        self._avg_rate = new_avg_rate

    def get_current_avg_rate(self):
        return f"Student rate is {self._avg_rate}"

# Example of usage
new_student = Student('Andzej', 'Mackevic', 29, 4.5)
print(new_student.get_current_avg_rate())
new_student.set_avg_rate(4.7) # Change current average rate
print(new_student.get_current_avg_rate())