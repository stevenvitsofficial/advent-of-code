import unittest
from src.Day2 import WrappingPaper


class TestDay2(unittest.TestCase):
    def test_OrderPaper(self):
        self.assertEqual(WrappingPaper.OrderPaper(2, 3, 4), 58)
        self.assertEqual(WrappingPaper.OrderPaper(1, 1, 10), 43)

    def test_OrderPaperNotNumbers(self):
        with self.assertRaises(Exception):
            WrappingPaper.OrderPaper("x", 2, 3)

    def test_OrderPaperNegativeNumbers(self):
        with self.assertRaises(Exception):
            WrappingPaper.OrderPaper(-1, 2, 3)

if __name__ == '__main__':
    unittest.main()