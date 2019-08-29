import unittest
from core import stock_operations

class TestStockOperations(unittest.TestCase):

    def test_max_profit_with_max_value_ahead_of_min_value(self):
        data = [1,2,3,4,5,6,7,8,9]
        expected = (1,9)
        self.assertEqual(stock_operations.most_profit(data), expected)

    def test_max_profit_with_max_value_behind_of_min_value(self):
        data = [4,5,6,7,8,9,3,2,1]
        expected = (4,9)
        self.assertEqual(stock_operations.most_profit(data), expected)

    def test_max_profit_with_just_two_different_values(self):
        data = [2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,9]
        expected = (1,9)
        self.assertEqual(stock_operations.most_profit(data), expected)

    def test_max_profit_with_tuple_type(self):
        data = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        expected = (1,9)
        self.assertEqual(stock_operations.most_profit(data), expected)

    def test_max_profit_with_set_type(self):
        data = set([1,2,3,4,5,6,7,8,9])
        expected = TypeError
        with self.assertRaises(expected):
            stock_operations.most_profit(data)

    def test_max_profit_with_string_type(self):
        data = str([1,2,3,4,5,6,7,8,9])
        expected = TypeError
        with self.assertRaises(expected):
            stock_operations.most_profit(data)

    def test_max_profit_with_int_type(self):
        data = 123456789
        expected = TypeError
        with self.assertRaises(expected):
            stock_operations.most_profit(data)

    def test_max_profit_with_decimals(self):
        data = [1.1, 1.2, 1.3, 1.4, 1.5]
        expected = (1.1,1.5)
        self.assertEqual(stock_operations.most_profit(data), expected)