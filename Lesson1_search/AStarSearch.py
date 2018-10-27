from Lesson1_search.Puzzle import Puzzle
from copy import deepcopy

class Node:
    '''

    '''

    def __init__(self, parent, state: Puzzle, cost):
        '''

        '''
        self.parent = parent
        self.state = state
        # self.action = action
        self.cost = cost

    def getH(self):
        '''

        :param node:
        :return:
        '''
        h1 = self.state.getNumCorrect()
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
        self.head = Node(None, start_state, 0)
        self.root = self.head
        self.goal = start_state.goal
        self.frontier_nodes = []
        self.expanded_nodes = []
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
        currentPick = self.frontier_nodes[0]
        for node in self.frontier_nodes:
            if node < currentPick:
                # print("node " + str(node.getF()) + " < currentPick " + str(currentPick.getF()))
                currentPick = node
        return currentPick

    def popNextNode(self):
        '''

        :return:
        '''
        bestNode = self.getNextNode()
        for child in bestNode.getChildren():
            if not self.isNodeExpanded(child):
                self.frontier_nodes.append(child)
        self.expanded_nodes.append(bestNode)
        self.frontier_nodes.remove(bestNode)
        return bestNode

    def isNodeExpanded(self, node):
        '''

        :return:
        '''
        for expanded_node in self.expanded_nodes:
            if node.state == expanded_node.state:
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
        while not goalFound:
            head = self.popNextNode()
            if (head == goalFound):
                goalFound = True
            # if previous_state != head.state.toString():
            #     # print("New state:\n" + head.state.toString())
            #     print("f is  " + str(head.getF()))
            # else:
            #     print("No new state")
            # previous_state = head.state.toString()
            print("Loop #" + str(loop) + "  Explored: " + str(self.expanded_nodes.__len__()) + " Frontier: " \
                  + str(self.frontier_nodes.__len__()) + " Max Depth: " + str(self.max_depth))
            print(self.subtreeToStr(self.root, 0))
            loop = loop + 1
        print("Done!")
        print(self.head.state.toString())
