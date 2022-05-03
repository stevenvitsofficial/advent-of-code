import unittest
from src.Day4 import CoinMiner
from src.exceptions import *


class MyTestCase(unittest.TestCase):
    def test_Mining(self):
        self.assertEqual(CoinMiner.Mine('abcdef'), 609043)
        self.assertEqual(CoinMiner.Mine('pqrstuv'), 1048970)

    def test_MiningNotString(self):
        with self.assertRaises(InputValueNotStringError):
            CoinMiner.Mine(4532452435)

if __name__ == '__main__':
    unittest.main()
