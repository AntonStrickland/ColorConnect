#Name: Anton Strickland
#CS5400 Puzzle Project 1

import agent
import map
from sys import argv

# Set config filepath
cfgPath = ''
if len(argv) < 2:
  print "Please specify a file path for the puzzle instance text file."
  exit()
else:
	cfgPath = argv[1]
  
print "Creating grid..."
gridInput = []
with open(cfgPath) as input:
  for line in input:
    gridInput.append(line.split())
	
print gridInput

gridSize = int(gridInput[0][0])
numberOfColors = int(gridInput[0][1])
grid = map.CreateMap(gridSize, gridSize, gridInput)

myAgent = agent.Agent()
percept = None

# action = myAgent.Action(percept)

