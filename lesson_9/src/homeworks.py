# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(number1, number2):
    return number1 + number2
# Function verification
# print(f"Sum of 2 + 2 is {sum_two_numbers(2, 2)}")


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_of_numbers_list(input_numbers_list):
    return sum(input_numbers_list) / len(input_numbers_list)
# Function verification
# input_list = [1, 2, 3, 4]
# print(f"Average of list {input_list} is {average_of_numbers_list(input_list)}")


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_list(input_string):
    return input_string[::-1]
# Function verification
# print(f"Reversed ABC is {reverse_list('ABC')}")


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_string(input_string_list):
    return (sorted(input_string_list))[len(input_string_list) - 1]
# Function verification
# input_list = ["aa", "aaa", "aaaa"]
# print(f"Longest string in {input_list} is {longest_string(input_list)}")


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    return -1
# Function verification
# print("Positive result testing:", find_substring("aaabbbcd", "bbb"))
# print("Negative result testing:", find_substring("aaabbbcd", "bxb"))
# Initial testing
# str1 = "Hello, world!"
# str2 = "world"
# print(find_substring(str1, str2)) # поверне 7
# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
# print(find_substring(str1, str2)) # поверне -1