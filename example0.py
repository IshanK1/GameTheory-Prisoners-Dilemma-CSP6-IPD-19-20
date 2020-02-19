

'''Information and description on this strategy.'''
team_name = '3*Team to be determined*'
strategy_name = "Trust, then don't forgive"
strategy_description = 'Collude first. If opponent betrays at any point in the game, betray forever.'
   
def move(my_history, their_history, my_score, their_score):
  '''
  This strategy Colludes when the length of my_history = 0. Then, colludes until betrayed, then always betrays.

  history: a string with one letter (c or b) per round that has been played with this opponent.
  their_history: a string of the same length as history, possibly empty. 
  The first round between these two players is my_history[0] and their_history[0]
  The most recent round is my_history[-1] and their_history[-1]
    
  Returns 'c' or 'b' for collude or betray.
  '''
  # This player colludes on even numbered rounds (first round is round #0).
  if len(str(my_history)) == 0: # It's the first round, so collude.
    return 'c'
  elif len(str(my_history)) > 0 and their_history == 'b':#Executes if opponent betrays in a round after the first one, will betray forever. 
    return 'b'
  else:#Executes if the opponent never betrays 
    return 'c'

move(0,0,0,0)#Calls the function with appropriate starting values