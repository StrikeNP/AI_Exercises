import math
from random import shuffle


class Puzzle:
    '''

    '''

    # def __init__(self, dimension):
    #     '''
    #
    #     :param dimension:
    #     '''
    #     if dimension <= 0 or dimension == None:
    #         dimension = 15
    #     self.dimension = dimension
    #     self.map = [dimension][dimension]

    def __init__(self, size):
        '''
        Create a new puzzle map with at most the given size/number of
        squares. The actual number of squares will be the smallest number
        close to the size that gives an even square root. This is to say
        that the dimensions of the puzzle must be the same.

        TODO finish example

        Example: size of 15 will result in 15 blocks + 1 empty space, =  16. sqrt(16) is 4,
            so the dimensions of a size 15 will be 4. Given a size of
        :param size:
        '''
        self.size = size
        if size <= 0 or size == None:
            size = 15
        self.dimension = int(math.sqrt(size + 1))  # add 1 to ensure there is an empty space to move blocks with

        goalValues = [i for i in range(0, self.size + 1)]
        self.goal = []
        for y in range(0, self.dimension):
            self.goal.append([])
            for x in range(0, self.dimension):
                self.goal[y].append(goalValues.pop(0))

        self.size = self.dimension * self.dimension
        self.map = [[-1 for i in range(0, self.dimension)] for i in
                    range(0, self.dimension)]  # generate a 2d array and fill it with -1's
        self.space = (-1, -1)
        self.randomize()

    def toString(self):
        '''
        Get the map value as a human readable/visual string ready to be
        printed out
        :return: Current game map as a visual string
        '''
        map_string = "| -"
        for x in range(0, self.dimension):
            map_string = map_string + "----"
        map_string = map_string + " |"
        for y in range(0, self.dimension):
            map_string = map_string + "\n|"
            for x in range(0, self.dimension):
                spacer = " "
                if self.map[y][x] < 10:
                    spacer = spacer + " "
                map_string = map_string + spacer + str(self.map[y][x]) + " |"
        map_string = map_string + "\n| "
        for y in range(0, self.dimension):
            map_string = map_string + "----"
        map_string = map_string + "- |"
        return map_string

    def isGoal(self):
        '''

        :return:
        '''
        print("Testing isGoal")
        for y in range(0,self.dimension):
            for x in range(0,self.dimension):
                if self.map[y][x] != self.goal[y][x]:
                    print("Node is not goal: " + str(self.map[y][x]) + " != " + str(self.goal[y][x]))
                    return False
        return True


    def randomize(self):
        '''

        :return:
        '''
        # values = [i for i in range(0, self.size)]
        # shuffle(values)
        # for y in range(0, self.dimension):
        #     for x in range(0, self.dimension):
        #         self.map[y][x] = values.pop()
        #         if self.map[y][x] == 0:
        #             self.space = (x, y)
        self.map = [[1,2,4,7],[13,9,5,3],[15,6,14,8],[10,12,0,11]]
        # self.map = [[1,0,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
        self.space = (2,3)
        # self.space = (1,0)

    def positionExists(self, x, y):
        '''

        :param x:
        :param y:
        :return:
        '''
        if x > -1 and y > -1 and x < self.dimension and y < self.dimension:
            return True
        else:
            return False

    def getPercentCorrect(self):
        '''

        :param other:
        :return:
        '''
        num_correct = self.getNumWrong()
        percent_correct = float(num_correct) / float(self.size + 1)
        return percent_correct

    def getNumWrong(self):
        '''

        :param other:
        :return:
        '''
        num_correct = 0
        for y in range(0, self.dimension):
            for x in range(0, self.dimension):
                if self.goal[y][x] == self.map[y][x]:
                    num_correct = num_correct + 1
        num_wrong = self.size - num_correct
        return num_wrong

    def applyAction(self, x, y):
        '''

        :param x:
        :param y:
        :return:
        '''
        if not self.isNextToSpace(x, y):
            return -1
        if self.space[0] == x and self.space[1] == y:
            return -1
        self.map[self.space[1]][self.space[0]] = self.map[y][x]
        self.map[y][x] = 0
        self.space = (x, y)

    def isNextToSpace(self, x, y):
        if self.positionExists(x, y) and (x + 1, y) == self.space or (x - 1, y) == self.space or (
                x, y + 1) == self.space or (x, y - 1) == self.space:
            return True
        else:
            return False

    # def goalIndexOf(self, value):
    #     '''
    #
    #     :param value:
    #     :return:
    #     '''
    #     y = -1
    #     x = -1
    #     for row in self.goal:
    #         y = y + 1
    #         try:
    #             if row.index(value) >= 0:
    #                 x = row.index(value)
    #                 break
    #         except:
    #             continue
    #     return (x, y)

    # def indexOf(self, value):
    #     '''
    #
    #     :param value:
    #     :return:
    #     '''
    #     y = -1
    #     x = -1
    #     for row in self.map:
    #         y = y + 1
    #         try:
    #             if row.index(value) >= 0:
    #                 x = row.index(value)
    #                 break
    #         except:
    #             continue
    #
    #     return (x, y)

    def posDistFromGoal(self, x, y):
        '''

        :param x:
        :param y:
        :return:
        '''
        # value_pos = self.indexOf(value)
        value = self.map[y][x]
        # goal_a = self.goalIndexOf(value)
        goal_y = int(value / self.dimension)
        goal_x = value - (goal_y * self.dimension)
        goal = (goal_x, goal_y)
        # print("Dim="+str(self.dimension)+"  GoalA=" + str(goal) + "  Goal=" + str(goal))
        x_dist = abs(float(x) - float(goal[0]))
        y_dist = abs(float(y - float(goal[1])))
        dist = math.sqrt((x_dist * x_dist) + (y_dist * y_dist))
        return dist

    def distSum(self):
        '''

        :return:
        '''
        total = 0
        # for value in range(0, self.size):
        #     total = total + self.posDistFromGoal(value)
        for y in range(0, self.dimension):
            for x in range(0, self.dimension):
                total = total + self.posDistFromGoal(x,y)
        return total

    def __eq__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.toString().__eq__(other.toString()):
            return True
        else:
            return False

    def __ne__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getPercentCorrect() == other.getPercentCorrect():
            return False
        else:
            return True

    def __gt__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getPercentCorrect() > other.getPercentCorrect():
            return True
        else:
            return False

    def __lt__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getPercentCorrect() < other.getPercentCorrect():
            return True
        else:
            return False

    def __ge__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getPercentCorrect() >= other.getPercentCorrect():
            return True
        else:
            return False

    def __le__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getPercentCorrect() <= other.getPercentCorrect():
            return True
        else:
            return False
