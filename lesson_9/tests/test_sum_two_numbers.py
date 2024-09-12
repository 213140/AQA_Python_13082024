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


if __name__ == '__init__':
    unittest.main()