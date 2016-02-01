#Name: Anton Strickland
#CS5400 Puzzle Project 2

import pygame
import sys 

color = (255,0,0)

colorRed = (255,0,0)
colorGreen = (0,255,0)
colorBlue = (0,0,255)
colorOrange = (255,165,0)
colorWhite = (255,255,255)
colorBlack = (0,0,0)
colorPink = (255,200,200)

colorList = [colorRed, colorBlue, colorGreen, colorOrange, colorPink, colorWhite]
bgColor1 = (54,54,54)
bgColor2 = (45,45,45)

colorPointList = []
frontierList = []

thickness = 0
screen = pygame.display.set_mode((640,480))

def initialize(grid, gridSize, numberOfColors):

  x = 100
  y = 100
  boxWidth = 10
  halfBoxWidth = 5
  
  pygame.init()
  pygame.display.update()

  # Create a list of points for each color
  for c in range(numberOfColors):
    colorPointList.append([])
    
  for i in range(gridSize):
    for j in range(gridSize):
      if grid[i][j].colored is not "e" and grid[i][j].startPoint is True:
        colorPointList[int(grid[i][j].colored)].append((grid[i][j].y, grid[i][j].x))
        
        
def drawFrontier(currentNode, gameboard):

  screen.fill(colorBlack)
  
  numberOfTiles = len(gameboard)
  
  bigX = 25
  bigY = 100
  bigWidth = 50
  
  smallX = 25 + bigX + (bigWidth*numberOfTiles)
  smallY = bigY
  
  statesPerColumn = 3
  index = 0
  
  delayTime = 500

  drawBoard(gameboard, bigWidth, int(bigWidth/2), bigX, bigY, currentNode.state.controllers)
  pygame.display.update()
  pygame.time.delay(delayTime)
    
  for node in frontierList:
    # update the screen
    if (index > statesPerColumn):
      index = 0
      smallX = smallX + 75
      smallY = 100
    # print (node.state.pointsList)
    drawBoard(gameboard, 10, 5, smallX, smallY, node.state.controllers, False)
    smallY = smallY + 50
    index = index + 1
    
    pygame.display.update()
    pygame.time.delay(delayTime)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
  del frontierList[:]
  pygame.time.delay(delayTime)
    

def drawBoard(board, boxWidth, halfBoxWidth, x=100, y=100, controllers=None, printf=True):
  quarterBox = int(halfBoxWidth*0.5)
  circleRadius = int(halfBoxWidth*0.75)
  gridSize = len(board)
  for i in range(gridSize):
    for j in range(gridSize):
      currentColor = board[i][j].colored
      
      if ((i+j)%2 == 0):
        pygame.draw.rect(screen, bgColor1, (x+(boxWidth*i),y+(boxWidth*j),boxWidth,boxWidth), thickness)
      else:
        pygame.draw.rect(screen, bgColor2, (x+(boxWidth*i),y+(boxWidth*j),boxWidth,boxWidth), thickness)
        
      if currentColor == "e":
        currentColor = colorBlack
      else:
        currentColor = colorList[int(currentColor)]
       
      if board[i][j].startPoint is True or board[i][j].endPoint is True:
        pygame.draw.circle(screen, currentColor, (x+(boxWidth*i)+halfBoxWidth,y+(boxWidth*j)+halfBoxWidth), circleRadius, thickness)
      #else:
      # pygame.draw.rect(screen, currentColor, (x+(boxWidth*i),y+(boxWidth*j),boxWidth,boxWidth), thickness)
  
  newPointsList = []
  for control in controllers:
    newPointsList.append([])
  
  for control in controllers:
    #if (printf is True):
      #print(control.points)
    for i in range(len(control.points)):
        newTuple = (x + (control.points[i][0] * boxWidth) + halfBoxWidth, y + (control.points[i][1] * boxWidth) + halfBoxWidth)
        newPointsList[control.id].append(newTuple) 
    if (len(newPointsList[control.id]) > 1):
      pygame.draw.lines(screen, colorList[control.id], False, newPointsList[control.id], quarterBox)

def visualize(grid, gridSize, numberOfColors):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      
  screen.fill(colorBlack)
  # print(colorPointList)
  drawBoard(grid, 50, 24, 100, 100, colorPointList)
  
  # update the screen
  pygame.display.update()
  pygame.time.delay(500)
  