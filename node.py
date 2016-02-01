#Name: Anton Strickland
#CS5400 Puzzle Project 2

class Node():
    __slots__ = ['state', 'parent', 'action', 'pathCost']
    
    def __init__(self, state, parent, action, cost):
      self.state = state
      self.parent = parent
      self.action = action
      self.pathCost = cost

    def __str__(self):
      return "this is a node"
      
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