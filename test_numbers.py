import unittest
import numbers


class TestNumbers(unittest.TestCase):
    def test_amountNumbers_empty(self):
        self.assertEqual(numbers.get_amount_numbers(""), [0])

    def test_amountNumbers_one_element(self):
        self.assertEqual(numbers.get_amount_numbers("2"), [1])

    def test_amountNumbers_two_elements(self):
        self.assertEqual(numbers.get_amount_numbers("2,5"), [2])

    def test_amountNumbers_n_elements(self):
        self.assertEqual(numbers.get_amount_numbers("2,5,10,3,311"), [5])

    def test_min_number_empty(self):
        self.assertEqual(numbers.get_min_number(""), [0, 0])

if __name__ == '__main__':
    unittest.main()
