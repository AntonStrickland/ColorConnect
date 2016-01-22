#Name: Anton Strickland
#CS5400 Puzzle Project 1

class Tile():
  def __init__(self, x, y, c):
    self.x = x
    self.y = y
    self.colored = c
    self.startPoint = False
    self.endPoint = False
  
  def __str__(self):
    return str(self.x) + "," + str(self.y) + ": " + str(self.colored)


def CreateMap(width, height, input):
  index = 4
  world = []
  for i in xrange(width):
    world.append([])
  for j in xrange(height):
    world[i].append(Tile(i, j, input[index]))
    # print str(i) + "," + str(j) + ": " + str(input[index])
    index = index + 2
    
  return world