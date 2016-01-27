#Name: Anton Strickland
#CS5400 Puzzle Project 1

import agent
import map
import visual
import bfts
import state
from sys import argv
import random

random.seed(0)




def getBestMove(thisMove, bestMove):
  #print("This: " + thisMove[0] + str(thisMove[1]))
  #print("Best: " + bestMove[0] + str(bestMove[1]))
  if (thisMove[1] > bestMove[1]):
    bestMove = thisMove
  elif (thisMove[1] == bestMove[1]):
    if (random.random() < 0.5):
      bestMove = thisMove
  # print("Winner: " + bestMove[0] + str(bestMove[1]))
  return bestMove
  


# Set config filepath
cfgPath = ''
if len(argv) < 2:
  print("Please specify a file path for the puzzle instance text file.")
  exit()
else:
  cfgPath = argv[1]
  
# print("Creating grid...")
gridInput = []
with open(cfgPath) as input:
  for line in input:
    gridInput.append(line.split())
	
# print(gridInput)

gridSize = int(gridInput[0][0])
numberOfColors = int(gridInput[0][1])
grid = map.CreateMap(gridSize, gridSize, gridInput)

myAgent = agent.Agent()
percept = None

# Keep track of the start and end points
startPointList = []
endPointList = []

for i in range(gridSize):
  for j in range(gridSize):
    if grid[i][j].colored is not "e":
      if grid[i][j].startPoint is True:
        startPointList.append((grid[i][j].colored, i, j))
      elif grid[i][j].endPoint is True:
        endPointList.append((grid[i][j].colored, i, j))

# Create the controllers for each color
controllerList = []
for c in range(numberOfColors):
  controllerList.append(agent.ColorController(startPointList[c][0], startPointList[c][1],startPointList[c][2]))

# action = myAgent.Action(percept)

actionSet = [("Left", 1), ("Right", 1), ("Up", 1), ("Down", 1)]
validList = []
colorMoves = []

visual.setupColors(grid, gridSize, numberOfColors)

terminationCondition = False

# This is where we do the thinking for the game strategy

# Initial state
# initialState = State( bfts.Node(grid, None, None, 0), controllerList)

initialState = state.State(grid, controllerList)

rootNode = bfts.Node(initialState, None, None, 0)
bfts.BFTS(rootNode, actionSet)



# Carry out the best strategy we've found
while (not terminationCondition):
  visual.visualize(grid, gridSize, numberOfColors)
  

  '''
  del colorMoves[:]
  best = None
  for controller in controllerList:
    if controller.reachedGoal is False:
      for move in actionSet:
        if (controller.checkMoveValidity(move[0], gridSize, gridSize, grid)):
          # print("Valid: " + move[0])
          validList.append(move)
          if (best is None):
            best = move
          best = getBestMove(move, best)
    colorMoves.append(best)
  # print("Best move among the colors:")
  # print (colorMoves)
  for move in colorMoves:
    if (best is None):
      best = move
    if (move is not None):
      best = getBestMove(move, best)
  
  bestIndex = colorMoves.index(best)
  
  # If there is a move to be made, then make the best one. Else, end the game in failure.
  if (best is not None):
    controllerList[bestIndex].takeAction(best[0], grid)
        
    newX = visual.x + (controllerList[bestIndex].pos_x * visual.boxWidth) + visual.halfBoxWidth
    newY = visual.y + (controllerList[bestIndex].pos_y * visual.boxWidth) + visual.halfBoxWidth
    visual.colorPointList[controllerList[bestIndex].id].append( (newX, newY) )
  else:
    terminationCondition = True'''
  
print ("No moves remaining. Game over!")
    
    