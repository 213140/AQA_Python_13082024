# Декоратори:
#
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def logging_decorator(func):
    def wrapper(*args):
        func(*args)
        logging.info(f"Function used as input city name: {args[0]}, city residence: {args[1]}")
    return wrapper

# # 1 way of using
@logging_decorator
def some_function(city_name: str, city_residents: int):
    print(f"City name is {city_name} and has {city_residents} residents")
# Check if decorator works
some_function('Warsaw', 800000)

# 2 way of using
def some_function(city_name: str, city_residents: int):
     print(f"City name is {city_name} and has {city_residents} residents")
# Crete copy of original function
copy_of_function = some_function
# Connect copy with decorator
dec2_with_func = logging_decorator(copy_of_function)
# Call both: copy with deco. and original function
dec2_with_func('Warsaw', 800000)
copy_of_function('Warsaw', 800000)




