#Name: Anton Strickland
#CS5400 Puzzle Project 1

import state
import map
  
    
class ColorController():

    __slots__ = ['id', 'pos_x', 'pos_y', 'reachedGoal', 'points']

    def __init__(self, id, startX, startY, pts, goal):
      self.id = int(id)
      self.pos_x = startX
      self.pos_y = startY
      self.reachedGoal = goal
      self.points = pts

        
    def takeAction(self, move, world):
      if (move == "Left"):
        self.pos_x -= 1
      elif (move == "Right"):
        self.pos_x += 1
      elif (move == "Up"):
        self.pos_y -= 1
      elif (move == "Down"):
        self.pos_y += 1
      
      # print (str(self.pos_x) + "," + str(self.pos_y))
      world[self.pos_x][self.pos_y].colored = str(self.id)
      return self.pos_x, self.pos_y
      
    def checkColorConnect(self, newPos):
      if (newPos.colored == "e"):
        return True
      elif (newPos.colored == str(self.id) and newPos.endPoint is True):
        return True
      else:
        return False
        
    def checkMoveValidity(self, move, maxWidth, maxHeight, gameboard):
     # Move left		
     if (move == "Left" and self.pos_x - 1 >= 0 and self.checkColorConnect(gameboard[self.pos_x-1][self.pos_y])):
       return True
       
     # Move right
     if (move == "Right" and self.pos_x + 1 < maxWidth and self.checkColorConnect(gameboard[self.pos_x+1][self.pos_y])):
       return True
       
     # Move up		
     if (move == "Up" and self.pos_y - 1 >= 0 and self.checkColorConnect(gameboard[self.pos_x][self.pos_y-1])):
       return True
       
     # Move down		
     if (move == "Down" and self.pos_y + 1 < maxHeight and self.checkColorConnect(gameboard[self.pos_x][self.pos_y+1])):
       return True
       
     return False
      
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
      # print (self.gameboard[newX][newY].colored)
      for controls in currentState.controllers:
        for p in controls.points:
          if (newX, newY) == p:
            return None
      if (gameboard[newX][newY].endPoint is True and str(gameboard[newX][newY].colored) != str(self.id)):
        return None

      # Copy and update the same controller within the new state
      newControllerList = []
      for control in currentState.controllers:
        newPoints = control.points[:]
        newController = ColorController(control.id, control.pos_x, control.pos_y, newPoints, control.reachedGoal)
        if (newController.id == self.id):
          newController.pos_x = newX
          newController.pos_y = newY
          newController.points.append( (newX, newY) )
          if (gameboard[newX][newY].endPoint is True):
            newController.reachedGoal = True
        newControllerList.append(newController)


      newState = state.State(newControllerList)    
      # newState.board[newX][newY].colored = str(self.id)

      return newState