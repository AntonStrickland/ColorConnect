#Name: Anton Strickland
#CS5400 Puzzle Project 1

import control
import tile
import bfts
import state
from sys import argv
import time

# Set config filepath
cfgPath = ''
if len(argv) < 2:
  print("Please specify a file path for the puzzle instance text file.")
  exit()
else:
  cfgPath = argv[1]

# Create the name of the output file
nameIndex = len(cfgPath)-5
name = ""
while(cfgPath[nameIndex] != '/'):
  name += cfgPath[nameIndex]
  nameIndex -= 1
name = name[::-1] 

# Create the gameboard
gridInput = []
with open(cfgPath) as input:
  for line in input:
    gridInput.append(line.split())

gridSize = int(gridInput[0][0])
numberOfColors = int(gridInput[0][1])
gameboard = tile.CreateInitialBoard(gridSize, gridSize, gridInput)

# Keep track of the start and end points
startPointList = []
endPointList = []

for i in range(gridSize):
  for j in range(gridSize):
    if gameboard[i][j].colored is not "e":
      if gameboard[i][j].startPoint is True:
        startPointList.append((gameboard[i][j].colored, i, j))
      elif gameboard[i][j].endPoint is True:
        endPointList.append((gameboard[i][j].colored, i, j))

# Create the controllers for each color
controllerList = []
for c in range(numberOfColors):
  controllerList.append(control.ColorController(startPointList[c][0], startPointList[c][1],startPointList[c][2], [(startPointList[c][1],startPointList[c][2] )], False))

actionSet = ["Left", "Right", "Up", "Down"]
terminationCondition = False

# Initial state
initialState = state.State(controllerList)

rootNode = bfts.Node(initialState, None, None, 0)
startTime = time.time()

# This is where we do the thinking for the game strategy
BFTS = bfts.BFTS(gameboard, actionSet)
solutionNode = BFTS.Search(rootNode)
elapsedTime = time.time() - startTime

if (solutionNode is not None):
  solutionPath = BFTS.getSolutionPath(solutionNode)

  pathIndex = len(solutionPath)-1

  # Carry out the strategy we've found
  while (not terminationCondition):
    
    if (pathIndex < 0):
      terminationCondition = True
      
    if (solutionPath[pathIndex].action is not None):
      controllerNumber = solutionPath[pathIndex].action[1]
      newX, newY = controllerList[controllerNumber].takeAction(solutionPath[pathIndex].action[0], gameboard)
      
    pathIndex = pathIndex - 1
      
  # Write to the output file
  with open("output/solution-" + name + ".txt",'w+') as output:
    microseconds = int(elapsedTime*1000000)
    output.write(str(microseconds) + "\n")
    pathIndex = len(solutionPath)-2
    output.write( str(len(solutionPath)-1) + "\n")
    controllerNumber = solutionPath[pathIndex].action[1]
    outputString = str(controllerNumber) + " " + str(solutionPath[pathIndex].state.controllers[controllerNumber].pos_x) + " " + str(solutionPath[pathIndex].state.controllers[controllerNumber].pos_y)
    output.write(outputString)
    pathIndex = pathIndex - 1
    while pathIndex > -1:
      controllerNumber = solutionPath[pathIndex].action[1]
      outputString =  ", " + str(controllerNumber) + " " + str(solutionPath[pathIndex].state.controllers[controllerNumber].pos_x) + " " + str(solutionPath[pathIndex].state.controllers[controllerNumber].pos_y)
      output.write(outputString)
      pathIndex = pathIndex - 1
    s = ""
    for i in range(len(gameboard)):    
      for j in range(len(gameboard[0])):
        s += str(gameboard[j][i].colored) + " "
      s += "\n"
    output.write("\n" + s)
      
  print ("Please check output/solution-" + name + ".txt for solution.")
  