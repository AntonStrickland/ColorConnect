#Name: Anton Strickland
#CS5400 Puzzle Project 1

import agent
import map
import sys 
from sys import argv

import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))

color = (255,0,0)

colorRed = (255,0,0)
colorGreen = (0,255,0)
colorBlue = (0,0,255)
colorDarkBlue = (0,0,128)
colorWhite = (255,255,255)
colorBlack = (0,0,0)
colorPink = (255,200,200)

colorList = [colorRed, colorBlue]



pygame.display.update()

# Set config filepath
cfgPath = ''
if len(argv) < 2:
  print("Please specify a file path for the puzzle instance text file.")
  exit()
else:
	cfgPath = argv[1]
  
print("Creating grid...")
gridInput = []
with open(cfgPath) as input:
  for line in input:
    gridInput.append(line.split())
	
print(gridInput)

gridSize = int(gridInput[0][0])
numberOfColors = int(gridInput[0][1])
grid = map.CreateMap(gridSize, gridSize, gridInput)

myAgent = agent.Agent()
percept = None

# action = myAgent.Action(percept)

thickness = 0
x = 100
y = 100
boxWidth = 50

while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      

  screen.fill(colorBlack)
  
  for i in range(gridSize):
    for j in range(gridSize):
      currentColor = grid[i][j].colored
      if currentColor == "e":
        currentColor = colorBlack
      else:
        currentColor = colorList[int(currentColor)]
        
      if grid[i][j].startPoint is True or grid[i][j].endPoint is True:
        pygame.draw.circle(screen, currentColor, (x+(boxWidth*i),y+(boxWidth*j)), 25, thickness)
      else:
        pygame.draw.rect(screen, currentColor, (x+(boxWidth*i),y+(boxWidth*j),boxWidth,boxWidth), thickness)
   

  # update the screen
  pygame.display.update()