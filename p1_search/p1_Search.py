# p1_Search.py
# ---------
# Based on search.py from the UC Berkeley Pacman AI Projects.
# Original authors: John DeNero, Dan Klein, Brad Miller, Nick Hay, Pieter Abbeel.
# Original project link: http://ai.berkeley.edu
#
# Modifications for UCI EECS 118 by Mahmoud Elfar, 2025.
# This version includes changes to <TBD>.
#
# Licensing: You may use or extend this file for educational purposes
# provided that (1) solutions are not distributed or published,
# (2) this notice is retained, and (3) clear attribution to UC Berkeley is kept.


"""
In p1_Search.py, you will implement generic search algorithms which are called by
Pacman agents (in p1_SearchAgents.py).
"""

import util
from game import Directions
from typing import List

class node:
    state = None
    action = None
    previous = None
    cost = 0
    
    def __init__(self, c, a=None, p=None, price=None):
        """
        Node with no cost factor. Because we are not implementing cost factor.
        Assume c is a valid GameState object.
        Assume p is like a pointer or something idk
        No clue what datatype Actions are
        """
        self.state = c
        self.action = a
        self.previous = p
        self.cost = price if price != None else 0

class infCounter(util.Counter):
    '''
    Same as the Counter, except that the default value is infinity
    '''
    def __getitem__(self, idx):
        self.setdefault(idx, float('inf'))
        return dict.__getitem__(self, idx)

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    origin = problem.getStartState()
    originNode = node(origin)
    final = None #contains last node of search
    frontier = util.Stack()
    explored = set()

    frontier.push(originNode) #node
    while not frontier.isEmpty():
        current = frontier.pop() #node
        currentState = current.state
        if currentState in explored: #in the case we get duplicates in the frontier (from convergent/circular paths)
            continue
        if problem.isGoalState(currentState):
            final = current
            break
        succList = problem.getSuccessors(currentState)
        for succ, act, cost in succList: #iterate thru list of successors
            potential = node(succ, act, current, cost)
            if potential.state not in explored:
                frontier.push(potential) #add unexplored successor to the frontier
        explored.add(current.state) #add current node to explored set.

    if final == None:
        print("Search Failed! (DFS)")
        return []
    else:
        #construct path home
        path = []
        returnNode = final
        while returnNode.action is not None:
            print(returnNode.state, returnNode.action, returnNode.previous.state)
            path.insert(0, returnNode.action)
            returnNode = returnNode.previous
        print(returnNode)
        return path
     

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    origin = problem.getStartState()
    originNode = node(origin)
    final = None #contains last node of search
    frontier = util.Queue()
    explored = set()

    frontier.push(originNode) #node
    while not frontier.isEmpty():
        current = frontier.pop() #node
        currentState = current.state
        if currentState in explored: #in the case we get duplicates in the frontier (from convergent/circular paths)
            continue                # before we explore them the first time
        if problem.isGoalState(currentState):
            final = current
            break
        explored.add(currentState) #add current node to explored set.
        #print(currentState)
        succList = problem.getSuccessors(currentState)
        for succ, act, cost in succList: #iterate thru list of successors
            if succ not in explored:
                potential = node(succ, act, current, cost)
                frontier.push(potential) #add unexplored successor to the frontier

    if final == None:
        print("Search Failed! (BFS)")
        return []
    else:
        #construct path home
        path = []
        returnNode = final
        while returnNode.action is not None:
            #print(returnNode.state, returnNode.action, returnNode.previous.state)
            path.insert(0, returnNode.action)
            returnNode = returnNode.previous
        print(returnNode)
        return path
    

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    origin = problem.getStartState()
    originNode = node(origin)
    final = None #contains last node of search
    frontier = util.PriorityQueue()
    explored = set()

    frontier.push(originNode, originNode.cost) #node
    while not frontier.isEmpty():
        current = frontier.pop() #node
        currentState = current.state
        if currentState in explored: #in the case we get duplicates in the frontier (from convergent/circular paths)
            continue                # before we explore them the first time
        if problem.isGoalState(currentState):
            final = current
            break
        explored.add(currentState) #add current node to explored set.
        #print(currentState)
        succList = problem.getSuccessors(currentState)
        for succ, act, cost in succList: #iterate thru list of successors
            if succ not in explored:
                potential = node(succ, act, current, cost + current.cost)
                frontier.push(potential, potential.cost) #add unexplored successor to the frontier

    if final == None:
        print("Search Failed! (UCS)")
        return []
    else:
        #construct path home
        path = []
        returnNode = final
        while returnNode.action is not None:
            #print(returnNode.state, returnNode.action, returnNode.previous.state)
            path.insert(0, returnNode.action)
            returnNode = returnNode.previous
        print(returnNode)
        return path


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
