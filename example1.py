
'''Information and description on this strategy.'''
team_name = '2*Team to be determined*'
strategy_name = "Collude then Mimic "
strategy_description = "Collude, then start to mimic whatever the last person's choice was."
    
def move(my_history, their_history, my_score, their_score):
  '''
  This strategy colludes first. Then, always mimics the other player's choice to collud or betray based on the value of "their_history'. 

  their_history: a string of the same length as history, possibly empty. 
  The first round between these two players is my_history[0] and their_history[0]
  The most recent round is my_history[-1] and their_history[-1]
    
  Returns 'c' or 'b' for collude or betray.
  '''

  if len(str(my_history)) == 0: # It's the first round; collude.
    return 'c'
  elif their_history =='b':
    return 'b'
  else:
    return 'c'

move(0,0,0,0)#Calls the function with appropriate starting values