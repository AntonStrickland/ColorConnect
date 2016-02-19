#Name: Anton Strickland
#CS5400 Puzzle Project 4

import node
import sys
import queue

class GBFTS():

  __slots__ = ['gameboard', 'gridSize', 'totalNodes', 'frontier', 'actionSet', 'endPointList', 'exploredSet']

  def __init__(self, gameboard, actionSet, endPointList):
    self.gameboard = gameboard
    self.totalNodes = 1
    self.frontier = queue.PriorityQueue()
    self.actionSet = actionSet
    self.gridSize = len(gameboard)
    self.endPointList = endPointList
    
  def ManhattanDist(self, x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
    
  def Search(self, rootNode):
    solutionFound = False

    # Begin with the root node in the frontier
    self.frontier.put(rootNode)
    self.totalNodes = 1

    while (not self.frontier.empty()):
      # Check to see if this state is the solution
      currentNode = self.frontier.get()
      solutionFound = node.CheckSolution(currentNode)
      
      # If a solution has been found, return it
      if (solutionFound):
        return currentNode
        
      # Else, expand the frontier
      self.ExpandFrontier(currentNode)
        
    return None
        
  # Expand the frontier of nodes for searching
  def ExpandFrontier(self, currentNode):
    # For each possible action that can be taken by each possible color controller
    for controller in currentNode.state.controllers:
      for action in self.actionSet:
        if controller.reachedGoal is False:
          # If this color has not already reached its endpoint and it's a valid action...
          if (controller.checkMoveValidity(action, self.gridSize, self.gridSize, self.gameboard)):
            
            # Generate a new state from the result of this state and this action
            newState = controller.result(self.gameboard, currentNode.state, action)
            
            # If a valid state has been generated...
            if (newState is not None):
            
              # The heuristic is equal to the summed Manhattan Distance from all controllers' current positions to their endpoints
              newHeuristic = 0
              for c in newState.controllers:
                newHeuristic += self.ManhattanDist(c.pos_x, c.pos_y, self.endPointList[c.id][1], self.endPointList[c.id][2])
              
              # Create a new node with this state and heuristic
              newNode = node.Node(newState, currentNode, (action, controller.id), currentNode.pathCost + 1, newHeuristic)
              
              # Add the new node to the frontier
              self.frontier.put(newNode)
              self.totalNodes = self.totalNodes + 1
            