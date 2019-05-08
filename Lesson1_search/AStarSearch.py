import heapq
import re
import time

from Lesson1_search.Puzzle import Puzzle
from copy import deepcopy

class Node:
    '''

    '''

    def __init__(self, parent, state: Puzzle, cost, depth = -1):
        '''

        '''
        self.parent = parent
        self.state = state
        # self.action = action
        self.cost = cost
        self.depth = depth

    def __hash__(self):
        '''

        :return:
        '''
        string_rep = str(self.state.map)
        hash = re.sub('[^0-9]', '', string_rep)
        return int(hash)


    def getH(self):
        '''

        :param node:
        :return:
        '''
        h1 = self.state.getNumWrong()
        h2 = self.state.distSum()
        h = max(h1, h2)
        return h

    def getChildren(self):
        '''

        :return:
        '''
        children = []

        action_x = self.state.space[0] + 1
        action_y = self.state.space[1]
        if self.state.positionExists(action_x,action_y):
            children.append(self.getChildAtPos(action_x,action_y))

        action_x = self.state.space[0] - 1
        action_y = self.state.space[1]
        if self.state.positionExists(action_x,action_y):
            children.append(self.getChildAtPos(action_x,action_y))

        action_x = self.state.space[0]
        action_y = self.state.space[1] + 1
        if self.state.positionExists(action_x,action_y):
            children.append(self.getChildAtPos(action_x,action_y))

        action_x = self.state.space[0]
        action_y = self.state.space[1] - 1
        if self.state.positionExists(action_x,action_y):
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
            if new_node.state.applyAction(x,y) != None:
                print("ERROR: invalid action specified!")
            new_node.action = (x, y)
            new_node.cost = self.cost + 1
            new_node.parent = self
            new_node.depth = self.depth + 1
            return new_node
        else:
            return None

    def getF(self):
        '''
        
        :return: 
        '''
        return self.cost + self.getH()

    # def __eq__(self, other):
    #     '''
    #
    #     :param other:
    #     :return:
    #     '''
    #     if self.state == other.state:
    #         return True
    #     else:
    #         return False

    def __ne__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getF() !=  other.getF():
            return False
        else:
            return True

    def __gt__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getF() > other.getF():
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
            # print(str(self.getF()) + " < " + str(other.getF()))
        else:
            # print(str(self.getF()) + " >= " + str(other.getF()))
            return False

    def __ge__(self, other):
        '''

        :param other:
        :return:
        '''
        if self.getF() >= other.getF():
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

    def __init__(self, start_state: Puzzle):
        '''
        
        :param head: 
        :param goal: 
        '''
        self.max_depth = 0
        self.head = Node(None, start_state, 0, 0)
        self.root = self.head
        self.goal = start_state.goal
        self.frontier_nodes = []
        heapq.heapify(self.frontier_nodes)
        self.expanded_nodes = {}
        self.frontier_nodes.append(self.head)

    def subtreeToStr(self, subtree_root: Node, depth: int):
        '''

        :param subtree_root:
        :param depth: How many nodes deep in the tree subtree_node is, this translates to number of tabs needed
        :return:
        '''
        # self.max_depth = 0
        string_result = str(subtree_root)
        for node in set(self.expanded_nodes + self.frontier_nodes):
            if node.parent == subtree_root:
                string_result = string_result + "\n"
                for i in range(0, depth):
                    string_result = string_result + "\t|"
                depth = depth + 1
                if depth > self.max_depth:
                    self.max_depth = depth
                string_result = string_result + self.subtreeToStr(node, depth)
        # for node in self.frontier_nodes:
        #     if node.parent == subtree_root:
        #         string_result = string_result + "\n"
        #         for i in range(0, depth):
        #             string_result = string_result + "\t|"
        #         depth = depth + 1
        #         string_result = string_result + self.subtreeToStr(node, depth)
        return string_result

    def getNextNode(self):
        '''
        
        :return: 
        '''
        # currentPick = self.frontier_nodes[0]
        # for node in self.frontier_nodes:
        #     if node < currentPick:
        #         currentPick = node
        #return currentPick
        return heapq.heappop(self.frontier_nodes)


    def popNextNode(self):
        '''

        :return:
        '''
        start = time.time()
        bestNode = self.getNextNode()
        end = time.time()
        # print("Getting node took: " + str(end - start))
        start = time.time()
        for child in bestNode.getChildren():
            if not self.isNodeExpanded(child):
                #self.frontier_nodes.append(child)
                heapq.heappush(self.frontier_nodes, child)
        end = time.time()
        # print("Getting children took: " + str(end - start))
        self.expanded_nodes[bestNode] = bestNode#.append(bestNode)
        # self.frontier_nodes.remove(bestNode)
        return bestNode

    def isNodeExpanded(self, node):
        '''

        :return:
        '''
        # for expanded_node in self.expanded_nodes:
        #     if node.state == expanded_node.state:
        #         return True
        #     else:
        #         return False
        if node in self.expanded_nodes.keys():
            return True
        else:
            return False

    def printTree(self):
        '''

        :return:
        '''


    def search(self):
        '''

        :return:
        '''
        goalFound = False
        for child in self.head.getChildren():
            self.frontier_nodes.append(child)
        previous_state = ""
        loop = 0
        self.max_depth = 0

        print("Starting at:\n")
        print(self.root.state.toString())
        print("Goal:")
        print(self.root.state.goal)

        while not goalFound:
            self.head = self.popNextNode()
            if self.head.depth > self.max_depth:
                self.max_depth = self.head.depth
            if self.head.state.isGoal():
                goalFound = True
            print("Loop #" + str(loop) +
                  "\tExplored: " + str(self.expanded_nodes.__len__()) +
                  "\tFrontier: " + str(self.frontier_nodes.__len__()) +
                  "\tMax Depth: " + str(self.max_depth) +
                  "\tCost: " + str(self.head.getF()) +
                  "\tHead: ", self.head)
            # print(self.head.state.toString())
            # print(self.subtreeToStr(self.root, 0))
            loop = loop + 1
        print("Done!")
        print(self.head.state.toString())
