#Name: Anton Strickland
#CS5400 Puzzle Project 4

import node
import sys
import visual
import queue

class ASTAR():

  __slots__ = ['gameboard', 'gridSize', 'totalNodes', 'frontier', 'actionSet', 'startPointList', 'endPointList', 'exploredSet']

  def __init__(self, gameboard, actionSet, startPointList, endPointList):
    self.gameboard = gameboard
    self.totalNodes = 1
    self.frontier = queue.PriorityQueue(sys.maxsize)
    self.actionSet = actionSet
    self.gridSize = len(gameboard)
    self.startPointList = startPointList
    self.endPointList = endPointList
    self.exploredSet = []
    
  def ManhattanDist(self, x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
    
  def Search(self, rootNode):


    solutionFound = False
    del self.exploredSet[:]

    # Begin with the root node in the frontier
    self.frontier.put( (rootNode.heuristic, rootNode) )
    self.totalNodes = 1

    while (not self.frontier.empty()):
      # Check to see if this state is the solution
      frontierGET = self.frontier.get()
      currentNode = frontierGET[1]
      solutionFound = node.CheckSolution(currentNode)
      
      # If a solution has been found, return it. Else, expand frontier.
      if (solutionFound):
        return currentNode
      
      self.exploredSet.append( currentNode.state.stateID )
      # visual.exploredList.append(currentNode)
      if (currentNode in visual.frontierList):
        visual.frontierList.remove(currentNode)
      self.ExpandFrontier(currentNode)
      # visual.drawFrontier(currentNode, self.gameboard, True)
        
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
              ctrl = None
              for c in newState.controllers:
                if c.id == controller.id:
                  ctrl = c
                  
              
            
              # print(endPoint)
              # print("---")
              # print((controller.pos_x, controller.pos_y, endPoint[1], endPoint[2]))
              newG = self.ManhattanDist(ctrl.pos_x, ctrl.pos_y, self.startPointList[controller.id][1], self.startPointList[controller.id][2])
              newH = self.ManhattanDist(ctrl.pos_x, ctrl.pos_y, self.endPointList[controller.id][1], self.endPointList[controller.id][2])
              newHeuristic = newG + newH
              
              # if (controller.id == 2):
                # print(newState.controllers[controller.id].pos_x, newState.controllers[controller.id].pos_y, endPoint[1], endPoint[2])
                # print(newHeuristic)
                
              newNode = node.Node(newState, currentNode, (action, controller.id), currentNode.pathCost + 1, newHeuristic)
              
              newNode.state.getID()
              if (newNode.state.stateID not in self.exploredSet):
                self.frontier.put( (newHeuristic,newNode) )
                # visual.frontierList.append(newNode)
                self.totalNodes = self.totalNodes + 1
                
                # print(self.totalNodes)
                
              if (self.totalNodes % 50000 == 0):
                print("qSize: " + str(self.frontier.qsize()))
                print("ES: " + str(len(self.exploredSet)))
                print("Total: " + str(self.totalNodes))
            