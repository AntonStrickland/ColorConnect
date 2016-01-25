#Name: Anton Strickland
#CS5400 Puzzle Project 1

import agent
import map
import visual
from sys import argv
import random


def getBestMove(move, best):
  if (move.cost < best.cost):
    best = move
  elif (cost == best):
    if (random.random() < 0.5):
      best = move
  return best
      
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

# action = myAgent.Action(percept)

visual.setupColors(grid, gridSize, numberOfColors)

while True:
  # takeTurn(grid)
  visual.visualize(grid, gridSize, numberOfColors)
  
  

    
    