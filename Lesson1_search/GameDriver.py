import sys
from Lesson1_search.Puzzle import Puzzle


def main(args):
    puzzle = Puzzle(15)
    print(puzzle.toString())

if  __name__ == '__main__':
    main(sys.argv)