import unittest 
import numbers

class TestNumbers(unittest.TestCase):
    def test_amountNumbers_empty(self):
        self.assertEqual(numbers.get_amount_numbers(""), [0])


if __name__ == '__main__':
    unittest.main()