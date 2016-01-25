#Name: Anton Strickland
#CS5400 Puzzle Project 1

import random

class Agent():

  def __init__(self):
    pass

  def Action(self, percept):
    state = UpdateState(state, percept)
    if seq is None:
      goal = FormulateGoal(state)
      problem = FormulateProblem(state, goal)
      seq = Search(problem)
      if seq == "Failure":
        return None
      
    action = First(seq)
    seq = Rest(seq)
    
    return action
    
class ColorController():

    def __init__(self, id, startX, startY):
      self.id = int(id)
      self.pos_x = startX
      self.pos_y = startY
      self.reachedGoal = False
      
    def checkColorConnect(self, newPos):
      if (newPos.colored == "e"):
        return True
      elif (newPos.colored == str(self.id) and newPos.endPoint is True):
        self.reachedGoal = True
        return True
      else:
        return False
      
    def checkMoveValidity(self, maxWidth, maxHeight, world):
      r = random.randint(0,4)
      
      #Stay in the same tile
      if (r == 0):
        return True
			
      # Move left		
      if (r == 1 and self.pos_x - 1 >= 0 and self.checkColorConnect(world[self.pos_x-1][self.pos_y])):
        self.pos_x -= 1
        world[self.pos_x][self.pos_y].colored = str(self.id)
        return True
      
      # Move right
      if (r == 2 and self.pos_x + 1 < maxWidth and self.checkColorConnect(world[self.pos_x+1][self.pos_y])):
        self.pos_x += 1
        world[self.pos_x][self.pos_y].colored = str(self.id)
        return True
			
      # Move up		
      if (r == 3 and self.pos_y - 1 >= 0 and self.checkColorConnect(world[self.pos_x][self.pos_y-1])):
        self.pos_y -= 1
        world[self.pos_x][self.pos_y].colored = str(self.id)
        return True
			
      # Move down		
      if (r == 4 and self.pos_y + 1 < maxHeight and self.checkColorConnect(world[self.pos_x][self.pos_y+1])):
        self.pos_y += 1
        world[self.pos_x][self.pos_y].colored = str(self.id)
        return True
      
      return False