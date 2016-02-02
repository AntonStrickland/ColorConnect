#Name: Anton Strickland
#CS5400 Puzzle Project 1

import state

    
class ColorController():

    __slots__ = ['id', 'pos_x', 'pos_y', 'reachedGoal', 'points']

    def __init__(self, id, startX, startY, pts, goal):
      self.id = int(id)
      self.pos_x = startX
      self.pos_y = startY
      self.reachedGoal = goal
      self.points = pts
    
    # Take an action on the actual gameboard
    def takeAction(self, move, world):
      if (move == "Left"):
        self.pos_x -= 1
      elif (move == "Right"):
        self.pos_x += 1
      elif (move == "Up"):
        self.pos_y -= 1
      elif (move == "Down"):
        self.pos_y += 1
      
      world[self.pos_x][self.pos_y].colored = str(self.id)
      return self.pos_x, self.pos_y
      
    # Check to see if the controller's new position is at an endpoint or empty space
    def checkColorConnect(self, newPos):
      if (newPos.colored == "e"):
        return True
      elif (newPos.colored == str(self.id) and newPos.endPoint is True):
        return True
      else:
        return False
    
    # Check to see if a valid move can be made
    def checkMoveValidity(self, move, maxWidth, maxHeight, gameboard):	
     if (move == "Left" and self.pos_x - 1 >= 0 and self.checkColorConnect(gameboard[self.pos_x-1][self.pos_y])):
       return True
       
     if (move == "Right" and self.pos_x + 1 < maxWidth and self.checkColorConnect(gameboard[self.pos_x+1][self.pos_y])):
       return True
       		
     if (move == "Up" and self.pos_y - 1 >= 0 and self.checkColorConnect(gameboard[self.pos_x][self.pos_y-1])):
       return True
       
     if (move == "Down" and self.pos_y + 1 < maxHeight and self.checkColorConnect(gameboard[self.pos_x][self.pos_y+1])):
       return True
       
     return False
    
    # Return a new state, given a current state and an action
    def result(self, gameboard, currentState, move):
      newX = self.pos_x
      newY = self.pos_y
     
      if (move == "Left"):
        newX = self.pos_x - 1
      elif (move == "Right"):
        newX = self.pos_x + 1
      elif (move == "Up"):
        newY = self.pos_y - 1
      elif (move == "Down"):
        newY = self.pos_y + 1
        
      # Only make valid moves
      for controls in currentState.controllers:
        for p in controls.points:
          if (newX, newY) == p:
            return None
      if (gameboard[newX][newY].endPoint is True and str(gameboard[newX][newY].colored) != str(self.id)):
        return None

      # Copy and update the same controller within the new state
      newControllerList = []
      for controls in currentState.controllers:
        newPoints = controls.points[:]
        newController = ColorController(controls.id, controls.pos_x, controls.pos_y, newPoints, controls.reachedGoal)
        if (newController.id == self.id):
          newController.pos_x = newX
          newController.pos_y = newY
          newController.points.append( (newX, newY) )
          if (gameboard[newX][newY].endPoint is True):
            newController.reachedGoal = True
        newControllerList.append(newController)

      newState = state.State(newControllerList)
      return newState