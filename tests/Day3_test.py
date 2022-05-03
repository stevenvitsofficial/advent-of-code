import unittest
from src.Day3 import Santa
from src.exceptions import *

class TestDay3(unittest.TestCase):
    def test_VisitHouses(self):
        self.assertEqual(Santa.VisitHouses('>'), 2)
        self.assertEqual(Santa.VisitHouses('^>v<'), 4)
        self.assertEqual(Santa.VisitHouses('^v^v^v^v^v'), 2)

    def test_VisitHousesWrongCommand(self):
        with self.assertRaises(InvalidInputCharacterError):
            Santa.VisitHouses('ix0()(')

if __name__ == '__main__':
    unittest.main()
