#Name: Anton Strickland
#CS5400 Puzzle Project 1

class Node():

    def __init__(self, state, parent, action, cost):
      self.state = state
      self.parent = parent
      self.action = action
      self.pathCost = cost
      
      
def bfts(grid, goalState):
  # Initial state
  initialState = Node(grid, None, None, 0)

  solutionFound = False
  searching = True
  currentState = initialState

  frontier = queue.Queue()

  while (searching):

    if (frontier.empty()):
      searching = False
      return None
    
    # Check to see if this state is the solution
    currentState = frontier.get()
    solutionFound = checkSolution(currentState, goalState)
    
    # If a solution has not been found, then expand the frontier
    if (not solutionFound):
      currentState = expandFrontier(currentState)
    else:
      searching = False
      return currentState
      
      
def checkSolution(self, grid, goal):
  pass
      
def expandFrontier(self, state):
  del validList[:]
  # For each possible action that can be taken by each possible color controller
  for action in actionSet:
    for controller in controllerList:
      if controller.reachedGoal is False:
        # If we have not reached the goal and it's a valid action, then add the resulting state to the frontier
        if (controller.checkMoveValidity(move[0], gridSize, gridSize, state)):
          frontier.put( controller.result(state, move[0]) )