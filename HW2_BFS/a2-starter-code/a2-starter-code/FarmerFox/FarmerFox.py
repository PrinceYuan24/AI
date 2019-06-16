'''FarmerFox.py
("Farmer, Fox, Chicken & Grain" problem)
'''
#<METADATA>
SOLUZION_VERSION = "2.0"
PROBLEM_NAME = "Farmer, Fox, Chicken & Grain"
PROBLEM_VERSION = "2.0"
PROBLEM_AUTHORS = ['Ziyuan Wang']
PROBLEM_CREATION_DATE = "14-April-2018"

# The following field is mainly for the human solver, via either the Text_SOLUZION_Client.
# or the SVG graphics client.
PROBLEM_DESC=\
 '''The <b>"Farmer, Fox, Chicken & Grain"</b> problem is a traditional puzzle
in which the player starts off with a farmer, a fox, a chicken and grain
on the left bank of a river.  The boat can only hold a farmer and a item. 
Fox and chicken or chicken and grain is forbidden either on the left bank or right bank.  
In the formulation presented here, the computer will not let you make a move to such a forbidden situation, 
and it will only show you moves that could be executed "safely."
'''
#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
M=0  # array index to access missionary counts
C=1  # same idea for cannibals
LEFT=0 # same idea for left side of river
RIGHT=1 # etc.

class State():

  def __init__(self, d=None):
    if d==None: 
      d = {'Left bank':['Farmer','Fox','Chicken','Grain'],
           'Boat':'left',
           'Right bank':[]}
    self.d = d

  def __eq__(self,s2):
    for prop in ['Left bank', 'Boat', 'Right bank']:
      if self.d[prop] != s2.d[prop]: return False
    return True

  def __str__(self):
    # Produces a textual description of a state.
    p = self.d['Left bank']
    txt = 'Left bank:\n'
    for item in p:
      txt += item + ' '
    txt += 'Boat side:\n'
    txt += self.d['Boat']+".\n"
    txt += 'Right bank:\n'
    p = self.d['Right bank']
    for item in p:
      txt += item + ' '
    return txt

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State({})
    news.d['Left bank']=[self.d['Left bank'][:]]
    news.d['Boat'] = self.d['Boat']
    news.d['Reft bank']=[self.d['Reft bank'][:]]
    return news 

  def sideItems(self, side):
    '''
    Get the animals from the side  
    '''
    if side == 'left':
      p = self.d['Left bank']
    elif side == 'right':
      p = self.d['Right bank']
    return p
  
  def removeAnimal(self, p, animal):
    '''
    Remove the animal from one side
    '''
    newp = []
    for a in p:
      newp.append(a)
    newp.remove(animal)
    return newp

  def addAnimal(self, p, animal):
    '''
    Add the animal from one side
    '''
    newp = []
    for a in p:
      newp.append(a)
    newp.append(animal)
    return newp

  def anotherSide(self, side):
    '''
    Get other side name
    '''
    if side == 'left':
      anotherSide = 'right'
    elif side == 'right':
      anotherSide = 'left'
    return anotherSide

  def availableCheck(self, p):
    '''
    'Chicken' and 'Grain' or 'Fox' and 'Chicken' cannot on either side
    '''
    if p.count('Chicken') > 1 and p.count('Grain') > 1:
      return True
    if p.count('Chicken') > 1 and p.count('Fox') > 1:
      return True
    return False

  def can_move(self,animal):
    '''Tests whether it's legal to move the boat and take
     1 farmer and 1 animal.'''
    side = self.d['Boat'] # Where the boat is.
    anotherSide = self.anotherSide(side)
    p = self.sideItems(side)
    otherp = self.sideItems(anotherSide)
 
    if p.count('Farmer')<1: return False # Need an farmer to steer boat.
    if animal == '': return True # Farmer steer boat to other side with nothing
    if p.count(animal)<1: return False # There is no this kind of animal on this side

    p_remaining = self.removeAnimal(p,animal)
    p_remaining = self.removeAnimal(p_remaining,'Farmer')

    # 'Chicken' and 'Grain' or 'Fox' and 'Chicken' cannot on either side:

    if self.availableCheck(p_remaining): return False
    otherp_remaining =  self.addAnimal(otherp,animal)
    otherp_remaining =  self.addAnimal(otherp_remaining,'Farmer')
    if self.availableCheck(otherp_remaining): return False
    return True


  def move(self,animal):
    '''Assuming it's legal to make the move, this computes
     the new state resulting from moving the boat carrying
     m missionaries and c cannibals.'''
    news = self.copy()      # start with a deep copy.
    side = self.d['Boat']         # where is the boat?
    anotherSide = self.anotherSide(side)
    p = self.sideItems(side)         # get the array of one side.
    otherp = self.sideItems(anotherSide)

    if animal == '':
      # Just move the farmer
      p[side] = p[side].remove('Farmer')
      p[otherp] = p[otherp].append('Farmer')
    else:
      p[side] = p[side].remove(animal)     # Remove people from the current side.
      p[side] = p[side].remove('Farmer')
      p[otherp] = p[otherp].append(animal) # Add them at the other side.
      p[otherp] = p[otherp].append('Farmer')
    news.d['Boat'] = anotherSide       # Move the boat itself.
    return news

def goal_test(s):
  '''If all Ms and Cs are on the right, then s is a goal state.'''
  p = s.d['Right side']
  return (len(p) == 4)

def goal_message(s):
  return "Congratulations on successfully guiding the all staff across the river!"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
CREATE_INITIAL_STATE = lambda : State(d={'Left bank':['Farmer','Fox','Chicken','Grain'],
           'Boat':'left',
           'Right bank':[]})
#</INITIAL_STATE>

#<OPERATORS>
MC_combinations = ['','Fox','Chicken','Grain']

for animal in MC_combinations:
  if animal == '':
    OPERATORS = [Operator("Cross the river with one Farmer",
      lambda s, a=animal: s.can_move(a),
      lambda s, a=animal: s.move(a))]
  else:
    OPERATORS = [Operator("Cross the river with one Farmer and one " + animal,
      lambda s, a=animal: s.can_move(a),
      lambda s, a=animal: s.move(a) )] 
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>
