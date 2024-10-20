"""
Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. Наслідуйте від нього декілька (> 2) інших фігур,
та реалізуйте математично вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""

from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    @abstractmethod
    def area(self):
        """ Must be implemented in subclass """
        pass

    @abstractmethod
    def perimeter(self):
        """ Must be implemented in subclass """
        pass

    def __str__(self):
        return f"Area of circle_1 is {self.area()} and perimeter is {self.perimeter()}"

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * pi

    def perimeter(self):
        return 2 * pi * self.__radius

class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return self.__side * 4

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def area(self):
        return  self.__side_a * self.__side_b

    def perimeter(self):
        return (self.__side_a * 2) + (self.__side_b * 2)


if __name__ == '__main__':
    # Test all subclasses
    # Circle
    circle_1 = Circle(5)
    print(circle_1)
    # Square
    square_1 = Square(2)
    print(square_1)
    # Rectangle
    rectangle_1 = Rectangle(2, 3)
    print(rectangle_1)