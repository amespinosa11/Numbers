import unittest
import numbers


class TestNumbers(unittest.TestCase):
    def test_amountNumbers_empty(self):
        self.assertEqual(numbers.get_amount_numbers(""), [0])

    def test_amountNumbers_one_element(self):
        self.assertEqual(numbers.get_amount_numbers("2"), [1])


if __name__ == '__main__':
    unittest.main()
