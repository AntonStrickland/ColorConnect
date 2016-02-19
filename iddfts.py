#Name: Anton Strickland
#CS5400 Puzzle Project 4

import node
import sys

class IDDFTS():

  __slots__ = ['gameboard', 'gridSize', 'totalNodes', 'actionSet']

  def __init__(self, gameboard, actionSet):
    self.gameboard = gameboard
    self.totalNodes = 1
    self.actionSet = actionSet
    self.gridSize = len(gameboard)
    
  def Search(self, rootNode):
    for depth in range(sys.maxsize):
      print(depth)
      self.totalNodes = 1
      result = self.DepthLimitedSearch(rootNode, depth)
      if result[1] != "Cutoff":
        print(self.totalNodes)
        return result[0]
        
  def DepthLimitedSearch(self, currentNode, depthLimit):
      if node.CheckSolution(currentNode) is True:
        return (currentNode, "Solution")
      elif depthLimit == 0:
        return (None, "Cutoff")
      else:
        hasBeenCutoff = False
        for controller in currentNode.state.controllers:
          for action in self.actionSet:
            if (controller.reachedGoal is False and controller.checkMoveValidity(action, self.gridSize, self.gridSize, self.gameboard)):
              newState = controller.result(self.gameboard, currentNode.state, action)
              if (newState is not None):
                childNode = node.Node(newState, currentNode, (action, controller.id), currentNode.pathCost + 1)
                self.totalNodes = self.totalNodes + 1
                result = self.DepthLimitedSearch(childNode, depthLimit-1)
                if (result[1] == "Cutoff"):
                  hasBeenCutoff = True
                elif (result[1] == "Solution"):
                  return result
        if (hasBeenCutoff is True):
          return (None, "Cutoff")
        else:
          return (None, "Failure")
                
          