import unittest
from Lesson1_search.Puzzle import *

class MyTestCase(unittest.TestCase):



    def test_posDistFromGoal(self):
        puzzle = Puzzle()
        override_map = [[1,2,4,7],    # 0,1,2,3
                        [13,9,5,3],   # 4,5,6,7
                        [15,6,14,8],  # 8,9,10,11
                        [10,12,0,11]] #12,13,14,15

        override_space = (2,3)
        puzzle.set_puzzle(override_map, override_space)

        self.assertAlmostEqual(puzzle.posDistFromGoal(0,0), 1, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(1,0), 1, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(2,0), 2.236, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(3,0), 1, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(0,1), 2.236, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(1,1), 1, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(2,1), 1, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(3,1), 1, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(0,2), 3.162, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(1,2), 1.414, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(2,2), 1, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(3,2), 3, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(0,3), 2.236, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(1,3), 1, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(2,3), 3.606, 2)
        self.assertAlmostEqual(puzzle.posDistFromGoal(3,3), 1, 2)


    def test_distSum(self):
        puzzle = Puzzle()
        override_map = [[1,2,4,7],    # 0,1,2,3
                        [13,9,5,3],   # 4,5,6,7
                        [15,6,14,8],  # 8,9,10,11
                        [10,12,0,11]] #12,13,14,15

        override_space = (2,3)
        puzzle.set_puzzle(override_map, override_space)

        distSum = puzzle.distSum()

        self.assertAlmostEqual(distSum, 26.89, 2)

if __name__ == '__main__':
    unittest.main()
