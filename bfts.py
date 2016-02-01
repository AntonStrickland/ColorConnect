#Name: Anton Strickland
#CS5400 Puzzle Project 2
import queue
import state
import control
import node
      
class BFTS():

  __slots__ = ['gameboard', 'totalNodes', 'frontier', 'actionSet']

  def __init__(self, gameboard, actionSet):
    self.gameboard = gameboard
    self.totalNodes = 1
    self.frontier = queue.Queue()
    self.actionSet = actionSet
  
  # Perform the BFTS algorithm
  def Search(self, rootNode):

    print("Performing BFTS...")
    solutionFound = False
    currentNode = rootNode

    # Begin with the root node in the frontier
    self.frontier.put(rootNode)
    self.totalNodes = 1

    while (not self.frontier.empty()):
      # Check to see if this state is the solution
      currentNode = self.frontier.get()
      solutionFound = node.CheckSolution(currentNode)
      
      # If a solution has not been found, then expand the frontier
      # Otherwise, return the winning node
      if (not solutionFound):
        self.ExpandFrontier(currentNode)
      else:
        return currentNode
    print("No solution found.")
    return None
        
  # Expand the frontier of nodes for searching
  def ExpandFrontier(self, currentNode):
    gridSize = len(self.gameboard)
    # For each possible action that can be taken by each possible color controller
    for controller in currentNode.state.controllers:
      for action in self.actionSet:
        if controller.reachedGoal is False:
          # If this color has not already reached its endpoint and it's a valid action, then add the resulting state to the frontier
          if (controller.checkMoveValidity(action, gridSize, gridSize, self.gameboard)):
            newState = controller.result(self.gameboard, currentNode.state, action)
            if (newState is not None):
              newNode = node.Node(newState, currentNode, (action, controller.id), currentNode.pathCost + 1)
              self.frontier.put(newNode)
              self.totalNodes = self.totalNodes + 1
            