import unittest
from lesson_9.src.homeworks import average_of_numbers_list

class TestAverageOfNumbersList(unittest.TestCase):

    def test_average_of_numbers_list_positive(self):
        result = average_of_numbers_list([1, 2, 3])
        self.assertEqual(result, 2)

    def test_average_of_numbers_list_negative(self):
        result = average_of_numbers_list([-1, -2, -3])
        self.assertEqual(result, -2)

    def test_average_of_numbers_list_mixed(self):
        result = average_of_numbers_list([2, -2, 6])
        self.assertEqual(result, 2)


if __name__ == '__init__':
    unittest.main(verbosity=2)