#Name: Anton Strickland
#CS5400 Puzzle Project 1

class State():
  __slots__ = ['controllers']
  
  def __init__(self, controllers):
    self.controllers = controllers
  
  # Print the board to the screen
  def printBoard(self):
    for i in range(len(self.board)):
      s = ""
      for j in range(len(self.board[0])):
        s += str(self.board[j][i].colored) + " "
      print (s)
  
  # Return the board as a string
  def returnBoard(self):
    s = ""
    for i in range(len(self.board)):    
      for j in range(len(self.board[0])):
        s += str(self.board[j][i].colored) + " "
      s += "\n"
    return s