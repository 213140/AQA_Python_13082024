# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
from cgitb import strong
from itertools import count


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(number1, number2):
    return number1 + number2
# Function verification
print(f"Sum of 2 + 2 is {sum_two_numbers(2, 2)}")


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_of_numbers_list(input_numbers_list):
    return sum(input_numbers_list) / len(input_numbers_list)
# Function verification
input_list = [1, 2, 3, 4]
print(f"Average of list {input_list} is {average_of_numbers_list(input_list)}")


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_list(input_string):
    return input_string[::-1]
# Function verification
print(f"Reversed ABC is {reverse_list("ABC")}")


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_string(input_string_list):
    return (sorted(input_string_list))[len(input_string_list) -1]
# Function verification
input_list = ["aa", "aaa", "aaaa"]
print(f"Longest string in {input_list} is {longest_string(input_list)}")


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    return -1
# Function verification
print("Positive result testing:", find_substring("aaabbbcd", "bbb"))
print("Negative result testing:", find_substring("aaabbbcd", "bxb"))
# Initial testing
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7
str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


# task 7
# Change all letters in string into UPPER case
def all_upper_case(string1):
    return string1.upper()
# Test Function
string_for_test = ("asafdsafghgkjhbksDWSAQRCWRX")
print(f"String {string_for_test} in upper is {all_upper_case(string_for_test)}")


# task 8
#Receive and string from user
def print_user_string(entered_string):
    print(f"User entered string: {entered_string}")
# Function tetsing
print_user_string("Some string")


# task 9
#Check if unique characters quantity in the string is more than 10
def check_characters_set(entered_string):
    set_from_string = set(entered_string[::1])
    print(f"If Unique characters quantity more than 10?: {len(set_from_string) > 10}")
check_characters_set("asdfghjklzcvbn")


# task 10
# Sum of all even numbers in list
def even_numbers_sum_in_string(user_list):
    list2 = []
    for item in user_list:
        if item % 2 == 0:
            list2.append((item))
    print(f"Sum of all even numbers is {sum(list2)}")
# Test function
new_list = [1, 4, 57, 79, 6, 9, 12, 7, 9, 11, 100 ]
even_numbers_sum_in_string(new_list)