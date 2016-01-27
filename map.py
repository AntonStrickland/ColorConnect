#Name: Anton Strickland
#CS5400 Puzzle Project 1

class Tile():
  def __init__(self, y, x, c):
    self.x = x
    self.y = y
    self.colored = c
    self.startPoint = False
    self.endPoint = False
  
  def __str__(self):
    return str(self.x) + "," + str(self.y) + ": " + str(self.colored)


def CreateMap(width, height, input):
  index = 3
  world = []
  seenColors = []
  for i in range(height):
    world.append([])
    for j in range(width):
      newTile = Tile(i, j, input[j+1][i])
      
      if newTile.colored != "e":
        for col in seenColors:
          if col == newTile.colored:
            newTile.endPoint = True
        if newTile.endPoint is not True:
          newTile.startPoint = True
          seenColors.append(newTile.colored)
      
      world[i].append(newTile)
      # print (str(i) + "," + str(j) + ": " + str(input[i+1][j]))
      index = index + 1
    
  return world