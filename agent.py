#Name: Anton Strickland
#CS5400 Puzzle Project 1

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