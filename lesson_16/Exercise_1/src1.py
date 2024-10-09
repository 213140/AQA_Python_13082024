"""
Завдання 1

Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє керівника з команди розробників.
Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
"""

class Employee:
    name = str
    salary = int


class Manager(Employee):
    department = str


class Developer(Employee):
    programming_language = str


class TeamLead(Manager, Developer):
    team_size = int