import unittest
import lesson_9.src.homeworks as my_functions

class TestSumTwoNumbersFunction(unittest.TestCase):

    def test_sum_two_numbers_positive_numbers(self):
        result = my_functions.sum_two_numbers(1, 4)
        self.assertEqual(result, 5)

    def test_sum_two_numbers_negative_numbers(self):
        result = my_functions.sum_two_numbers(-1, -4)
        self.assertEqual(result, -5)

    def test_sum_two_numbers_mixed_numbers(self):
        result = my_functions.sum_two_numbers(-1, 4)
        self.assertEqual(result, 3)


class TestAverageOfNumbersList(unittest.TestCase):

    def test_average_of_numbers_list_positive(self):
        result = my_functions.average_of_numbers_list([1, 2, 3])
        self.assertEqual(result, 2)

    def test_average_of_numbers_list_negative(self):
        result = my_functions.average_of_numbers_list([-1, -2, -3])
        self.assertEqual(result, -2)

    def test_average_of_numbers_list_mixed(self):
        result = my_functions.average_of_numbers_list([2, -2, 6])
        self.assertEqual(result, 2)


class TestReverseList(unittest.TestCase):

    def test_reverse_list_of_positive_numbers(self):
        result = my_functions.reverse_list([1, 2, 3])
        self.assertEqual(result, [3, 2, 1])

    def test_reverse_list_of_negative_numbers(self):
        result = my_functions.reverse_list([-1, -2, -3])
        self.assertEqual(result, [-3, -2, -1])

    def test_reverse_list_of_letters(self):
        result = my_functions.reverse_list(['a', 'b', 'c'])
        self.assertEqual(result, ['c', 'b', 'a'])

    def test_reverse_list_of_special_characters(self):
        result = my_functions.reverse_list(['@', '#', '$'])
        self.assertEqual(result, ['$', '#', '@'])

if __name__ == '__init__':
    unittest.main()