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
        self.GOAL = [i for i in range(0,self.size)]
        if size <= 0 or size == None:
            size = 15
        self.dimension = int(math.sqrt(size + 1)) # add 1 to ensure there is an empty space to move blocks with
        self.size = self.dimension * self.dimension
        self.map = [[-1 for i in range(0,size)] for i in range(0,size)] # generate a 2d array and fill it with -1's
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
                self.map[x][y] = values.pop()

    def getPercentCorrect(self):
        '''

        :param other:
        :return:
        '''
        num_correct = 0.0
        for y in range(0,self.dimension):
            for x in range(0, self.dimension):
                if self.GOAL[x][y] == self.map[x][y]:
                    num_correct = num_correct + 1.0
        percent_correct = num_correct/(self.size + 1)
        return percent_correct

    def __eq__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getPercentCorrect() == other.getPercentCorrect():
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