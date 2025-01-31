'''PlayerSkeletonA.py
The beginnings of an agent that might someday play Baroque Chess.

'''

import BC_state_etc as BC
import BC_checker as BC_c

def parameterized_minimax(currentState, alphaBeta=False, ply=3,\
    useBasicStaticEval=True, useZobristHashing=False):
  '''Implement this testing function for your agent's basic
  capabilities here.'''

   
  pass

# Max: Ture, MIn: False
def minmax(currentState, ply, MaxOrMin = False):
  children, comment = BC_c.any_moves(currentState.board_string, currentState.whose_move)
  if ply == 0 or FinalNode(currentState):
    return ply
  if MaxOrMin:
    value = -1000
    for child in children:
      value = max(value, minmax(child, ply-1, False))
      #value = max(value, minmax(child, ply − 1, False))
    return value
  else:
    value = 1000
    for child in children:
      value = min(value, minmax(child, ply-1, True))
    return value

def FinalNode(s):
  finalnode = False
  black_king_detected = False
  white_king_detected = False

  b = s.board
  for i in range(8):
    for j in range(8):
      if b[i][j] == BC.BLACK_KING: black_king_detected = True
      if b[i][j] == BC.WHITE_KING: white_king_detected = True
  if white_king_detected and not black_king_detected: finalnode = True
  if black_king_detected and not white_king_detected: finalnode = True
  return finalnode


def makeMove(currentState, currentRemark, timelimit=10):
    # Compute the new state for a move.
    # You should implement an anytime algorithm based on IDDFS.

    # The following is a placeholder that just copies the current state.
    newState = BC.BC_state(currentState.board)

    # Fix up whose turn it will be.
    newState.whose_move = 1 - currentState.whose_move
    
    # Construct a representation of the move that goes from the
    # currentState to the newState.
    # Here is a placeholder in the right format but with made-up
    # numbers:
    move = ((6, 4), (3, 4))

    # Make up a new remark
    newRemark = "I'll think harder in some future game. Here's my move"

    return [[move, newState], newRemark]

def nickname():
    return "Newman"

def introduce():
    return "I'm Newman Barry, a newbie Baroque Chess agent."

def prepare(player2Nickname):
    ''' Here the game master will give your agent the nickname of
    the opponent agent, in case your agent can use it in some of
    the dialog responses.  Other than that, this function can be
    used for initializing data structures, if needed.'''
    pass

def basicStaticEval(state):
    '''Use the simple method for state evaluation described in the spec.
    This is typically used in parameterized_minimax calls to verify
    that minimax and alpha-beta pruning work correctly.'''
    pass

def staticEval(state):
    '''Compute a more thorough static evaluation of the given state.
    This is intended for normal competitive play.  How you design this
    function could have a significant impact on your player's ability
    to win games.'''
    pass

