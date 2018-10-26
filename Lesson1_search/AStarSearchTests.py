import unittest
from Lesson1_search.AStarSearch import *
from Lesson1_search.Puzzle import *

class MyTestCase(unittest.TestCase):



    def test_getH(self):
        puzzle = Puzzle()
        test_node = Node(None, puzzle, 0)
        test_child = Node(test_node,puzzle,0)

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
