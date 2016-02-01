#Name: Anton Strickland
#CS5400 Puzzle Project 1

class Tile():
  __slots__ = ['x', 'y', 'colored', 'startPoint', 'endPoint']
  
  def __init__(self, y, x, c):
    self.x = x
    self.y = y
    self.colored = c
    self.startPoint = False
    self.endPoint = False
  
  def __str__(self):
    return str(self.colored)


# Create the initial board setup
def CreateInitialBoard(width, height, input, offset=1):
  world = []
  seenColors = []
  for i in range(height):
    world.append([])
    for j in range(width):
      newTile = Tile(i, j, input[j+offset][i])
      world[i].append(newTile)
      # print (str(i) + "," + str(j) + ": " + str(input[i+offset][j]))
      
  for j in range(height):
    for i in range(width):
      if world[i][j].colored != "e":
        for col in seenColors:
          if col == world[i][j].colored:
            world[i][j].endPoint = True
        if world[i][j].endPoint is not True:
          world[i][j].startPoint = True
          seenColors.append(world[i][j].colored)
    
  return world