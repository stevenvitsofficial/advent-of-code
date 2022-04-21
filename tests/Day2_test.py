import unittest
from src.Day2 import WrappingPaper


class TestWrappingPaper(unittest.TestCase):
    def test_OrderPaper(self):
        self.assertEqual(WrappingPaper.OrderPaper(2, 3, 4), 58)
        self.assertEqual(WrappingPaper.OrderPaper(1, 1, 10), 43)


if __name__ == '__main__':
    unittest.main()