#Name: Anton Strickland
#CS5400 Puzzle Project 1
import queue
import state

class Node():

    def __init__(self, state, parent, action, cost):
      self.state = state
      self.parent = parent
      self.action = action
      self.pathCost = cost

    def __str__(self):
      return self.state
      
def BFTS(rootNode, actionSet):

  print("Finding solution...")
  solutionFound = False
  searching = True
  currentNode = rootNode

  frontier = queue.Queue()
  frontier.put(rootNode)

  while (searching):
    if (frontier.empty()):
      searching = False
      return None
    
    # Check to see if this state is the solution
    currentNode = frontier.get()
    print("Checking state...") #+ str(currentNode.state.board))
    currentNode.state.printBoard()
    solutionFound = CheckSolution(currentNode)
    
    # If a solution has not been found, then expand the frontier
    if (not solutionFound):
      ExpandFrontier(currentNode, frontier, actionSet)
    else:
      searching = False
      return currentNode
      

# Check if all controllers have reached their endpoints
def CheckSolution(node):
  for controller in node.state.controllers:
        if controller.reachedGoal is False:
          return False
  print("Solution found!")
  return True
      
def ExpandFrontier(node, frontier, actionSet):
  # For each possible action that can be taken by each possible color controller
  # print("Expand frontier!")
  gridSize = len(node.state.board)
  for controller in node.state.controllers:
    for action in actionSet:
      print ("Testing " +  str(controller.id) + " " + str(action[0]))
      if controller.reachedGoal is False:
        # If this color has not already reached its endpoint and it's a valid action, then add the resulting state to the frontier
        if (controller.checkMoveValidity(action[0], gridSize, gridSize, node.state.board)):
          newBoard = controller.result(node.state, action[0])
          newState = node.state.copy()
          controller.result(newState, action[0])
          newNode = Node(newState, node.state, action[0], node.pathCost + action[1])
          frontier.put(newNode)
          print("Expanded frontier." + " C: " + str(controller.id) + " M: " + str(action[0]))
          
  return