#Name: Anton Strickland
#CS5400 Puzzle Project 1
import queue
import state
import control

totalNodes = 1

class Node():
    __slots__ = ['state', 'parent', 'action', 'pathCost']
    
    def __init__(self, state, parent, action, cost):
      self.state = state
      self.parent = parent
      self.action = action
      self.pathCost = cost

    def __str__(self):
      return "this is a node"
      
class BFTS():

  __slots__ = ['gameboard', 'totalNodes', 'frontier', 'actionSet']

  def __init__(self, gameboard, actionSet):
    self.gameboard = gameboard
    self.totalNodes = 1
    self.frontier = queue.Queue()
    self.actionSet = actionSet
  
  # Perform the BFTS algorithm
  def Search(self, rootNode):

    print("Finding solution...")
    solutionFound = False
    currentNode = rootNode

    # Begin with the root node in the frontier
    self.frontier.put(rootNode)
    self.totalNodes = 1

    while (not self.frontier.empty()):
      # Check to see if this state is the solution
      currentNode = self.frontier.get()
      solutionFound = self.CheckSolution(currentNode)
      
      # If a solution has not been found, then expand the frontier
      # Otherwise, return the winning node
      if (not solutionFound):
        self.ExpandFrontier(currentNode)
      else:
        return currentNode
    print("No solution found.")
    return None
      
  # Check if all controllers have reached their endpoints
  def CheckSolution(self, node):
    for controller in node.state.controllers:
          if controller.reachedGoal is False:
            return False
    print("Solution found!")
    return True
    
  # Returns the solution path from the winning node to the root node
  def getSolutionPath(self, node):
    solutionPath = self.addToPath(node, [])
    return solutionPath
    
  # Add to the solution path (in reverse order)
  def addToPath(self, node, path):
    path.append(node)
    if (node.parent is not None):
      self.addToPath(node.parent, path)
    return path
        
  # Expand the frontier of nodes for searching
  def ExpandFrontier(self, node):
    gridSize = len(self.gameboard)
    # For each possible action that can be taken by each possible color controller
    for controller in node.state.controllers:
      for action in self.actionSet:
        if controller.reachedGoal is False:
          # If this color has not already reached its endpoint and it's a valid action, then add the resulting state to the frontier
          if (controller.checkMoveValidity(action, gridSize, gridSize, self.gameboard)):
            newState = controller.result(self.gameboard, node.state, action)
            if (newState is not None):
              newNode = Node(newState, node, (action, controller.id), node.pathCost + 1)
              self.frontier.put(newNode)
              self.totalNodes = self.totalNodes + 1
            
    return totalNodes