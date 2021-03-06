#Name: Anton Strickland
#CS5400 Puzzle Project 4

import control
import tile
import node
import bfts
import iddfts
import gbfgs
import gbfts
import asgs
import state
from sys import argv
import time

# Set config filepath
cfgPath = ''
if len(argv) < 2:
  print("Please specify a file path for the puzzle instance text file.")
  exit()

cfgPath = argv[1]  
if len(argv) == 3:
  searchAlgorithm = argv[2]
else:
  searchAlgorithm = "bfts"

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
        
        
startPointList.sort(key=lambda node: node[0])
endPointList.sort(key=lambda node: node[0])

# Create the controllers for each color
controllerList = []
for c in range(numberOfColors):
  controllerList.append(control.ColorController(startPointList[c][0], startPointList[c][1],startPointList[c][2], [(startPointList[c][1],startPointList[c][2] )], False))

actionSet = ["Left", "Right", "Up", "Down"]
terminationCondition = False

# Initial state
initialState = state.State(controllerList)

rootNode = node.Node(initialState, None, None, 0)
startTime = time.time()

print("Performing " + searchAlgorithm + "...")

# This is where we do the thinking for the game strategy
if (searchAlgorithm == "bfts"):
  BFTS = bfts.BFTS(gameboard, actionSet)
  solutionNode = BFTS.Search(rootNode)
elif (searchAlgorithm == "iddfts"):
  IDDFTS = iddfts.IDDFTS(gameboard, actionSet)
  solutionNode = IDDFTS.Search(rootNode)
elif (searchAlgorithm == "gbfgs"):
  GBFGS = gbfgs.GBFGS(gameboard, actionSet, endPointList)
  solutionNode = GBFGS.Search(rootNode)
elif (searchAlgorithm == "gbfts"):
  GBFTS = gbfts.GBFTS(gameboard, actionSet, endPointList)
  solutionNode = GBFTS.Search(rootNode)
elif (searchAlgorithm == "asgs"):
  ASGS = asgs.ASGS(gameboard, actionSet, endPointList)
  solutionNode = ASGS.Search(rootNode)
elif (searchAlgorithm == "asgs2"):
  ASGS = asgs.ASGS(gameboard, actionSet, endPointList, True)
  solutionNode = ASGS.Search(rootNode)
else:
  print("Please enter either bfts, iddfts, gbfgs, gbfts, asgs, or asgs2 as a search algorithm.")
  exit()

elapsedTime = time.time() - startTime
# print(elapsedTime)

if (solutionNode is not None):
  solutionPath = node.getSolutionPath(solutionNode)

  pathIndex = len(solutionPath)-1

  # Carry out the strategy we've found
  while (not terminationCondition):
    
    if (pathIndex < 0):
      terminationCondition = True
      
    if (solutionPath[pathIndex].action is not None):
      controllerNumber = solutionPath[pathIndex].action[1]
      
      for controller in controllerList:
        if controller.id == controllerNumber:
          newX, newY = controller.takeAction(solutionPath[pathIndex].action[0], gameboard)
      
    pathIndex = pathIndex - 1
      
  # Write to the output file
  with open("output/solution-" + searchAlgorithm + "-" + name + ".txt",'w+') as output:
    microseconds = int(elapsedTime*1000000)
    output.write(str(microseconds) + "\n")
    pathIndex = len(solutionPath)-2
    output.write( str(len(solutionPath)-1) + "\n")
    controllerNumber = solutionPath[pathIndex].action[1]
    
    for controller in solutionPath[pathIndex].state.controllers:
        if controller.id == controllerNumber:
          outputString = str(controllerNumber) + " " + str(controller.pos_x) + " " + str(controller.pos_y)
          
    output.write(outputString)
    pathIndex = pathIndex - 1
    while pathIndex > -1:
      controllerNumber = solutionPath[pathIndex].action[1]
      
      for controller in solutionPath[pathIndex].state.controllers:
        if controller.id == controllerNumber:
          outputString =  ", " + str(controllerNumber) + " " + str(controller.pos_x) + " " + str(controller.pos_y)
          
      output.write(outputString)
      pathIndex = pathIndex - 1
    s = ""
    for i in range(len(gameboard)):    
      for j in range(len(gameboard[0])):
        s += str(gameboard[j][i].colored) + " "
      s += "\n"
    output.write("\n" + s)
      
  print ("Please check output/solution-" + searchAlgorithm + "-" + name + ".txt for solution.")
else:
  print ("Search failed to find a solution.")
  