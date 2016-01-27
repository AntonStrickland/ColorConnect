#Name: Anton Strickland
#CS5400 Puzzle Project 1

import copy

class State():
  def __init__(self, board, controllers):
    self.board = board
    self.controllers = controllers
    
  def __str__(self):
    return self.board
      
  def copy(self):
      return copy.deepcopy(self)
      
  def printBoard(self):
    for i in range(len(self.board)):
      s = ""
      for j in range(len(self.board[0])):
        s += str(self.board[i][j].colored) + " "
      print (s)