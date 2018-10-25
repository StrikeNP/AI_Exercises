import sys
from Lesson1_search.Puzzle import Puzzle
from Lesson1_search.AStarSearch import AStarSearch


def main(args):
    puzzle = Puzzle(15)
    a_star = AStarSearch(puzzle)
    a_star.search()
    print(a_star.head.state.toString())

if  __name__ == '__main__':
    main(sys.argv)