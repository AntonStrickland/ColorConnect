#Name: Anton Strickland
#CS5400 Puzzle Project 4

import node
import sys
import queue

class ASGS():

  __slots__ = ['gameboard', 'gridSize', 'totalNodes', 'frontier', 'actionSet', 'endPointList', 'exploredSet', 'frontierSet', 'bonus']

  def __init__(self, gameboard, actionSet, endPointList, bonus=False):
    self.gameboard = gameboard
    self.totalNodes = 1
    self.frontier = queue.PriorityQueue(sys.maxsize)
    self.actionSet = actionSet
    self.gridSize = len(gameboard)
    self.endPointList = endPointList
    self.exploredSet = set()
    self.frontierSet = set()
    self.bonus = bonus
    
  def ManhattanDist(self, x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
    
  def Search(self, rootNode):
  
    # Make sure the explored set is empty at start
    solutionFound = False
    self.exploredSet.clear()

    # Begin with the root node in the frontier
    self.frontier.put( (rootNode.heuristic, rootNode) )
    self.totalNodes = 1

    while (not self.frontier.empty()):
      # Check to see if this state is the solution
      frontierGET = self.frontier.get()
      currentNode = frontierGET[1]
      solutionFound = node.CheckSolution(currentNode)
      
      # If a solution has been found, return it
      if (solutionFound):
        return currentNode
      
      # Add the current node's hashed ID to the explored set and expand frontier
      self.exploredSet.add(currentNode.state.stateID)
      self.ExpandFrontier(currentNode)
        
    return None
        
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
              # The bonus heuristic is equal to the above plus the number of colors which have not been connected yet
              newH = 0
              for c in newState.controllers:
                newH += self.ManhattanDist(c.pos_x, c.pos_y, self.endPointList[c.id][1], self.endPointList[c.id][2])
                if (self.bonus is True and c.reachedGoal is False):
                  newH += 1

              # G is equal to the path cost + 1
              newG = currentNode.pathCost + 1
              
              # The f-value is equal to g + h
              newF = newG + newH
              newNode = node.Node(newState, currentNode, (action, controller.id), currentNode.pathCost + 1, newF)
              
              # Assign the new node a hashed ID
              newNode.state.getID()
              newHash = newNode.state.stateID
              
              # If this ID is not currently in the explored set, then add it to the frontier
              if (newHash not in self.exploredSet and newHash not in self.frontierSet):
                self.frontier.put( (newF,newNode) )
                self.frontierSet.add(newHash)
                self.totalNodes = self.totalNodes + 1
            