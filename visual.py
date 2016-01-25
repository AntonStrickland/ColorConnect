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

thickness = 0
x = 100
y = 100
boxWidth = 50
halfBoxWidth = 25

pygame.display.update()

def setupColors(grid, gridSize, numberOfColors):

  # Create a list of points for each color
  for c in range(numberOfColors):
    colorPointList.append([])
    
  for i in range(gridSize):
    for j in range(gridSize):
      if grid[i][j].colored is not "e" and grid[i][j].startPoint is True:
        newX = x + (grid[i][j].x * boxWidth) + halfBoxWidth
        newY = y + (grid[i][j].y * boxWidth) + halfBoxWidth
        colorPointList[int(grid[i][j].colored)].append((newX, newY))
  
  # Test the lines
  newX = x + (1 * boxWidth) + halfBoxWidth
  newY = y + (0 * boxWidth) + halfBoxWidth
  colorPointList[0].append((newX, newY))
  
  # Test the lines
  newX = x + (1 * boxWidth) + halfBoxWidth
  newY = y + (1 * boxWidth) + halfBoxWidth
  colorPointList[0].append((newX, newY))
  
def visualize(grid, gridSize, numberOfColors):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      

  screen.fill(colorBlack)
  colorBGIndex = 0
  for i in range(gridSize):
    colorBGIndex = colorBGIndex + 1
    for j in range(gridSize):
      currentColor = grid[i][j].colored
      
      if (colorBGIndex%2 == 0):
        pygame.draw.rect(screen, bgColor1, (x+(boxWidth*i),y+(boxWidth*j),boxWidth,boxWidth), thickness)
      else:
        pygame.draw.rect(screen, bgColor2, (x+(boxWidth*i),y+(boxWidth*j),boxWidth,boxWidth), thickness)
        
      colorBGIndex = colorBGIndex + 1
        
      if currentColor == "e":
        currentColor = colorBlack
      else:
        currentColor = colorList[int(currentColor)]
       
      
      if grid[i][j].startPoint is True or grid[i][j].endPoint is True:
        pygame.draw.circle(screen, currentColor, (x+(boxWidth*i)+halfBoxWidth,y+(boxWidth*j)+halfBoxWidth), 15, thickness)
      #else:
      # pygame.draw.rect(screen, currentColor, (x+(boxWidth*i),y+(boxWidth*j),boxWidth,boxWidth), thickness)
      
  for i in range(numberOfColors):
    # print (colorPointList[i])
    if (len(colorPointList[i]) > 1):
      pygame.draw.lines(screen, colorList[i], False, colorPointList[i], 5)
   

  # update the screen
  pygame.display.update()
  