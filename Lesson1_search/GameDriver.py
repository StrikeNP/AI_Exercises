import sys
from Lesson1_search.Puzzle import Puzzle
from Lesson1_search.AStarSearch import AStarSearch


def main(args):
    puzzle = Puzzle(15)
    puzzle.shuffle(30)
    a_star = AStarSearch(puzzle)
    a_star.search()
    print("Solution:\n")
    a_star.printSolution()

if  __name__ == '__main__':
    main(sys.argv)