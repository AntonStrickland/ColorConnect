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


def createMap(world, width, height, input):
	index = 4
	for i in xrange(width):
		world.append([])
		for j in xrange(height):
			world[i].append(Tile(i, j, input[index]))
			# print str(i) + "," + str(j) + ": " + str(input[index])
			index = index + 2
			
	return world

from sys import argv

# Set config filepath
cfgPath = ''
if len(argv) < 2:
	print "Please specify a file path for the puzzle instance text file."
	exit()
else:
	cfgPath = argv[1]
	
print "Creating grid..."
with open(cfgPath) as input:
	gridInput = input.read()
	
print gridInput

gridSize = int(gridInput[0])
numberOfColors = int(gridInput[2])

grid = []
grid = createMap(grid, gridSize, gridSize, gridInput)

# Test the grid
print grid[1][0]
print grid[3][0]






