#Name: Anton Strickland
#CS5400 Puzzle Project 1
import queue
import state
import visual
import time

totalNodes = 1

class Node():

    def __init__(self, state, parent, action, cost):
      self.state = state
      self.parent = parent
      self.action = action
      self.pathCost = cost

    def __str__(self):
      return "this is a node"
      
def BFTS(rootNode, actionSet):

  print("Finding solution...")
  
  startTime = time.time()
  solutionFound = False
  searching = True
  currentNode = rootNode

  frontier = queue.Queue()
  frontier.put(rootNode)
  totalNodes = 1

  while (searching):
    if (frontier.empty()):
      searching = False
      return None
    
    # Check to see if this state is the solution
    currentNode = frontier.get()
    # print("Checking state...") #+ str(currentNode.state.board))
    # currentNode.state.printBoard()
    solutionFound = CheckSolution(currentNode)
    
    # If a solution has not been found, then expand the frontier
    if (not solutionFound):
      # print("Solution not found. Expanding frontier.")
      totalNodes = ExpandFrontier(currentNode, frontier, actionSet, totalNodes)
      # visual.drawFrontier(currentNode)
    else:
      elapsedTime = time.time() - startTime
      searching = False
      print("Total nodes:" + str(totalNodes))
      print("Elapsed time:" + str(elapsedTime))
      print (currentNode)
      return currentNode

# Check if all controllers have reached their endpoints
def CheckSolution(node):
  for controller in node.state.controllers:
        if controller.reachedGoal is False:
          return False
  print("Solution found!")
  return True
  
def getSolutionPath(node):
  print(node)
  solutionPath = addToPath(node, [])
  return solutionPath
  
  
def addToPath(node, path):
  node.state.printBoard()
  print("---")
  path.append(node)
  if (node.parent is not None):
    addToPath(node.parent, path)
  return path
  
      
def ExpandFrontier(node, frontier, actionSet, totalNodes):
  # For each possible action that can be taken by each possible color controller
  # print("Expand frontier!")
  gridSize = len(node.state.board)
  for controller in node.state.controllers:
    for action in actionSet:
      # print ("Testing " +  str(controller.id) + " " + str(action[0]))
      if controller.reachedGoal is False:
        # If this color has not already reached its endpoint and it's a valid action, then add the resulting state to the frontier
        if (controller.checkMoveValidity(action[0], gridSize, gridSize, node.state.board)):
          newState = controller.result(node.state, action[0])
          if (newState is not None):
            newNode = Node(newState, node, (action[0], controller.id), node.pathCost + action[1])
            frontier.put(newNode)
            totalNodes = totalNodes + 1
            # visual.frontierList.append(newNode)
            # print("Expanded frontier." + str(controller.id) + str(action[0]))
            # newState.printBoard()
          
  return totalNodes