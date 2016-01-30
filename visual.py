#Name: Anton Strickland
#CS5400 Puzzle Project 1

import pygame
import sys 

pygame.init()

screen = pygame.display.set_mode((640,480))

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

boxWidth = 10
halfBoxWidth = 5

pygame.display.update()

def setupColors(grid, gridSize, numberOfColors):

  x = 100
  y = 100

  # Create a list of points for each color
  for c in range(numberOfColors):
    colorPointList.append([])
    
  for i in range(gridSize):
    for j in range(gridSize):
      if grid[i][j].colored is not "e" and grid[i][j].startPoint is True:
        newX = x + (grid[i][j].x * boxWidth) + halfBoxWidth
        newY = y + (grid[i][j].y * boxWidth) + halfBoxWidth
        colorPointList[int(grid[i][j].colored)].append((newX, newY))
        
        
def drawFrontier(currentNode):

  screen.fill(colorBlack)
  x = 100
  y = 100
  index = 0
  
  drawBoard(currentNode.state.board, 320, 25, currentNode.state.pointsList)
  
  for node in frontierList:
    # update the screen
    if (index > 5):
      index = 0
      x = x + 100
      y = 100
    print (node.state.pointsList)
    drawBoard(node.state.board, x, y, node.state.pointsList)
    y = y + 50
    index = index + 1
    
    pygame.display.update()
    pygame.time.delay(1000)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
  del frontierList[:]
  pygame.time.delay(1000)
    

def drawBoard(board, x=100, y=100, pointsList=None):
  colorBGIndex = 0
  gridSize = len(board)
  for i in range(gridSize):
    colorBGIndex = colorBGIndex + 1
    for j in range(gridSize):
      currentColor = board[i][j].colored
      
      if (colorBGIndex%2 == 0):
        pygame.draw.rect(screen, bgColor1, (x+(boxWidth*i),y+(boxWidth*j),boxWidth,boxWidth), thickness)
      else:
        pygame.draw.rect(screen, bgColor2, (x+(boxWidth*i),y+(boxWidth*j),boxWidth,boxWidth), thickness)
        
      colorBGIndex = colorBGIndex + 1
        
      if currentColor == "e":
        currentColor = colorBlack
      else:
        currentColor = colorList[int(currentColor)]
       
      
      if board[i][j].startPoint is True or board[i][j].endPoint is True:
        pygame.draw.circle(screen, currentColor, (x+(boxWidth*i)+halfBoxWidth,y+(boxWidth*j)+halfBoxWidth), halfBoxWidth, thickness)
      #else:
      # pygame.draw.rect(screen, currentColor, (x+(boxWidth*i),y+(boxWidth*j),boxWidth,boxWidth), thickness)
  
  newPointsList = []
  for color in range(len(pointsList)):
    newPointsList.append([])
    # print (pointsList)
    # print(pointsList[color])
    # print(newPointsList)
    for i in range(len(pointsList[color])):
        newTuple = (x + (pointsList[color][i][0] * boxWidth) + halfBoxWidth, y + (pointsList[color][i][1] * boxWidth) + halfBoxWidth)
        newPointsList[color].append(newTuple) 
    # print ("\nDrawing lines")
    if (len(newPointsList[color]) > 1):
      # print(newPointsList[color])
      pygame.draw.lines(screen, colorList[color], False, newPointsList[color], 2)
    # print("\nOriginal list:")
    # print (pointsList)
  
def visualize(grid, gridSize, numberOfColors):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      

  screen.fill(colorBlack)
  drawBoard(grid, gridSize)
  
  # update the screen
  pygame.display.update()
  pygame.time.delay(250)
  