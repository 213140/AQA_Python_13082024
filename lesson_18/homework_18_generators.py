# Генератори:
#
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.


def even_numbers_generator(n):
    start = 0
    while start < n:
        yield start
        start += 2

def fibonachi_numbers_generator(n):
    a, b = 0, 1
    while 0 <= a & a < n:
        yield a
        a, b = b, a + b


### Check even_numbers_generator
gen1 = even_numbers_generator(11)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# print(next(gen1))  # StopIteration error appear
print('_' * 30)

### Check even_numbers_generator
gen2 = fibonachi_numbers_generator(1000)
while True:
    try:
        print(next(gen2))
    except StopIteration:
        break
print('_' * 30)
