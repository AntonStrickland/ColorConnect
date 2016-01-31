#Name: Anton Strickland
#CS5400 Puzzle Project 1
import queue
import state
import visual
import agent
import gc

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
      
  def Search(self, rootNode):

    print("Finding solution...")
    
    gc.enable()
    solutionFound = False
    searching = True
    currentNode = rootNode

    self.frontier.put(rootNode)
    self.totalNodes = 1

    while (not self.frontier.empty()):
      # Check to see if this state is the solution
      currentNode = self.frontier.get()
      # print("Checking state...") #+ str(currentNode.state.board))
      # currentNode.state.printBoard()
      solutionFound = self.CheckSolution(currentNode)
      
      # If a solution has not been found, then expand the frontier
      if (not solutionFound):
        # print("Total nodes:" + str(self.totalNodes))
        self.ExpandFrontier(currentNode)
        # visual.drawFrontier(currentNode, self.gameboard, self.totalNodes)
      else:
        print("Total nodes:" + str(self.totalNodes))
        # print (currentNode)
        return currentNode
      gc.collect(0)
    print("No solution found.")
      
  # Check if all controllers have reached their endpoints
  def CheckSolution(self, node):
    for controller in node.state.controllers:
          if controller.reachedGoal is False:
            return False
    print("Solution found!")
    return True
    
  def getSolutionPath(self, node):
    #print(node)
    solutionPath = self.addToPath(node, [])
    return solutionPath
    
    
  def addToPath(self, node, path):
    #node.state.printBoard()
    #print("---")
    path.append(node)
    if (node.parent is not None):
      self.addToPath(node.parent, path)
    return path
        

        
  def ExpandFrontier(self, node):
    # For each possible action that can be taken by each possible color controller
    gridSize = len(self.gameboard)
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
              # visual.frontierList.append(newNode)
            
    return totalNodes