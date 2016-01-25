import pygame

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
bgColor = (54,54,54)

thickness = 0
x = 100
y = 100
boxWidth = 50
halfBoxWidth = 25

pygame.display.update()

  
def visualize(grid, gridSize):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      

  screen.fill(colorBlack)
  
  for i in range(gridSize):
    for j in range(gridSize):
      currentColor = grid[i][j].colored
      pygame.draw.rect(screen, bgColor, (x+(boxWidth*i),y+(boxWidth*j),boxWidth,boxWidth), thickness)
      
      if currentColor == "e":
        currentColor = colorBlack
      else:
        currentColor = colorList[int(currentColor)]
       
      
      if grid[i][j].startPoint is True or grid[i][j].endPoint is True:
        pygame.draw.circle(screen, currentColor, (x+(boxWidth*i)+halfBoxWidth,y+(boxWidth*j)+halfBoxWidth), 15, thickness)
      #else:
      # pygame.draw.rect(screen, currentColor, (x+(boxWidth*i),y+(boxWidth*j),boxWidth,boxWidth), thickness)
   

  # update the screen
  pygame.display.update()
  