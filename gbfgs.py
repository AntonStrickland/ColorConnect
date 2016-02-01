#Name: Anton Strickland
#CS5400 Puzzle Project 2

import node
import sys
import visual
import queue

class GBFGS():

  __slots__ = ['gameboard', 'gridSize', 'totalNodes', 'frontier', 'actionSet', 'endPointList', 'exploredSet']

  def __init__(self, gameboard, actionSet, endPointList):
    self.gameboard = gameboard
    self.totalNodes = 1
    self.frontier = queue.Queue()
    self.actionSet = actionSet
    self.gridSize = len(gameboard)
    self.endPointList = endPointList
    self.exploredSet = []
    
  def ManhattanDist(self, x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
    
  # Perform the BFTS algorithm
  def Search(self, rootNode):

    print("Performing GBFGS...")
    solutionFound = False
    del self.exploredSet[:]

    # Begin with the root node in the frontier
    self.frontier.put(rootNode)
    self.totalNodes = 1

    while (not self.frontier.empty()):
      # Check to see if this state is the solution
      currentNode = self.frontier.get()
      solutionFound = node.CheckSolution(currentNode)
      
      # If a solution has been found, return it. Else, expand frontier.
      if (solutionFound):
        return currentNode
        
      self.exploredSet.append(currentNode)
      self.ExpandFrontier(currentNode)
        
    print("No solution found.")
    return None
        
  # Expand the frontier of nodes for searching
  def ExpandFrontier(self, currentNode):
    # For each possible action that can be taken by each possible color controller
    for controller in currentNode.state.controllers:
      for action in self.actionSet:
        if controller.reachedGoal is False:
          # If this color has not already reached its endpoint and it's a valid action, then add the resulting state to the frontier
          if (controller.checkMoveValidity(action, self.gridSize, self.gridSize, self.gameboard)):
            newState = controller.result(self.gameboard, currentNode.state, action)
            if (newState is not None):
              #newHeuristic = self.ManhattanDist(controller.pos_x, controller.pos_y, self.endPointList[controller.id][1], self.endPointList[controller.id][2])
              newNode = node.Node(newState, currentNode, (action, controller.id), currentNode.pathCost + 1)
              if ((newNode not in self.exploredSet)):
                self.frontier.put(newNode)
                self.totalNodes = self.totalNodes + 1
                # print(self.totalNodes)
            