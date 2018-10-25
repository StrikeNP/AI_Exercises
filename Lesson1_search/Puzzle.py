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
        self.dimension = int(math.sqrt(size + 1)) # add 1 to ensure there is an empty space to move blocks with

        goalValues = [i for i in range(0,self.size + 1)]
        self.goal = []
        for y in range (0,self.dimension):
            self.goal.append([])
            for x in range (0, self.dimension):
                self.goal[y].append(goalValues.pop(0))

        self.size = self.dimension * self.dimension
        self.map = [[-1 for i in range(0,self.dimension)] for i in range(0, self.dimension)] # generate a 2d array and fill it with -1's
        self.space = (-1,-1)
        self.randomize()

    def toString(self):
        '''
        Get the map value as a human readable/visual string ready to be
        printed out
        :return: Current game map as a visual string
        '''
        # TODO return puzzle state as visual string
        map_string = "| -"
        for x in range(0,self.dimension):
            map_string = map_string + "----"
        map_string = map_string + " |"
        for y in range(0,self.dimension):
            map_string = map_string + "\n|"
            for x in range(0, self.dimension):
                spacer = " "
                if self.map[x][y] < 10:
                    spacer = spacer + " "
                map_string = map_string  + spacer + str(self.map[x][y]) + " |"
        map_string = map_string + "\n| "
        for y in range(0,self.dimension):
            map_string = map_string + "----"
        map_string = map_string + "- |"
        return map_string


    def randomize(self):
        '''

        :return:
        '''
        # TODO randomize the playspace
        values = [i for i in range(0,self.size)]
        shuffle(values)
        for y in range(0,self.dimension):
            for x in range(0,self.dimension):
                if x == 0:
                    self.space = (x,y)
                self.map[x][y] = values.pop()

    def positionExists(self,x,y):
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
        num_correct = self.getNumCorrect()
        percent_correct = float(num_correct)/float(self.size + 1)
        return percent_correct

    def getNumCorrect(self):
        '''

        :param other:
        :return:
        '''
        num_correct = 0
        for y in range(0,self.dimension):
            for x in range(0, self.dimension):
                if self.goal[x][y] == self.map[x][y]:
                    num_correct = num_correct + 1
        return num_correct

    def applyAction(self,x,y):
        '''

        :param x:
        :param y:
        :return:
        '''
        if not self.isNextToSpace(x,y):
            return -1
        self.map[self.space[0]][self.space[1]] = self.map[x][y]
        self.map[x][y] = 0
        self.space = (x,y)

    def isNextToSpace(self, x, y):
        if self.positionExists(x,y) and (x + 1 ,y) == self.space or (x - 1 ,y) == self.space or (x,y + 1) == self.space or (x,y - 1) == self.space:
            return True
        else:
            return False

    def __eq__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.map == other.map:
            return True
        else:
            return False

    def __ne__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getPercentCorrect() ==  other.getPercentCorrect():
            return False
        else:
            return True

    def __gt__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getPercentCorrect() >  other.getPercentCorrect():
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
        if self.getPercentCorrect() >=  other.getPercentCorrect():
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