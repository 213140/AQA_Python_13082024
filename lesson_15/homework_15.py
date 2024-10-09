# Homework description in Ukrainian
# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод setattr.

class Rhombus:

    def __setattr__(self, name, value):
        if name == 'side_a' and value <= 0:
            raise ValueError('Side a can`t be less or equal zero!')
        else:
            super().__setattr__(name , value)

        if name == 'corner_a' and value >= 180:
            raise ValueError('Corner can not be bigger or equal to 180!')
        else:
            super().__setattr__(name , value)
            super().__setattr__('corner_b', 180 - value)

    def __str__(self):
        return f"Figure side lenght is {self.side_a} and contains two corners {self.corner_a} and {self.corner_b}"


# Test new Rhombus class
rhombus_1 = Rhombus()
setattr(rhombus_1, 'side_a', 10)
setattr(rhombus_1, 'corner_a', 100)
print(rhombus_1)
# Try to change params
# rhombus_1.side_a = -5 # error raise expected by __setattr__ method
# rhombus_1.corner_a = 200 # error raise expected by __setattr__ method

