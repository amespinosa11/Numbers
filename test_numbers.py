import unittest
import numbers


class TestNumbers(unittest.TestCase):
    def test_info_numbers_empty(self):
        self.assertEqual(numbers.get_info_numbers(""), [0, 0])

    def test_info_numbers_one_element(self):
        self.assertEqual(numbers.get_info_numbers("2"), [1])

    def test_info_numbers_two_elements(self):
        self.assertEqual(numbers.get_info_numbers("2,5"), [2])

    def test_info_numbers_n_elements(self):
        self.assertEqual(numbers.get_info_numbers("2,5,10,3,311"), [5])


if __name__ == '__main__':
    unittest.main()
