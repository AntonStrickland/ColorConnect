#Name: Anton Strickland
#CS5400 Puzzle Project 2

import node
import sys

class IDDFTS():

  __slots__ = ['gameboard', 'totalNodes', 'frontier', 'actionSet']

  def __init__(self, gameboard, actionSet):
    self.gameboard = gameboard
    self.totalNodes = 1
    self.actionSet = actionSet
    
  def Search(self, rootNode):
    print("Performing ID-DFTS...")
    for depth in range(sys.maxsize):
      result = self.DepthLimitedSearch(rootNode, depth)
      if result[1] is not ("Cutoff"):
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
            if (controller.reachedGoal is False and controller.checkMoveValidity(action, gridSize, gridSize, self.gameboard)):
              newState = controller.result(self.gameboard, currentNode.state, action)
              if (newState is not None):
                childNode = node.Node(newState, currentNode, (action, controller.id), currentNode.pathCost + 1)
                self.totalNodes = self.totalNodes + 1
                result = DepthLimitedSearch(childNode, depthLimit-1)
                if (result[1] == "Cutoff"):
                  hasBeenCutoff = True
                elif (result[1] == "Solution"):
                  return result
        if (hasBeenCutoff is True):
          return (None, "Cutoff")
        else:
          return (None, "Failure")
                
          