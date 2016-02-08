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
colorQ = (111,111,111)
colorW = (55,0,55)
colorE = (22,22,200)

colorList = [colorRed, colorBlue, colorGreen, colorOrange, colorPink, colorWhite, colorQ, colorW, colorE]
bgColor1 = (54,54,54)
bgColor2 = (45,45,45)

colorPointList = []
frontierList = []
exploredList = []

thickness = 0
#screen = pygame.display.set_mode((1024,480))
pygame.init()
  
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)
headerFont = pygame.font.SysFont("monospace", 30)
  
def initialize(grid, gridSize, numberOfColors):

  x = 100
  y = 100
  boxWidth = 10
  halfBoxWidth = 5
  


  pygame.display.update()

  # Create a list of points for each color
  for c in range(numberOfColors):
    colorPointList.append([])
    
  for i in range(gridSize):
    for j in range(gridSize):
      if grid[i][j].colored is not "e" and grid[i][j].startPoint is True:
        colorPointList[int(grid[i][j].colored)].append((grid[i][j].y, grid[i][j].x))
        
        
def drawFrontier(currentNode, gameboard, graphSearch=False):

  screen.fill(colorBlack)
  
  numberOfTiles = len(gameboard)
  
  bigX = 25
  bigY = 100
  bigWidth = 50
  
  smallX = 25 + bigX + (bigWidth*numberOfTiles)
  smallY = bigY
  
  statesPerColumn = 4
  statesPerFrontier = 29
  index = 0
  
  delayTime = 0

  drawBoard(gameboard, bigWidth, int(bigWidth/2), bigX, bigY, currentNode.state.controllers)
  
  # render text
  label = headerFont.render("Current H:" + str(currentNode.heuristic), 1, (255,255,0))
  screen.blit(label, (bigX, bigY-30))

  pygame.display.update()
  pygame.time.delay(delayTime)
  
  frontierList.sort(key=lambda node: node.heuristic)
  nodeIndex = 0
  for node in frontierList:
    if nodeIndex > statesPerFrontier:
      break
    # update the screen
    if (index > statesPerColumn):
      index = 0
      smallX = smallX + 75
      smallY = 100
    # print (node.state.pointsList)
    drawBoard(gameboard, 10, 5, smallX, smallY, node.state.controllers, False)
    label = myfont.render("H:" + str(node.heuristic), 1, (255,255,0))
    screen.blit(label, (smallX+40, smallY))
    smallY = smallY + 75
    index = index + 1
    nodeIndex = nodeIndex + 1
    pygame.display.update()
    pygame.time.delay(delayTime)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
  
  '''
  if (graphSearch):
    index = 0
    smallX = 25
    smallY = 125 + bigX + (bigWidth*numberOfTiles)
    for node in exploredList:
      # update the screen
      if (index > statesPerColumn):
        index = 0
        smallX = smallX + 75
        smallY = 125 + bigX + (bigWidth*numberOfTiles)
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
  '''
  
  if (not graphSearch):  
    del frontierList[:]
  pygame.time.delay(delayTime*10)
  
    

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
  