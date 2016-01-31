#Name: Anton Strickland
#CS5400 Puzzle Project 1

import copy

class State():
  __slots__ = ['controllers']
  
  def __init__(self, controllers):
    # self.board = board
    self.controllers = controllers
    # self.pointsList = []
    
  #def __str__(self):
  #  return self.board
      
  def copy(self):
      return copy.deepcopy(self)
      
  def printBoard(self):
    for i in range(len(self.board)):
      s = ""
      for j in range(len(self.board[0])):
        s += str(self.board[j][i].colored) + " "
      print (s)
      
  def returnBoard(self):
    s = ""
    for i in range(len(self.board)):    
      for j in range(len(self.board[0])):
        s += str(self.board[j][i].colored) + " "
      s += "\n"
    return s