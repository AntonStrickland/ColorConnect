#Name: Anton Strickland
#CS5400 Puzzle Project 1

class Agent():

  def __init__(self):
    pass

  def Action(self, percept):
    state = self.UpdateState(state, percept)
    if seq is None:
      goal = FormulateGoal(state)
      problem = FormulateProblem(state, goal)
      seq = Search(problem)
      if seq == "Failure":
        return None
      
    action = First(seq)
    seq = Rest(seq)
    
    return action
    
  def UpdateState(state, percept):
    pass
    
  def FormulateGoal(state):
    pass
  
  def FormulateProblem(state, goal):
    pass
    
  def Search(problem):
    pass
    
  
    
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
        
    def result(self, newState, move):
    
      newX = self.pos_x
      newY = self.pos_y
      print(newX, newY)

      if (move == "Left"):
        newX = self.pos_x - 1
      elif (move == "Right"):
        newX = self.pos_x + 1
      elif (move == "Up"):
        newY = self.pos_y - 1
      elif (move == "Down"):
        newY = self.pos_y + 1
      
      print("Old: ")
      newState.printBoard()
      
      # print (str(self.pos_x) + "," + str(self.pos_y))
      newState.board[newX][newY].colored = str(self.id)
      
      # Update the same controller within the new state
      for controller in newState.controllers:
        if (controller.id == self.id):
          print (controller)
          print (self)
          controller.pos_x = newX
          controller.pos_y = newY
      
      print(newX, newY)
      print("New: ")
      newState.printBoard()
      
      return newState
        
    def takeAction(self, move, world):
      if (move == "Left"):
        self.pos_x -= 1
        
      if (move == "Right"):
        self.pos_x += 1
        
      if (move == "Up"):
        self.pos_y -= 1
        
      if (move == "Down"):
        self.pos_y += 1
      
      # print (str(self.pos_x) + "," + str(self.pos_y))
      world[self.pos_x][self.pos_y].colored = str(self.id)
      return
      
    def checkMoveValidity(self, move, maxWidth, maxHeight, world):

      # Move left		
      if (move == "Left" and self.pos_x - 1 >= 0 and self.checkColorConnect(world[self.pos_x-1][self.pos_y])):
        return True
      
      # Move right
      if (move == "Right" and self.pos_x + 1 < maxWidth and self.checkColorConnect(world[self.pos_x+1][self.pos_y])):
        return True
			
      # Move up		
      if (move == "Up" and self.pos_y - 1 >= 0 and self.checkColorConnect(world[self.pos_x][self.pos_y-1])):
        return True
			
      # Move down		
      if (move == "Down" and self.pos_y + 1 < maxHeight and self.checkColorConnect(world[self.pos_x][self.pos_y+1])):
        return True
      
      return False