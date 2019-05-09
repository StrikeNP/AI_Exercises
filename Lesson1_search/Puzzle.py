import math
import random


class Puzzle:
    '''

    '''
    def __init__(self, size = 15):
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

        self.goal = self.generate_goal()
        self.size = self.dimension * self.dimension
        self.map = self.generate_goal()
        self.space = (0, 0)


    def generate_goal(self):
        '''
        Generate the incrementing map goal state
        Example
        0,1,2,3
        4,5,6,7
        8,9,10,11
        12,13,14,15
        :return: The desired goal state
        '''
        goalValues = [i for i in range(0, self.size + 1)]
        goal = []
        for y in range(0, self.dimension):
            goal.append([])
            for x in range(0, self.dimension):
                goal[y].append(goalValues.pop(0))
        return goal

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
        # print("Testing isGoal")
        for y in range(0,self.dimension):
            for x in range(0,self.dimension):
                if self.map[y][x] != self.goal[y][x]:
                    # print("Node is not goal: " + str(self.map[y][x]) + " != " + str(self.goal[y][x]))
                    return False
        return True


    def shuffle(self, num_moves = 10):
        '''
        Apply num_moves amount of random plays/
        moves to the game board
        :param num_moves:
        :return:
        '''
        for i in range(num_moves):
            move_successful = False
            prev_direction = -1
            up = 0
            down = 1
            left = 2
            right = 3
            while move_successful is False:
                direction = random.randint(0, 3)
                if direction == up and prev_direction != down:
                    move_successful = self.move_up()
                    prev_direction = up
                if direction == down and prev_direction != up:
                    move_successful = self.move_down()
                    prev_direction = down
                if direction == left and prev_direction != right:
                    move_successful = self.move_left()
                    prev_direction = left
                if direction == right and prev_direction != left:
                    move_successful = self.move_right()
                    prev_direction = right


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
        Move the space to an x,y coordinate
        adjacent to the space's current position
        :param x:
        :param y:
        :return:
        '''
        if not self.positionExists(x, y):
            return -1
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

    def posDistFromGoal(self, x, y):
        '''

        :param x:
        :param y:
        :return:
        '''
        value = self.map[y][x]
        goal_y = int(value / self.dimension)
        goal_x = value - (goal_y * self.dimension)
        goal = (goal_x, goal_y)
        x_dist = abs(float(x) - float(goal[0]))
        y_dist = abs(float(y - float(goal[1])))
        dist = math.sqrt((x_dist * x_dist) + (y_dist * y_dist))
        return dist

    def move_up(self):
        '''
        Move the space up one square if possible, otherwise
        do nothing
        :return: True if move succeeds, false otherwise
        '''
        space_x, space_y = self.space
        if self.applyAction(space_x, space_y - 1) == -1:
            return False
        return True


    def move_down(self):
        '''
        Move the space down one square if possible, otherwise
        do nothing
        :return: True if move succeeds, false otherwise
        '''
        space_x, space_y = self.space
        if self.applyAction(space_x, space_y + 1) == -1:
            return False
        return True

    def move_left(self):
        '''
        Move the space left one square if possible, otherwise
        do nothing
        :return: True if move succeeds, false otherwise
        '''
        space_x, space_y = self.space
        if self.applyAction(space_x - 1, space_y) == -1:
            return False
        return True

    def move_right(self):
        '''
        Move the space right one square if possible, otherwise
        do nothing
        :return: True if move succeeds, false otherwise
        '''
        space_x, space_y = self.space
        if self.applyAction(space_x + 1, space_y) == -1:
            return False
        return True

    def distSum(self):
        '''

        :return:
        '''
        total = 0
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

    def set_puzzle(self,map, space):
        '''

        :param map:
        :param space:
        :return:
        '''
        self.map = map
        self.space = space

