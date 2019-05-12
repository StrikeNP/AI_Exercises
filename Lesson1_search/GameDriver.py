import sys
import time
from matplotlib import pyplot as plt

from Lesson1_search.Puzzle import Puzzle
from Lesson1_search.AStarSearch import AStarSearch


def main(args):
    num_trials = 10000
    solution_times = []
    solution_sizes = []
    plot_every = 500
    max_len = 20

    for i in range(1,num_trials+1):
        print("\rRunning game number ", i, '/', num_trials)
        runtime, solution_size = run_timed_search(max_len=max_len)
        solution_times.append(runtime)
        solution_sizes.append(solution_size)
        with open('data.csv', 'a') as fd:
            fd.write(str(solution_size) + "," + str(runtime)+"\n")
        if i % plot_every == 0:
            plotScatter(solution_sizes, solution_times, "A_Star_time-to-solution_" + str(i)+"-samples_max-len-" + str(max_len), "Length of solution",
                        "Time taken to solve (s)")
    # plotScatter(solution_sizes, solution_times, "A_Star_time-to-solution", "Length of solution", "Time taken to solve (s)")
    # print("Solution:\n")
    # a_star.printSolution()


def plotScatter(xvalues, yvalues, title, xlabel, ylabel):
    '''
    Plots a case onto a set of graphs (panels)
    :return:
    '''
    plt.figure()
    plt.subplot(111)
    plt.scatter(xvalues, yvalues)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.savefig(title + '.png')


def run_timed_search(max_len = 20):
    '''

    :return:
    '''
    starttime = time.time()
    puzzle = Puzzle(15)
    puzzle.shuffle(max_len)
    a_star = AStarSearch(puzzle)
    a_star.search()
    runtime = time.time() - starttime
    a_star.getSolution()
    # a_star.printSolution()
    solution_size = a_star.solution_len
    # frontier_size
    return runtime, solution_size


if  __name__ == '__main__':
    main(sys.argv)