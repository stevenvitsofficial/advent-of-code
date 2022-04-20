import unittest
from src.Day1 import Elevator


class TestElevator(unittest.TestCase):
    def test_MoveElevator(self):
        self.assertEqual(Elevator.MoveElevator('(())'), 0)
        self.assertEqual(Elevator.MoveElevator('()()'), 0)
        self.assertEqual(Elevator.MoveElevator('((('), 3)
        self.assertEqual(Elevator.MoveElevator('(()(()('), 3)
        self.assertEqual(Elevator.MoveElevator('())'), -1)
        self.assertEqual(Elevator.MoveElevator('))('), -1)
        self.assertEqual(Elevator.MoveElevator(')))'), -3)
        self.assertEqual(Elevator.MoveElevator(')())())'), -3)


if __name__ == '__main__':
    unittest.main()
