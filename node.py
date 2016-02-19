#Name: Anton Strickland
#CS5400 Puzzle Project 4

class Node():
    __slots__ = ['state', 'parent', 'action', 'pathCost', 'heuristic']
    
    def __init__(self, state, parent, action, cost, heuristic=0):
      self.state = state
      self.parent = parent
      self.action = action
      self.pathCost = cost
      self.heuristic = heuristic
      
    def __eq__(self, other):
      return self.heuristic == other.heuristic
      
    def __ne__(self, other):
      return self.heuristic != other.heuristic

    def __gt__(self, other):
      return self.heuristic > other.heuristic

    def __lt__(self, other):
      return self.heuristic < other.heuristic      
      
# Check if all controllers have reached their endpoints
def CheckSolution(currentNode):
  for controller in currentNode.state.controllers:
        if controller.reachedGoal is False:
          return False
  print("Solution found!")
  return True
    
# Returns the solution path from the winning node to the root node
def getSolutionPath(currentNode):
  solutionPath = addToPath(currentNode, [])
  return solutionPath
    
# Add to the solution path (in reverse order)
def addToPath(currentNode, path):
  path.append(currentNode)
  if (currentNode.parent is not None):
    addToPath(currentNode.parent, path)
  return path