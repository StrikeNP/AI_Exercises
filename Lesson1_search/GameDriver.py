import sys
import Puzzle


def main(args):
    puzzle = Puzzle.Puzzle(15)
    print(puzzle.toString())

if  __name__ == '__main__':
    main(sys.argv)