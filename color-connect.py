#Name: Anton Strickland
#CS5400 Puzzle Project 1

import agent
import map
import visual
import bfts
import state
from sys import argv
import random
import time

random.seed()
  
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
gameboard = map.CreateMap(gridSize, gridSize, gridInput)

# Keep track of the start and end points
startPointList = []
endPointList = []

for i in range(gridSize):
  s = ""
  for j in range(gridSize):
    s += str(gameboard[j][i].colored) + " "
    if gameboard[i][j].colored is not "e":
      if gameboard[i][j].startPoint is True:
        startPointList.append((gameboard[i][j].colored, i, j))
      elif gameboard[i][j].endPoint is True:
        endPointList.append((gameboard[i][j].colored, i, j))
  print(s)

# Create the controllers for each color
controllerList = []
for c in range(numberOfColors):
  controllerList.append(agent.ColorController(startPointList[c][0], startPointList[c][1],startPointList[c][2], [(startPointList[c][1],startPointList[c][2] )], False))
  # print (controllerList[c].points)
  

# action = myAgent.Action(percept)

actionSet = ["Left", "Right", "Up", "Down"]
terminationCondition = False

# This is where we do the thinking for the game strategy

# Initial state
initialState = state.State(controllerList)
#for color in range(numberOfColors):
#  initialState.pointsList.append( [] )
#  initialState.pointsList[color].append((startPointList[color][1] , startPointList[color][2]))
 
 
rootNode = bfts.Node(initialState, None, None, 0)
startTime = time.time()

BFTS = bfts.BFTS(gameboard, actionSet)
solutionNode = BFTS.Search(rootNode)
elapsedTime = time.time() - startTime
print("Elapsed time:" + str(elapsedTime))
solutionPath = BFTS.getSolutionPath(solutionNode)
# print(solutionPath)

pathIndex = len(solutionPath)-1

visual.initialize(gameboard, gridSize, numberOfColors)

# Carry out the strategy we've found
while (not terminationCondition):
  # visual.visualize(gameboard, gridSize, numberOfColors)
  
  if (pathIndex < 0):
    terminationCondition = True
    
  if (solutionPath[pathIndex].action is not None):
    controllerNumber = solutionPath[pathIndex].action[1]
    newX, newY = controllerList[controllerNumber].takeAction(solutionPath[pathIndex].action[0], gameboard)
    # print(solutionPath[pathIndex].action)
    # visual.colorPointList[controllerList[controllerNumber].id].append( (newX, newY) )
    
  pathIndex = pathIndex - 1
  
print ("No moves remaining. Game over!")

with open("output/solution.txt",'w+') as output:
  output.write(str(elapsedTime*1000000) + "\n")
  pathIndex = len(solutionPath)-2
  controllerNumber = solutionPath[pathIndex].action[1]
  outputString = str(controllerNumber) + " " + str(solutionPath[pathIndex].state.controllers[controllerNumber].pos_x) + " " + str(solutionPath[pathIndex].state.controllers[controllerNumber].pos_y)
  output.write(outputString)
  pathIndex = pathIndex - 1
  while pathIndex > -1:
    controllerNumber = solutionPath[pathIndex].action[1]
    outputString =  ", " + str(controllerNumber) + " " + str(solutionPath[pathIndex].state.controllers[controllerNumber].pos_x) + " " + str(solutionPath[pathIndex].state.controllers[controllerNumber].pos_y)
    output.write(outputString)
    pathIndex = pathIndex - 1
  # output.write("\n" + solutionPath[0].state.returnBoard())
    
    