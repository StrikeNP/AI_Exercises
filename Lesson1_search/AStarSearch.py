from Lesson1_search.Puzzle import Puzzle
from copy import deepcopy

class Node:
    '''

    '''

    def __init__(self, parent, state: Puzzle, action, cost):
        '''

        '''
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost

    def getH(self):
        '''

        :param node:
        :return:
        '''
        return self.state.getNumCorrect()

    def getChildren(self):
        '''

        :return:
        '''
        children = []

        action_x = self.state.space[0] + 1
        action_y = self.state.space[1]
        if self.state.positionExists(action_x,action_y) and (action_x,action_y) != self.state.space:
            children.append(self.getChildAtPos(action_x,action_y))
        action_x = self.state.space[0] - 1
        action_y = self.state.space[1]
        if self.state.positionExists(action_x,action_y) and (action_x,action_y) != self.state.space:
            children.append(self.getChildAtPos(action_x,action_y))
        action_x = self.state.space[0]
        action_y = self.state.space[1] + 1
        if self.state.positionExists(action_x,action_y) and (action_x,action_y) != self.state.space:
            children.append(self.getChildAtPos(action_x,action_y))
        action_x = self.state.space[0]
        action_y = self.state.space[1] - 1
        if self.state.positionExists(action_x,action_y) and (action_x,action_y) != self.state.space:
            children.append(self.getChildAtPos(action_x,action_y))

        return children


    def getChildAtPos(self,x,y):
        '''

        :param x:
        :param y:
        :return:
        '''
        if self.state.isNextToSpace(x,y):
            new_node = deepcopy(self)
            new_node.applyAction(x,y)
            new_node.cost =  self.cost + 1
            new_node.parent = self
            return new_node
        else:
            return None

    def getF(self):
        '''
        
        :return: 
        '''
        return self.cost + self.getH()

    def __eq__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.state == other.state:
            return True
        else:
            return False

    def __ne__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getF() ==  other.getF():
            return False
        else:
            return True

    def __gt__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getF() >  other.getF():
            return True
        else:
            return False

    def __lt__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getF() < other.getF():
            return True
        else:
            return False

    def __ge__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getF() >=  other.getF():
            return True
        else:
            return False

    def __le__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getF() <= other.getF():
            return True
        else:
            return False

class AStarSearch:
    '''
    
    '''

    def __init__(self, head: Node, goal: Puzzle):
        '''
        
        :param head: 
        :param goal: 
        '''
        self.head = head
        self.goal = goal
        self.frontier_nodes = []
        self.expanded_nodes = []
        self.frontier_nodes.append(head)

    def getNextNode(self):
        '''
        
        :return: 
        '''
        currentPick = self.frontier_nodes[0]
        for node in self.frontier_nodes:
            if node < currentPick:
                currentPick = node
        return currentPick

    def popNextNode(self):
        '''

        :return:
        '''
        bestNode = self.getNextNode()
        for child in bestNode.getChildren():
            self.frontier_nodes.append(child)
