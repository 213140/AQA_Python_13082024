import unittest
import lesson_9.src.homeworks as my_functions

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


if __name__ == '__init__':
    unittest.main()