########################################################
#
# CMPSC 441: Homework 3
#
########################################################


student_name = 'Type your full name here'
student_email = 'Type your email address here'



########################################################
# Import
########################################################

from hw3_utils import *
from collections import deque
import math

# Add your imports here if used




##########################################################
# 1. Best-First, Uniform-Cost, A-Star Search Algorithms
##########################################################


def best_first_search(problem):
    node = Node(problem.init_state, heuristic=problem.h(problem.init_state))
    frontier = deque([node])         # queue: popleft/append-sorted
    explored = [problem.init_state]  # used as "visited"

    pass




def uniform_cost_search(problem):
    node = Node(problem.init_state)
    frontier = deque([node])         # queue: popleft/append-sorted
    explored = []                    # used as "expanded" (not "visited")
    
    pass



    
def a_star_search(problem):
    node = Node(problem.init_state, heuristic=problem.h(problem.init_state))
    frontier = deque([node])         # queue: popleft/append-sorted
    explored = []                    # used as "expanded" (not "visited")
    
    pass




##########################################################
# 2. N-Queens Problem
##########################################################


class NQueensProblem(Problem):
    """
    The implementation of the class NQueensProblem related
    to Homework 2 is given for those students who were not
    able to complete it in Homework 2.
    
    Note that you do not have to use this implementation.
    Instead, you can use your own implementation from
    Homework 2.

    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    """
    
    def __init__(self, n):
        super().__init__(tuple([-1] * n))
        self.n = n
        

    def actions(self, state):
        if state[-1] != -1:   # if all columns are filled
            return []         # then no valid actions exist
        
        valid_actions = list(range(self.n))
        col = state.index(-1) # index of leftmost unfilled column
        for row in range(self.n):
            for c, r in enumerate(state[:col]):
                if self.conflict(row, col, r, c) and row in valid_actions:
                    valid_actions.remove(row)
                    
        return valid_actions

        
    def result(self, state, action):
        col = state.index(-1) # leftmost empty column
        new = list(state[:])  
        new[col] = action     # queen's location on that column
        return tuple(new)

    
    def goal_test(self, state):
        if state[-1] == -1:   # if there is an empty column
            return False;     # then, state is not a goal state

        for c1, r1 in enumerate(state):
            for c2, r2 in enumerate(state):
                if (r1, c1) != (r2, c2) and self.conflict(r1, c1, r2, c2):
                    return False
        return True

    
    def conflict(self, row1, col1, row2, col2):
        return row1 == row2 or col1 == col2 or abs(row1-row2) == abs(col1-col2)

    
    def g(self, cost, from_state, action, to_state):
        """
        Return path cost from start state to to_state via from_state.
        The path from start_state to from_state costs the given cost
        and the action that leads from from_state to to_state
        costs 1.
        """
        pass


    def h(self, state):
        """
        Returns the heuristic value for the given state.
        Use the total number of conflicts in the given
        state as a heuristic value for the state.
        """
        pass



##########################################################
# 3. Graph Problem
##########################################################



class GraphProblem(Problem):
    """
    The implementation of the class GraphProblem related
    to Homework 2 is given for those students who were
    not able to complete it in Homework 2.
    
    Note that you do not have to use this implementation.
    Instead, you can use your own implementation from
    Homework 2.

    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    """
    
    
    def __init__(self, init_state, goal_state, graph):
        super().__init__(init_state, goal_state)
        self.graph = graph

        
    def actions(self, state):
        """Returns the list of adjacent states from the given state."""
        return list(self.graph.get(state).keys())

    
    def result(self, state, action):
        """Returns the resulting state by taking the given action.
            (action is the adjacent state to move to from the given state)"""
        return action

    
    def goal_test(self, state):
        return state == self.goal_state

    
    def g(self, cost, from_state, action, to_state):
        """
        Returns the path cost from root to to_state.
        Note that the path cost from the root to from_state
        is the give cost and the given action taken at from_state
        will lead you to to_state with the cost associated with
        the action.
        """
        
        pass
    

    def h(self, state):
        """
        Returns the heuristic value for the given state. Heuristic
        value of the state is calculated as follows:
        1. if an attribute called 'heuristics' exists:
           - heuristics must be a dictionary of states as keys
             and corresponding heuristic values as values
           - so, return the heuristic value for the given state
        2. else if an attribute called 'locations' exists:
           - locations must be a dictionary of states as keys
             and corresponding GPS coordinates (x, y) as values
           - so, calculate and return the straight-line distance
             (or Euclidean norm) from the given state to the goal
             state
        3. else
           - cannot find nor calculate heuristic value for given state
           - so, just return a large value (i.e., infinity)
        """

        pass





##########################################################
# 4. Eight Puzzle
##########################################################


class EightPuzzle(Problem):
    def __init__(self, init_state, goal_state=(1,2,3,4,5,6,7,8,0)):
        pass
    

    def actions(self, state):
        pass

    
    def result(self, state, action):
        pass

    
    def goal_test(self, state):
        pass
    

    def g(self, cost, from_state, action, to_state):
        """
        Return path cost from root to to_state via from_state.
        The path from root to from_state costs the given cost
        and the action that leads from from_state to to_state
        costs 1.
        """
        pass
    

    def h(self, state):
        """
        Returns the heuristic value for the given state.
        Use the sum of the Manhattan distances of misplaced
        tiles to their final positions.
        """
        pass


