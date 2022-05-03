import unittest
from src.Day1 import Elevator


class TestDay2(unittest.TestCase):
    def test_MoveElevator(self):
        self.assertEqual(Elevator.MoveElevator('(())'), 0)
        self.assertEqual(Elevator.MoveElevator('()()'), 0)
        self.assertEqual(Elevator.MoveElevator('((('), 3)
        self.assertEqual(Elevator.MoveElevator('(()(()('), 3)
        self.assertEqual(Elevator.MoveElevator('())'), -1)
        self.assertEqual(Elevator.MoveElevator('))('), -1)
        self.assertEqual(Elevator.MoveElevator(')))'), -3)
        self.assertEqual(Elevator.MoveElevator(')())())'), -3)

    def test_MoveElevatorWrongCommand(self):
        with self.assertRaises(Exception):
            Elevator.MoveElevator('i()(')


if __name__ == '__main__':
    unittest.main()
