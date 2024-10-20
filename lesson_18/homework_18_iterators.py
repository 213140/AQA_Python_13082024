# Ітератори:
#
# Реалізуйте ітератор для зворотного виведення елементів списку.
# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class IteratorReverseList:
    def __init__(self, initial_list: list):
        self.current_position = 0
        self.initial_list = initial_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_position <= 0 & self.current_position < self.initial_list.__len__() * -1:
            self.current_position -= 1
            return self.initial_list[self.current_position]
        else:
            return StopIteration

class IterEvenNumbers:
    def __init__(self, n: int):
        self.current = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current + 2 <= self.n:
            self.current += 2
            if self.current % 2 == 0:
                return self.current
        else:
            raise StopIteration

### Check iterators
iter1 = IteratorReverseList([0, 1, 'b', 'middle', True, 'END'])
while True:
    print(next(iter1))

iter2 = IterEvenNumbers(15)
while True:
    print(next(iter2))


