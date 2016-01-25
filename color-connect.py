#Name: Anton Strickland
#CS5400 Puzzle Project 1

import agent
import map
import visual
from sys import argv
import random

random.seed(0)

def getBestMove(thisMove, bestMove):
  if (thisMove.cost < bestMove.cost):
    bestMove = thisMove
  elif (thisMove.cost == bestMove.cost):
    if (random.random() < 0.5):
      bestMove = thisMove
  return bestMove
      
def takeTurn(grid):
  currentPos = startPos #for each color
  
  #Check moves for each color, pick the best
  for c in range(numberOfColors):
    if (isValid(move)):
      move.cost = calculateCost(move)
      best = getBestMove(move, best)
    colorMoves.append(best)
   
  #Pick the best move among all the colors
  best = None
  for move in colorMoves:
    best = getBestMove(move, best)
    
  takeAction(best)

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

visual.setupColors(grid, gridSize, numberOfColors)

while True:
  # takeTurn(grid)
  visual.visualize(grid, gridSize, numberOfColors)
  
  for controller in controllerList:
    validMove = False
    while(not validMove):
        validMove = controller.checkMoveValidity(gridSize, gridSize, grid)
    newX = visual.x + (controller.pos_x * visual.boxWidth) + visual.halfBoxWidth
    newY = visual.y + (controller.pos_y * visual.boxWidth) + visual.halfBoxWidth
    visual.colorPointList[controller.id].append( (newX, newY) )
  
  

    
    