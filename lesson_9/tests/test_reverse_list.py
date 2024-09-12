import unittest
import lesson_9.src.homeworks as my_functions

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