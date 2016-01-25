#Name: Anton Strickland
#CS5400 Puzzle Project 1

class Tile():
  def __init__(self, x, y, c):
    self.x = x
    self.y = y
    self.colored = c
    self.startPoint = True
    self.endPoint = True
  
  def __str__(self):
    return str(self.x) + "," + str(self.y) + ": " + str(self.colored)


def CreateMap(width, height, input):
  index = 3
  world = []
  for i in range(width):
    world.append([])
    for j in range(height):
      world[i].append(Tile(i, j, input[i+1][j]))
      print (str(i) + "," + str(j) + ": " + str(input[i+1][j]))
      index = index + 1
    
  return world